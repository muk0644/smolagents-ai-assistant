import os
import datetime
import pytz
import random
import requests
from smolagents import tool, Tool
from huggingface_hub import list_models

# LangChain imports will be done dynamically in the function to avoid import errors
# if langchain-community is not installed yet

# --- Function-Based Tools ---

@tool
def my_custom_tool(arg1: str, arg2: int) -> str:
    """A sample tool to demonstrate custom function creation.
    Args:
        arg1: The first argument (text description).
        arg2: The second argument (numeric value).
    """
    return "Function execution successful."

@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """Fetches the current local time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        tz = pytz.timezone(timezone)
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"Current time in {timezone}: {local_time}"
    except Exception as e:
        return f"Error fetching time: {str(e)}"

@tool
def suggest_menu(occasion: str) -> str:
    """Suggests a menu based on the specified occasion.
    Args:
        occasion: The type of occasion ('casual', 'formal', 'superhero', 'custom').
    """
    menus = {
        "casual": "Pizza, snacks, and soft drinks.",
        "formal": "3-course dinner with wine selection.",
        "superhero": "High-protein buffet and energy drinks.",
        "custom": "Chef's choice custom menu."
    }
    return menus.get(occasion, "Standard catering menu.")

@tool
def catering_service_tool(query: str) -> str:
    """Returns the highest-rated catering service in the database.
    Args:
        query: Search term for catering services.
    """
    services = {
        "Gotham Catering Co.": 4.9,
        "Wayne Manor Catering": 4.8,
        "Gotham City Events": 4.7,
    }
    best_service = max(services, key=services.get)
    return f"Top result for '{query}': {best_service} (Rating: {services[best_service]}/5.0)"

# --- Class-Based Tools ---

class SuperheroPartyThemeTool(Tool):
    name = "superhero_party_theme_generator"
    description = "Generates creative superhero-themed party concepts based on a category."
    inputs = {"category": {"type": "string", "description": "The category."}}
    output_type = "string"

    def forward(self, category: str):
        themes = {
            "classic heroes": "Justice League Gala.",
            "villain masquerade": "Gotham Rogues' Ball.",
            "futuristic gotham": "Neo-Gotham Cyberpunk Night."
        }
        return themes.get(category.lower(), "Standard Superhero Theme.")

class WeatherInfoTool(Tool):
    name = "weather_info"
    description = "Fetches real-time weather data for a specific location using OpenWeatherMap API."
    inputs = {"location": {"type": "string", "description": "Target city or region (e.g., 'Berlin', 'New York')."}}
    output_type = "string"

    def forward(self, location: str):
        api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
        if not api_key:
            return "Error: OPENWEATHERMAP_API_KEY not found in .env file."
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
            
            # FIXED: Added timeout=10 to prevent infinite hanging and satisfy Bandit B113
            response = requests.get(url, timeout=10) 
            
            data = response.json()
            if response.status_code == 200:
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                return f"Current weather in {location}: {desc}, {temp}°C"
            else:
                return f"Error fetching weather: {data.get('message', 'City not found or API error')}"
        except requests.exceptions.Timeout:
            return f"Error: The request to the weather service timed out."
        except Exception as e:
            return f"API Request Error: {str(e)}"

class HubStatsTool(Tool):
    name = "hub_stats"
    description = "Retrieves the most downloaded model for a specific author from Hugging Face."
    inputs = {"author": {"type": "string", "description": "Username."}}
    output_type = "string"

    def forward(self, author: str):
        try:
            models = list(list_models(author=author, sort="downloads", direction=-1, limit=1))
            if models:
                m = models[0]
                return f"Top model by {author}: {m.id} ({m.downloads:,} downloads)."
            return f"No models found for: {author}"
        except Exception as e:
            return f"API Error: {str(e)}"

# --- LangChain Integration: SerpAPI Tool ---

def create_serpapi_langchain_tool():
    """Creates a SerpAPI search tool from LangChain integration.
    
    Note: Requires SERPAPI_API_KEY to be set in environment variables (.env file).
    The key is automatically loaded from .env by python-dotenv.
    
    Returns:
        Tool: SerpAPI tool wrapped for smolagents compatibility
    """
    try:
        # Dynamic import to avoid errors if langchain-community not installed
        from langchain.agents import load_tools  # type: ignore
        
        # Load SerpAPI tool from LangChain (requires SERPAPI_API_KEY in environment)
        langchain_tools = load_tools(["serpapi"])
        serpapi_tool = Tool.from_langchain(langchain_tools[0])
        return serpapi_tool
    except ImportError as ie:
        print(f"⚠️ Warning: langchain-community not installed: {str(ie)}")
        print("Run: pip install langchain-community")
        return None
    except Exception as e:
        print(f"⚠️ Warning: Could not load SerpAPI LangChain tool: {str(e)}")
        print("Make sure SERPAPI_API_KEY is set in your .env file")
        return None

# --- Custom Knowledge Base: Party Planning Retriever ---

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
            from langchain_community.docstore.document import Document  # type: ignore
            from langchain_text_splitters import RecursiveCharacterTextSplitter  # type: ignore
            from langchain_community.retrievers import BM25Retriever  # type: ignore
            
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