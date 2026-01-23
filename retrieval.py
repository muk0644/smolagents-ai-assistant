"""
RAG (Retrieval Augmented Generation) Module

This module contains retrieval-based tools for the smolagents AI assistant.
It implements semantic search functionality using BM25 algorithm and LangChain
integration for knowledge base retrieval.

All RAG/retrieval logic is isolated here.
"""

import datasets
from smolagents import Tool
from langchain_community.docstore.document import Document  # type: ignore
from langchain_text_splitters import RecursiveCharacterTextSplitter  # type: ignore
from langchain_community.retrievers import BM25Retriever  # type: ignore


class PartyPlanningRetrieverTool(Tool):
    """Semantic search tool for party planning knowledge base.
    
    Uses BM25 retrieval to find relevant party planning ideas from a curated
    knowledge base of superhero-themed event suggestions including entertainment,
    catering, decoration, and interactive experiences.
    """
    name = "party_planning_retriever"
    description = (
        "Uses semantic search to retrieve relevant party planning ideas for "
        "superhero-themed parties. Returns top 5 most relevant suggestions "
        "covering entertainment, catering, decorations, and interactive experiences."
    )
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. Should be related to party planning or superhero themes.",
        }
    }
    output_type = "string"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._initialize_knowledge_base()

    def _initialize_knowledge_base(self):
        """Initialize the knowledge base and retriever."""
        try:
            # Curated knowledge base for party planning
            party_ideas = [
                {
                    "text": "A superhero-themed masquerade ball with luxury decor, including gold accents, velvet curtains, and crystal chandeliers creating an elegant Gotham atmosphere.",
                    "source": "Party Ideas"
                },
                {
                    "text": "Hire a professional DJ who can play themed music for superheroes like Batman, Wonder Woman, and Superman. Include iconic movie soundtracks and epic orchestral pieces.",
                    "source": "Entertainment Ideas"
                },
                {
                    "text": "For catering, serve gourmet dishes named after superheroes: 'The Hulk's Green Smoothie', 'Iron Man's Power Steak', 'Wonder Woman's Warrior Salad', and 'Batman's Dark Knight Chocolate Cake'.",
                    "source": "Catering Ideas"
                },
                {
                    "text": "Decorate with iconic superhero logos and projections of Gotham, Metropolis, and other superhero cities around the venue. Use dramatic lighting and fog machines.",
                    "source": "Decoration Ideas"
                },
                {
                    "text": "Interactive VR experiences where guests can engage in superhero simulations, compete in themed games, or participate in escape room challenges based on comic book storylines.",
                    "source": "Entertainment Ideas"
                },
                {
                    "text": "Hire professional actors dressed as beloved superheroes and villains to interact with guests, pose for photos, and perform short theatrical skits.",
                    "source": "Entertainment Ideas"
                },
                {
                    "text": "Create a luxury photo booth area with superhero props, capes, masks, and a green screen for custom superhero backgrounds.",
                    "source": "Photo Opportunities"
                },
                {
                    "text": "Serve signature cocktails named after heroes: 'The Kryptonite Martini', 'Thor's Thunder Punch', 'Black Widow's Red Velvet', and non-alcoholic 'Captain America's Shield Smoothie'.",
                    "source": "Beverage Ideas"
                },
                {
                    "text": "Design custom invitations that look like comic book covers featuring the guest of honor as a superhero, complete with action scenes and dramatic headlines.",
                    "source": "Invitation Ideas"
                },
                {
                    "text": "Set up themed zones: The Batcave lounge area, Fortress of Solitude VIP section, and Avengers Assembly dance floor with distinct decorations for each.",
                    "source": "Venue Layout"
                }
            ]
            
            # Create documents
            source_docs = [
                Document(page_content=doc["text"], metadata={"source": doc["source"]})
                for doc in party_ideas
            ]
            
            # Split documents into chunks for efficient search
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50,
                add_start_index=True,
                strip_whitespace=True,
                separators=["\n\n", "\n", ".", " ", ""],
            )
            docs_processed = text_splitter.split_documents(source_docs)
            
            # Create BM25 retriever
            self.retriever = BM25Retriever.from_documents(
                docs_processed, k=5  # Retrieve top 5 documents
            )
            
        except ImportError as ie:
            print(f"⚠️ Warning: Required packages not installed: {str(ie)}")
            print("Run: pip install langchain-community langchain-text-splitters rank-bm25")
            self.retriever = None
        except Exception as e:
            print(f"⚠️ Warning: Could not initialize Party Planning Retriever: {str(e)}")
            self.retriever = None

    def forward(self, query: str) -> str:
        """Retrieve relevant party planning ideas based on the query."""
        if self.retriever is None:
            return "Error: Party Planning Retriever not properly initialized. Please check dependencies."
        
        assert isinstance(query, str), "Your search query must be a string"
        
        try:
            docs = self.retriever.invoke(query)
            
            if not docs:
                return "No relevant party planning ideas found for your query."
            
            result = "\n🎉 Retrieved Party Planning Ideas:\n"
            result += "=" * 60 + "\n"
            
            for i, doc in enumerate(docs, 1):
                source = doc.metadata.get("source", "Unknown Source")
                result += f"\n💡 Idea {i} ({source}):\n"
                result += f"{doc.page_content}\n"
                result += "-" * 60 + "\n"
            
            return result
            
        except Exception as e:
            return f"Error retrieving party planning ideas: {str(e)}"


# --- Guest Information Retriever Tool ---

class GuestInfoRetrieverTool(Tool):
    """Retrieves detailed information about party guests from Hugging Face dataset.
    
    Uses BM25 retrieval to find relevant guest information including names,
    relations, descriptions, and email addresses from the agents-course/unit3-invitees
    dataset.
    """
    name = "guest_info_retriever"
    description = (
        "Retrieves detailed information about gala guests based on their name or relation. "
        "Returns guest details including name, relation to host, biography, and email address."
    )
    inputs = {
        "query": {
            "type": "string",
            "description": "The name or relation of the guest you want information about."
        }
    }
    output_type = "string"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._initialize_guest_dataset()

    def _initialize_guest_dataset(self):
        """Load guest dataset from Hugging Face and initialize retriever."""
        try:
            # Load the dataset from Hugging Face
            guest_dataset = datasets.load_dataset("agents-course/unit3-invitees", split="train")
            
            # Convert dataset entries into Document objects
            docs = [
                Document(
                    page_content="\n".join([
                        f"Name: {guest['name']}",
                        f"Relation: {guest['relation']}",
                        f"Description: {guest['description']}",
                        f"Email: {guest['email']}"
                    ]),
                    metadata={"name": guest["name"]}
                )
                for guest in guest_dataset
            ]
            
            # Create BM25 retriever with top 3 results
            self.retriever = BM25Retriever.from_documents(docs, k=3)
            
        except ImportError as ie:
            print(f"⚠️ Warning: Required packages not installed: {str(ie)}")
            print("Run: pip install datasets langchain-community rank-bm25")
            self.retriever = None
        except Exception as e:
            print(f"⚠️ Warning: Could not load guest dataset: {str(e)}")
            print("Make sure you have internet connection to download the dataset.")
            self.retriever = None

    def forward(self, query: str) -> str:
        """Retrieve relevant guest information based on the query."""
        if self.retriever is None:
            return "Error: Guest Info Retriever not properly initialized. Please check dependencies and internet connection."
        
        assert isinstance(query, str), "Your search query must be a string"
        
        try:
            results = self.retriever.get_relevant_documents(query)
            
            if not results:
                return "No matching guest information found."
            
            # Return top 3 results combined
            return "\n\n".join([doc.page_content for doc in results[:3]])
            
        except Exception as e:
            return f"Error retrieving guest information: {str(e)}"

