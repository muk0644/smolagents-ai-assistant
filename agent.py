import os
from dotenv import load_dotenv
from smolagents import (
    CodeAgent, 
    InferenceClientModel, 
    load_tool, 
    FinalAnswerTool,
    DuckDuckGoSearchTool, 
    VisitWebpageTool,
    WebSearchTool,
    GoogleSearchTool,
    PythonInterpreterTool
)

# Import custom tools from your local file
from tools import (
    my_custom_tool, 
    get_current_time_in_timezone, 
    suggest_menu, 
    catering_service_tool, 
    SuperheroPartyThemeTool, 
    WeatherInfoTool, 
    HubStatsTool
)

load_dotenv()

def initialize_agent():
    """Initializes and returns the CodeAgent with all tools configured."""
    
    # 1. Initialize Standard Tools
    final_answer = FinalAnswerTool()
    python_tool = PythonInterpreterTool()
    image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)
    visit_webpage_tool = VisitWebpageTool()
    
    # Search Tools
    duckduckgo_tool = DuckDuckGoSearchTool()
    duckduckgo_tool.name = "duckduckgo_search"
    
    google_search_tool = GoogleSearchTool()
    google_search_tool.name = "google_search"
    
    web_search_tool = WebSearchTool()

    # 2. Initialize Custom Tools
    superhero_tool = SuperheroPartyThemeTool()
    weather_tool = WeatherInfoTool()
    hub_stats_tool = HubStatsTool()

    # 3. Configure Model
    model = InferenceClientModel(
        model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
        max_tokens=2096,
        temperature=0.5,
    )

    # 4. Collect All Tools
    all_tools = [
        final_answer, 
        python_tool, 
        get_current_time_in_timezone, 
        image_generation_tool, 
        my_custom_tool, 
        suggest_menu, 
        catering_service_tool, 
        superhero_tool, 
        weather_tool, 
        hub_stats_tool, 
        visit_webpage_tool, 
        duckduckgo_tool, 
        web_search_tool, 
        google_search_tool
    ]

    # 5. Create Agent
    agent = CodeAgent(
        model=model,
        tools=all_tools,
        max_steps=10,
        verbosity_level=1
    )
    
    return agent