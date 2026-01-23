"""
RAG (Retrieval Augmented Generation) Module

This module contains retrieval-based tools for the smolagents AI assistant.
It implements semantic search functionality using BM25 algorithm and LangChain
integration for knowledge base retrieval.

All RAG/retrieval logic is isolated here.
"""

import json
import os
from pathlib import Path
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
    """Retrieves information about party guests using Chroma Vector Database.
    
    Loads guest data from a local JSON file and uses Chroma DB for semantic search
    with embeddings. This approach is more reliable than external datasets and works
    seamlessly on both local and cloud deployments.
    """
    name = "guest_info_retriever"
    description = (
        "Retrieves detailed information about gala guests based on their name or relation. "
        "Returns guest details including name, relation to host, biography, and email address. "
        "Uses Chroma vector database for semantic search."
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
        self.collection = None
        self._initialize_chroma_db()

    def _initialize_chroma_db(self):
        """Load guest data from JSON and initialize Chroma DB."""
        try:
            import chromadb
            
            # Find guests.json file (in same directory as this script)
            current_dir = Path(__file__).parent
            json_path = current_dir / "guests.json"
            
            # Load guest data from JSON
            with open(json_path, "r", encoding="utf-8") as f:
                guests_data = json.load(f)
            
            # Create Chroma client (in-memory, no persistence needed)
            client = chromadb.Client()
            
            # Create or get collection
            self.collection = client.get_or_create_collection(
                name="party_guests",
                metadata={"description": "Guest information for gala party"}
            )
            
            # Add guest documents to Chroma
            for idx, guest in enumerate(guests_data):
                document_text = "\n".join([
                    f"Name: {guest['name']}",
                    f"Relation: {guest['relation']}",
                    f"Description: {guest['description']}",
                    f"Email: {guest['email']}"
                ])
                
                self.collection.add(
                    ids=[str(idx)],
                    documents=[document_text],
                    metadatas=[{"name": guest["name"], "email": guest["email"]}]
                )
            
            print(f"✅ Chroma DB initialized with {len(guests_data)} guests")
            
        except ImportError:
            print("⚠️ Warning: chromadb not installed. Run: pip install chromadb")
            self.collection = None
        except FileNotFoundError:
            print(f"⚠️ Warning: guests.json not found at {json_path}")
            self.collection = None
        except Exception as e:
            print(f"⚠️ Warning: Failed to initialize Chroma DB: {str(e)}")
            self.collection = None

    def forward(self, query: str) -> str:
        """Retrieve relevant guest information using Chroma DB semantic search."""
        if self.collection is None:
            return "Error: Guest Info Retriever not properly initialized. Please check if chromadb is installed and guests.json exists."
        
        assert isinstance(query, str), "Your search query must be a string"
        
        try:
            # Query Chroma DB for similar documents
            results = self.collection.query(
                query_texts=[query],
                n_results=3
            )
            
            if not results['documents'] or not results['documents'][0]:
                return "No matching guest information found."
            
            # Return top 3 results combined
            return "\n\n".join(results['documents'][0])
            
        except Exception as e:
            return f"Error retrieving guest information: {str(e)}"

