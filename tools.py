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
        # Dynamic import using the correct modern path for LangChain
        from langchain_community.utilities import SerpAPIWrapper  # type: ignore
        
        # Create SerpAPI wrapper (automatically uses SERPAPI_API_KEY from environment)
        search = SerpAPIWrapper()
        
        # Create a simple tool wrapper for smolagents
        class SerpAPITool(Tool):
            name = "serpapi_search"
            description = "Search the internet using SerpAPI for real-time information, news, and data."
            inputs = {"query": {"type": "string", "description": "The search query"}}
            output_type = "string"
            
            def forward(self, query: str) -> str:
                try:
                    return search.run(query)
                except Exception as e:
                    return f"SerpAPI search error: {str(e)}"
        
        return SerpAPITool()
        
    except ImportError as ie:
        print(f"⚠️ Warning: langchain-community not installed: {str(ie)}")
        print("Run: pip install langchain-community")
        return None
    except Exception as e:
        print(f"⚠️ Warning: Could not load SerpAPI LangChain tool: {str(e)}")
        print("Make sure SERPAPI_API_KEY is set in your .env file")
        return None