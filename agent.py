import os
from dotenv import load_dotenv
from smolagents import (
    CodeAgent, 
    InferenceClientModel,
    LiteLLMModel,
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
    HubStatsTool,
    create_serpapi_langchain_tool
)

load_dotenv()

def initialize_agent(selected_model_id="qwen"):
    """Initializes and returns the CodeAgent with all tools configured.
    
    Args:
        selected_model_id (str): The model to use. Options:
            - "qwen": Qwen2.5-Coder-32B-Instruct (HuggingFace)
            - "gemini-2.5-flash": Google Gemini 2.5 Flash
    
    Returns:
        CodeAgent: Configured agent with selected model
    """
    
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
    
    # Initialize LangChain SerpAPI tool (if available)
    serpapi_langchain_tool = create_serpapi_langchain_tool()

    # 3. Configure Model based on selection
    if selected_model_id == "qwen":
        # Original Qwen implementation (HuggingFace)
        model = InferenceClientModel(
            model_id='Qwen/Qwen2.5-Coder-32B-Instruct',
            max_tokens=2096,
            temperature=0.5,
        )
    elif selected_model_id == "gemini-2.5-flash":
        # Google Gemini 2.5 Flash
        google_api_key = os.getenv("GOOGLE_API_KEY")
        if not google_api_key:
            raise ValueError(
                "GOOGLE_API_KEY not found in environment variables. "
                "Please add it to your .env file."
            )
        
        try:
            model = LiteLLMModel(
                model_id="gemini/gemini-2.5-flash",
                api_key=google_api_key,
                max_tokens=2096,
                temperature=0.5,
            )
        except Exception as e:
            # Enable debug to see full error
            import litellm
            litellm._turn_on_debug()
            print(f"❌ LiteLLM Error with Gemini 2.5 Flash: {str(e)}")
            raise
    else:
        raise ValueError(f"Unknown model_id: {selected_model_id}")

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
    
    # Add LangChain SerpAPI tool if successfully loaded
    if serpapi_langchain_tool is not None:
        all_tools.append(serpapi_langchain_tool)

    # 5. Create Agent
    agent = CodeAgent(
        model=model,
        tools=all_tools,
        max_steps=10,
        verbosity_level=1
    )
    
    return agent