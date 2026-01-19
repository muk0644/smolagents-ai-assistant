# 🤖 SmolAgents AI Assistant

<div align="center">

![SmolAgents Logo](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/smolagents/smolagents.png)

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/YOUR_USERNAME/smolagents-ai-assistant)
[![Deploy](https://img.shields.io/badge/Deploy-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow?style=for-the-badge)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

**An intelligent AI agent with advanced features for web search, weather queries, image generation and more!**

> **📌 Suggested Repository Names:**
> - `smolagents-ai-assistant` ⭐ (Recommended)
> - `ai-agent-portfolio`
> - `qwen-smol-agent`
> - `intelligent-agent-hub`

> **📝 Repository Description:**
> *"🤖 Intelligent AI agent powered by smolagents & Qwen2.5-Coder. Features: Web search, real-time weather, image generation, Python execution, and custom tools. Built with Streamlit for an intuitive chat interface."*

[Demo](#-demo) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-architecture) • [Tools](#-tools)

</div>

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Architecture](#-project-architecture)
- [Available Tools](#-available-tools)
- [Code Structure](#-code-structure)
- [Technology Stack](#-technology-stack)
- [API Keys](#-api-keys)
- [Development](#-development)
- [Examples](#-examples)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 About the Project

This project is a **fully functional AI agent** built with the **smolagents** library from Hugging Face. The agent uses the powerful **Qwen2.5-Coder-32B-Instruct** model and provides a user-friendly **Streamlit** interface.

The agent can:
- 🌐 **Perform web research** (DuckDuckGo, Google)
- 🌤️ **Retrieve real-time weather data**
- 🎨 **Generate images** (Text-to-Image)
- 🧮 **Execute Python code** for mathematical calculations
- 🎉 **Generate party plans** and event ideas
- 📊 **Retrieve Hugging Face Hub statistics**
- ⏰ **Provide timezone information**

---

## ✨ Features

### 🔍 Intelligent Web Search
- **DuckDuckGo Integration**: Privacy-friendly search
- **Google Search**: Comprehensive web research
- **Webpage Visitor**: Extracts content from URLs

### 🌦️ Real-Time Weather
- Live weather data via OpenWeatherMap API
- Temperature, weather description and more
- Support for all cities worldwide

### 🎨 Image Generation
- Text-to-Image with Hugging Face Models
- Automatic saving to `generated_images/`
- High-resolution output

### 🧮 Python Interpreter
- Executes Python code directly
- Mathematical calculations
- Data processing

### 🎉 Custom Tools
- **Party Planner**: Superhero theme generator
- **Catering Service**: Restaurant recommendations
- **Menu Suggestions**: Based on occasion
- **Hub Statistics**: Download numbers from models

---

## 🖼️ Demo

### Main Interface
```
🕵️ SmolAgents AI Assistant
┌─────────────────────────────────────┐
│  🌤️  Weather in Berlin right now?  │
│  🔍  Who is the CEO of Hugging Face?│
│  🎨  Generate a cyberpunk city      │
│  🧮  Calculate sqrt(123456789) * pi │
└─────────────────────────────────────┘
```

### Example Interactions

**User**: "Weather in Erkner right now"  
**Agent**: "Current weather in Erkner: clear sky, 12°C"

**User**: "Generate an image of a sunset over mountains"  
**Agent**: *[Generates and displays image]*

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python Package Manager)
- Git

### Step 1: Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/smolagents-ai-assistant.git
cd smolagents-ai-assistant
```

### Step 2: Create Virtual Environment (recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory:
```env
HF_TOKEN=your_huggingface_token_here
OPENWEATHERMAP_API_KEY=your_openweather_api_key_here
SERPAPI_API_KEY=your_serpapi_key_here  # Optional for Google Search
```

---

## 🔐 Configuration

### Hugging Face Token
1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Create a new Access Token
3. Copy the token to the `.env` file

### OpenWeatherMap API Key
1. Register at [OpenWeatherMap](https://openweathermap.org/api)
2. Generate a free API key
3. Add it to the `.env` file

### SerpAPI Key (Optional)
1. Register at [SerpAPI](https://serpapi.com/)
2. Get your API key
3. Add it to the `.env` file

---

## 🚀 Usage

### Start Streamlit App
```bash
streamlit run app.py
```

The application will automatically open in your browser at `http://localhost:8501`

### Use Agent Directly (Python)
```python
from agent import initialize_agent

# Initialize agent
agent = initialize_agent()

# Make a request
response = agent.run("What's the weather in Berlin?")
print(response)
```

---

## 🏗️ Project Architecture

```
smolagents-ai-assistant/
│
├── app.py                  # Streamlit Frontend
├── agent.py               # Agent configuration & initialization
├── tools.py               # Custom tool definitions
├── requirements.txt       # Python dependencies
│
├── README.md             # Complete documentation
├── LICENSE               # MIT License
├── .gitignore            # Git ignore rules
│
├── .env                   # Environment variables (create from .env.example)
├── .env.example          # Template for environment variables
│
├── generated_images/     # Generated images (AI outputs)
│   └── .gitkeep          # Keep folder in Git
│
└── __pycache__/         # Python cache (ignored by Git)
```

---

## 🛠️ Available Tools

### Standard Tools (smolagents)
| Tool | Description | Usage |
|------|--------------|------------|
| `FinalAnswerTool` | Returns final answer | Automatic |
| `PythonInterpreterTool` | Executes Python code | Math, calculations |
| `DuckDuckGoSearchTool` | Web search (DuckDuckGo) | Privacy-friendly |
| `GoogleSearchTool` | Web search (Google) | Comprehensive search |
| `VisitWebpageTool` | Extracts webpage content | URL analysis |
| `WebSearchTool` | Generic web search | Flexible |

### Custom Tools

#### 1️⃣ **WeatherInfoTool** 🌤️
```python
# Usage by agent
"Weather in Erkner right now"
```
- Provides real-time weather data
- Uses OpenWeatherMap API
- Format: Description + Temperature in °C

#### 2️⃣ **SuperheroPartyThemeTool** 🦸
```python
# Usage by agent
"Plan a superhero party for Batman"
```
- Generates creative party themes
- Categories: Classic Heroes, Villain Masquerade, Futuristic Gotham

#### 3️⃣ **HubStatsTool** 📊
```python
# Usage by agent
"Most downloaded model by OpenAI"
```
- Shows top model from Hugging Face Hub
- Download statistics
- Author-based search

#### 4️⃣ **get_current_time_in_timezone** ⏰
```python
# Usage by agent
"What time is it in New York?"
```
- Worldwide timezone support
- Format: YYYY-MM-DD HH:MM:SS

#### 5️⃣ **suggest_menu** 🍽️
```python
# Usage by agent
"Suggest a menu for a formal dinner"
```
- Menu suggestions based on occasion
- Categories: Casual, Formal, Superhero, Custom

#### 6️⃣ **catering_service_tool** 🍴
```python
# Usage by agent
"Find best catering service in Gotham"
```
- Restaurant ratings
- Top service with rating

#### 7️⃣ **Text-to-Image Generation** 🎨
```python
# Usage by agent
"Generate an image of a cyberpunk city"
```
- Uses Hugging Face Diffusion Models
- Saves to `generated_images/`

---

## 💻 Code Structure

### `agent.py` - Agent Initialization
```python
def initialize_agent():
    """
    Creates and configures the CodeAgent with:
    - Qwen2.5-Coder-32B-Instruct Model
    - All standard and custom tools
    - max_steps=10 for complex tasks
    - verbosity_level=1 for debugging
    """
```

**Key Features:**
- Modular tool integration
- Caching for better performance
- Flexible model configuration

### `app.py` - Streamlit Frontend
```python
# Main components:
- Session State Management
- Chat History
- Avatar Icons (Agent & User)
- Image Display Logic
- Error Handling
```

**UI Features:**
- Responsive Design
- Chat-based interaction
- Automatic image display
- "New Chat" button

### `tools.py` - Tool Definitions

#### Function-based Tools (`@tool` Decorator)
```python
@tool
def my_custom_tool(arg1: str, arg2: int) -> str:
    """Example tool with typing"""
    return "Function execution successful."
```

#### Class-based Tools (`Tool` Subclass)
```python
class WeatherInfoTool(Tool):
    name = "weather_info"
    description = "Fetches real-time weather..."
    inputs = {"location": {"type": "string", ...}}
    output_type = "string"
    
    def forward(self, location: str):
        # API Call Logic
```

---

## 📚 Technology Stack

| Category | Technology | Purpose |
|-----------|-------------|--------|
| **Framework** | smolagents | Agent-Orchestrierung |
| **Frontend** | Streamlit | Web-UI |
| **LLM** | Qwen2.5-Coder-32B-Instruct | Inference Engine |
| **APIs** | Hugging Face Inference | Model Hosting |
| | OpenWeatherMap | Weather data |
| | SerpAPI | Google Search |
| **Language** | Python 3.8+ | Core Logic |
| **Libraries** | pytz | Timezones |
| | requests | HTTP Calls |
| | huggingface_hub | Hub Integration |
| | Pillow | Image processing |

---

## 🔑 API Keys

### Required Keys

#### 1. Hugging Face Token (REQUIRED)
```env
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxx
```
**How to obtain:**
- Register at [Hugging Face](https://huggingface.co)
- Go to Settings → Access Tokens
- Create a new token (Read access is sufficient)

#### 2. OpenWeatherMap API Key (REQUIRED for weather)
```env
OPENWEATHERMAP_API_KEY=xxxxxxxxxxxxxxxxxxxxx
```
**How to obtain:**
- Register at [OpenWeatherMap](https://openweathermap.org)
- Go to API Keys
- Free plan: 1,000 calls/day

#### 3. SerpAPI Key (OPTIONAL for Google Search)
```env
SERPAPI_API_KEY=xxxxxxxxxxxxxxxxxxxxx
```
**How to obtain:**
- Register at [SerpAPI](https://serpapi.com)
- Free plan: 100 searches/month

---

## 🔧 Development

### Tool Creation

#### Method 1: Function with `@tool` Decorator
```python
from smolagents import tool

@tool
def my_new_tool(param: str) -> str:
    """
    Description of your tool.
    
    Args:
        param: Parameter description
    """
    # Logic here
    return result
```

**Best Practices:**
- Klare, beschreibende Namen
- Type Hints for all parameters
- Detaillierte Docstrings mit Args-Sektion

#### Method 2: Class with `Tool` Subclass
```python
from smolagents import Tool

class MyNewTool(Tool):
    name = "my_new_tool"
    description = "What the tool does"
    inputs = {
        "param": {
            "type": "string",
            "description": "Parameter info"
        }
    }
    output_type = "string"
    
    def forward(self, param: str):
        # Logic here
        return result
```

### Adding a New Tool

1. **Define in `tools.py`**
2. **Import in `agent.py`**
3. **Add to `all_tools` list**

```python
# In agent.py
from tools import my_new_tool

all_tools = [
    final_answer,
    python_tool,
    my_new_tool,  # Add here
    # ... other tools
]
```

---

## 📖 Examples

### Example 1: Query Weather
```
User: "How's the weather in Berlin today?"

Agent:
→ Uses: weather_info tool
→ Result: "Current weather in Berlin: partly cloudy, 18°C"
```

### Example 2: Mathematical Calculation
```
User: "Calculate the square root of 123456789 multiplied by pi"

Agent:
→ Uses: PythonInterpreterTool
→ Code: import math; result = math.sqrt(123456789) * math.pi
→ Result: "34897.77..."
```

### Example 3: Image Generation
```
User: "Generate an image of a futuristic city at sunset"

Agent:
→ Uses: text-to-image tool
→ Saves: generated_images/city_sunset_123.png
→ Displays: Image in chat
```

### Example 4: Web Research
```
User: "Who is the CEO of Hugging Face?"

Agent:
→ Uses: duckduckgo_search tool
→ Visits: HF website
→ Result: "The CEO of Hugging Face is Clem Delangue."
```

### Example 5: Party Planning
```
User: "Plan a superhero party for Batman"

Agent:
→ Uses: SuperheroPartyThemeTool
→ Uses: suggest_menu
→ Uses: catering_service_tool
→ Result: Complete party plan with theme, menu, and catering
```

---

## 🐛 Troubleshooting

### Problem: "HF_TOKEN not found"
**Solution:**
```bash
# Check .env file
# Make sure HF_TOKEN is set
HF_TOKEN=hf_your_token_here
```

### Problem: Weather tool not working
**Solution:**
```bash
# Check OpenWeatherMap API Key
OPENWEATHERMAP_API_KEY=your_key_here

# Test API key validity
curl "http://api.openweathermap.org/data/2.5/weather?q=Berlin&appid=YOUR_KEY"
```

### Problem: Streamlit won't start
**Solution:**
```bash
# Port already in use? Use different port
streamlit run app.py --server.port 8502

# Or free up port 8501
netstat -ano | findstr :8501
taskkill /PID <PID> /F
```

### Problem: "Module not found"
**Solution:**
```bash
# Reinstall all dependencies
pip install -r requirements.txt --upgrade

# Or install individually
pip install smolagents streamlit python-dotenv
```

### Problem: Image generation fails
**Solution:**
```bash
# Create generated_images/ folder
mkdir generated_images

# Check write permissions
chmod 755 generated_images
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### 1. Fork the Repository
```bash
git clone https://github.com/YOUR_USERNAME/smolagents-ai-assistant.git
```

### 2. Create Branch
```bash
git checkout -b feature/neue-funktion
```

### 3. Commit Changes
```bash
git commit -m "Add: Neue Funktion XYZ"
```

### 4. Push to GitHub
```bash
git push origin feature/neue-funktion
```

### 5. Create Pull Request
Open a PR on GitHub with detailed description

---

## 📝 Tool-Entwicklungs-Guidelines

*(Completely based on `guidelineREADME.md` - Official smolagents Documentation)*

### 🎓 smolagents Tool Creation Methods

In smolagents there are **two main methods** for tool definition:

1. **@tool Decorator** - For simple function-based tools
2. **Tool Subclass** - For complex functionality with advanced metadata

---

### Method 1: `@tool` Decorator (⭐ Recommended)

The `@tool` decorator is the **recommended method** for simple tools. smolagents automatically parses:
- ✅ Funktionsnamen
- ✅ Type Hints for inputs and outputs
- ✅ Docstrings (inkl. Args-Sektion)

**Important:** All these elements are automatically integrated into the agent's system prompt!

#### Example 1: Simple Tool
```python
from smolagents import tool

@tool
def model_download_tool(task: str) -> str:
    """
    This tool returns the most downloaded model of a given task on the Hugging Face Hub.
    It returns the name of the checkpoint.

    Args:
        task: The task for which to get the download count.
    """
    from huggingface_hub import list_models
    most_downloaded_model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
    return most_downloaded_model.id
```

#### Example 2: Catering Service Tool
```python
from smolagents import tool

@tool
def catering_service_tool(query: str) -> str:
    """
    Returns the highest-rated catering service in the database.
    
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
```

**Agent initialisieren:**
```python
from smolagents import CodeAgent, InferenceClientModel

agent = CodeAgent(tools=[catering_service_tool], model=InferenceClientModel())
agent.run("Find me the best catering service")
```

---

### Method 2: `Tool` Subclass (For complex tools)

This method involves creating a subclass of `Tool`. For complex tools, we implement a class with metadata that helps the LLM use the tool effectively.

**Required attributes:**

| Attribute | Description |
|----------|--------------|
| `name` | Tool name (clear and descriptive) |
| `description` | Description for system prompt |
| `inputs` | Dictionary with `type` and `description` |
| `output_type` | Expected output type |
| `forward()` | Method with inference logic |

#### Beispiel 1: Model Download Tool
```python
from smolagents import Tool
from huggingface_hub import list_models

class ModelDownloadTool(Tool):
    name = "model_download_tool"
    description = "This tool returns the most downloaded model of a given task on the Hugging Face Hub. It returns the name of the checkpoint."
    inputs = {
        "task": {
            "type": "string", 
            "description": "The task for which to get the download count."
        }
    }
    output_type = "string"

    def forward(self, task: str) -> str:
        most_downloaded_model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
        return most_downloaded_model.id
```

#### Beispiel 2: Superhero Party Theme Generator
```python
from smolagents import Tool

class SuperheroPartyThemeTool(Tool):
    name = "superhero_party_theme_generator"
    description = "Generates creative superhero-themed party concepts based on a category."
    inputs = {
        "category": {
            "type": "string",
            "description": "The party theme category (e.g., 'classic heroes', 'villain masquerade')."
        }
    }
    output_type = "string"

    def forward(self, category: str):
        themes = {
            "classic heroes": "Justice League Gala - Celebrate iconic superheroes!",
            "villain masquerade": "Gotham Rogues' Ball - A dark and mysterious event.",
            "futuristic gotham": "Neo-Gotham Cyberpunk Night - High-tech superhero theme."
        }
        return themes.get(category.lower(), "Standard Superhero Theme.")
```

**Agent initialisieren:**
```python
from smolagents import CodeAgent, InferenceClientModel

agent = CodeAgent(tools=[ModelDownloadTool()], model=InferenceClientModel())
agent.run("Give me the most downloaded model for text-to-video task")
```

---

### 🛠️ Default Toolbox

smolagents comes with **pre-installed tools** that can be used directly:

| Tool | Description |
|------|--------------|
| `PythonInterpreterTool` | Executes Python code |
| `FinalAnswerTool` | Returns final answer |
| `UserInputTool` | Requests user input |
| `DuckDuckGoSearchTool` | Privacy-friendly web search |
| `GoogleSearchTool` | Google search |
| `VisitWebpageTool` | Extracts webpage content |
| `WebSearchTool` | Generic web search |

**Usage:**
```python
from smolagents import CodeAgent, InferenceClientModel, DuckDuckGoSearchTool, PythonInterpreterTool

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(), PythonInterpreterTool()], 
    model=InferenceClientModel()
)
```

---

### 🔗 LangChain-Integration

You can **reuse LangChain tools** in smolagents!

**Installation:**
```bash
pip install -U langchain-community
```

**SerpAPI Key setzen:**
```bash
export SERPAPI_API_KEY='your_serpapi_key'
```

**Load tool:**
```python
from langchain.agents import load_tools
from smolagents import Tool, CodeAgent, InferenceClientModel

# Convert LangChain tool to smolagents
search_tool = Tool.from_langchain(load_tools(["serpapi"])[0])

# Create agent
agent = CodeAgent(tools=[search_tool], model=InferenceClientModel())

# Use
agent.run("Search for luxury entertainment ideas for a superhero-themed event")
```

---

### ✅ Best Practices for Tool Development

1. **📛 Clear Names**
   - Self-explanatory and descriptive
   - Example: `weather_info`, not `tool1`

2. **📝 Type Hints**
   - Always for inputs and outputs
   - Helps LLM pass correct values

3. **📖 Documentation**
   - Detailed docstrings with `Args:` section
   - Each parameter should be described
   - These descriptions are instructions for the LLM!

4. **🛡️ Error Handling**
   - Try-Except blocks for external APIs
   - Meaningful error messages
   - Example:
   ```python
   try:
       response = requests.get(api_url)
       return response.json()
   except Exception as e:
       return f"API Error: {str(e)}"
   ```

5. **🧪 Testing**
   - Test tools individually before integration
   - Validate edge cases
   - Ensure output format is consistent

---

### 🎯 Tool-Format & apply_chat_template

Das Tool-Definitions-Format ist identisch mit dem, das in `apply_chat_template` verwendet wird. Der einzige Unterschied ist der hinzugefügte `@tool`-Decorator.

**More information:**
- [Tool Use API Dokumentation](https://huggingface.co/docs/transformers/chat_templating#tools-and-function-calling)
- [smolagents GitHub](https://github.com/huggingface/smolagents)

---

### 📚 Installation & Usage

**Install smolagents:**
```bash
pip install "smolagents[toolkit]"
```

**Create and use agent:**
```python
from smolagents import CodeAgent, WebSearchTool, InferenceClientModel

model = InferenceClientModel()
agent = CodeAgent(tools=[WebSearchTool()], model=model, stream_outputs=True)

# Run agent
agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")

# Share agent on Hugging Face Hub
agent.push_to_hub("username/my_agent")

# Load agent from Hub
# agent.from_hub("username/my_agent")
```

---

### 🎓 smolagents Features

| Feature | Beschreibung |
|---------|--------------|
| ✨ **Simplicity** | ~1,000 lines of code for complete agent logic |
| 🧑‍💻 **Code Agents** | Agents schreiben ihre Actions in Code |
| 🔒 **Sandboxed Execution** | Blaxel, E2B, Modal, Docker, Pyodide support |
| 🤗 **Hub Integration** | Share/Pull Tools & Agents vom HF Hub |
| 🌐 **Model-Agnostic** | Transformers, Ollama, OpenAI, Anthropic, etc. |
| 👁️ **Modality-Agnostic** | Text, Vision, Video, Audio Inputs |
| 🛠️ **Tool-Agnostic** | MCP Servers, LangChain, Hub Spaces als Tools |

---

### 📄 Citing smolagents

If you use smolagents in your publication, please cite it:

```bibtex
@Misc{smolagents,
  title =        {`smolagents`: a smol library to build great agentic systems.},
  author =       {Aymeric Roucher and Albert Villanova del Moral and Thomas Wolf 
                  and Leandro von Werra and Erik Kaunismäki},
  howpublished = {\url{https://github.com/huggingface/smolagents}},
  year =         {2025}
}
```

---

### 🔗 Additional Resources

- **Official Docs**: [huggingface.co/docs/smolagents](https://huggingface.co/docs/smolagents)
- **GitHub Repo**: [github.com/huggingface/smolagents](https://github.com/huggingface/smolagents)
- **Community**: [Hugging Face Forums](https://discuss.huggingface.co/)
- **Tutorials**: [Vision Agent Tutorial](https://huggingface.co/docs/smolagents/tutorials/vision)

---

## 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) for details.

```
MIT License

Copyright (c) 2026 YOUR_NAME

Permission is hereby granted, free of charge...
```

---

## 📧 Contact

**Creator**: Your Name  
**GitHub**: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)  
**E-Mail**: your.email@example.com  
**Hugging Face**: [@YOUR_HF_USERNAME](https://huggingface.co/YOUR_HF_USERNAME)

---

## 🌟 Acknowledgments

- **[Hugging Face](https://huggingface.co)** - For smolagents and Inference API
- **[Qwen Team](https://huggingface.co/Qwen)** - For the Qwen2.5-Coder Model
- **[Streamlit](https://streamlit.io)** - For the fantastic UI framework
- **[OpenWeatherMap](https://openweathermap.org)** - For weather data API

---

## 🔗 Useful Links

- [smolagents Dokumentation](https://huggingface.co/docs/smolagents)
- [Qwen2.5-Coder Model](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)
- [Streamlit Docs](https://docs.streamlit.io)
- [OpenWeatherMap API](https://openweathermap.org/api)

---

## 📊 Project Status

![Status](https://img.shields.io/badge/Status-Active-success)
![Version](https://img.shields.io/badge/Version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)

**Last Updated**: January 2026

---

<div align="center">

### ⭐ If you like this project, give it a star on GitHub! ⭐

**Made with ❤️ and 🤖 by smolagents**

</div>

---

## 🎯 Roadmap

### Planned Features
- [ ] Multi-User-Support
- [ ] Conversation Memory (long-term)
- [ ] Export chat history
- [ ] Docker container for easy deployment
- [ ] Support for more languages
- [ ] Voice input integration
- [ ] Dark Mode for UI
- [ ] Custom Tool Marketplace

### In Arbeit
- [x] Basis-Agent-Implementierung
- [x] Custom Tools (7+)
- [x] Streamlit UI
- [x] Bildgenerierung
- [x] Web-Suche
- [x] Wetter-Integration

---

## 📈 Statistiken

```
Total Lines of Code: ~800
Number of Tools: 13
Custom Tools: 7
API Integrations: 3
UI Framework: Streamlit
Agent Framework: smolagents
```

---

<div align="center">

**🚀 Good luck with your SmolAgents AI Assistant! 🚀**

</div>
