# 🤖 SmolAgents AI Assistant

<div align="center">

![SmolAgents Logo](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/smolagents/smolagents.png)

[![Deploy](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://smolagents-ai-assistant.streamlit.app/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions)](https://github.com/muk0644/smolagents-ai-assistant/actions)
[![Build Status](https://img.shields.io/github/actions/workflow/status/muk0644/smolagents-ai-assistant/ci-cd.yml?branch=feature/cicd-workflow&style=for-the-badge&logo=github)](https://github.com/muk0644/smolagents-ai-assistant/actions)
[![Python](https://img.shields.io/badge/Python-3.10-green?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)](https://smolagents-ai-assistant.streamlit.app/)
[![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow?style=for-the-badge)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)
[![Code Quality](https://img.shields.io/badge/Code_Quality-Flake8-blue?style=for-the-badge)](https://github.com/PyCQA/flake8)
[![Security](https://img.shields.io/badge/Security-Bandit-red?style=for-the-badge)](https://github.com/PyCQA/bandit)

**An intelligent AI agent with advanced features for web search, weather queries, image generation and more!**

🌐 **[Try the Live Demo](https://smolagents-ai-assistant.streamlit.app/)**

[Demo](#-demo) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-architecture) • [Tools](#-tools)

</div>

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [CI/CD Pipeline](#-cicd-pipeline)
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
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 About the Project

This project is a **fully functional AI agent** built with the **smolagents** library from Hugging Face. The agent uses the powerful **Qwen2.5-Coder-32B-Instruct** model and provides a user-friendly **Streamlit** interface.

### 🚀 Live Deployment
The application is **now deployed and live** on Streamlit Cloud:  
👉 **[smolagents-ai-assistant.streamlit.app](https://smolagents-ai-assistant.streamlit.app/)** 👈

The agent can:
- 🌐 **Perform web research** (DuckDuckGo, Google)
- 🌤️ **Retrieve real-time weather data**
- 🎨 **Generate images** (Text-to-Image)
- 🧮 **Execute Python code** for mathematical calculations
- 🎉 **Generate party plans** and event ideas
- 📊 **Retrieve Hugging Face Hub statistics**
- ⏰ **Provide timezone information**

---
🔄 CI/CD Pipeline

This project implements a **comprehensive CI/CD pipeline** using **GitHub Actions** to ensure code quality, security, and deployment readiness.

### 🚀 Pipeline Overview

The CI/CD workflow (`.github/workflows/ci-cd.yml`) automatically runs on every push or pull request to the `feature/cicd-workflow` branch, executing the following stages:

#### **1. Environment Setup**
- **Platform:** Ubuntu Latest
- **Python Version:** 3.10
- **Dependency Caching:** Pip dependencies cached (165MB) for faster builds

#### **2. Code Quality Checks**
```yaml
Linting with Flake8:
✅ Zero critical errors (E9, F63, F7, F82)
⚠️  133 style warnings (allowed: complexity, line length)
📊 Result: PASSED
```

**What Flake8 Checks:**
- Syntax errors and undefined names (build-blocking)
- Code complexity and line length (warnings only)
- Unused imports and variables
- PEP 8 style compliance

#### **3. Security Scans**
```yaml
Bandit Security Analysis:
✅ 615 lines of code scanned
✅ 0 vulnerabilities detected
🔒 Security Level: High confidence

Safety Dependency Check:
✅ 108 packages verified
⚠️  1 non-critical warning (continued)
📦 Dependencies: Secure
```

**Security Features:**
- **Bandit:** Scans for common security issues (SQL injection, hardcoded passwords, etc.)
- **Safety:** Checks for known vulnerabilities in dependencies
- **Secret Validation:** Ensures all API keys are properly configured

#### **4. Environment Validation**
```yaml
Required Secrets Verified:
✅ HF_TOKEN (38 characters) - Hugging Face authentication
✅ SERPAPI_API_KEY - Google Search integration
✅ OPENWEATHERMAP_API_KEY - Weather data access
```

#### **5. Project Structure Verification**
```yaml
Required Files Checked:
✅ app.py - Streamlit frontend
✅ agent.py - AI agent configuration
✅ tools.py - Custom tool implementations
✅ requirements.txt - Python dependencies
✅ README.md - Project documentation
```

#### **6. Python Syntax Validation**
- Import verification without execution
- AST parsing for syntax correctness
- Ensures all Python files are valid

### 📊 Build Metrics

| Metric | Value |
|--------|-------|
| **Build Time** | 45 seconds |
| **Dependencies Installed** | 108 packages |
| **Cache Size** | 165 MB |
| **Code Lines Scanned** | 615 lines |
| **Security Issues** | 0 critical |
| **Linting Errors** | 0 critical |

### 🎯 Workflow Trigger Conditions

The pipeline runs automatically on:
- ✅ Push to `feature/cicd-workflow` branch
- ✅ Pull requests to `feature/cicd-workflow` branch

### 📁 CI/CD Configuration File

Location: `.github/workflows/ci-cd.yml`

**Key Components:**
```yaml
name: CI/CD Pipeline for SmolAgents AI Assistant

on:
  push:
    branches: [ feature/cicd-workflow ]
  pull_request:
    branches: [ feature/cicd-workflow ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - Checkout code
      - Setup Python 3.10
      - Cache pip dependencies
      - Install requirements.txt
      - Install dev tools (flake8, bandit, safety)
      - Lint with flake8
      - Security scan with bandit
      - Check dependencies with safety
      - Validate environment secrets
      - Verify project structure
      - Validate Python syntax
      - Deployment readiness confirmation
```

### 🔐 Setting Up GitHub Secrets

To use the CI/CD pipeline, configure these secrets in your GitHub repository:

1. Navigate to **Settings → Secrets and variables → Actions**
2. Add the following secrets:

| Secret Name | Description | Required |
|------------|-------------|----------|
| `HF_TOKEN` | Hugging Face API token for model access | ✅ Yes |
| `SERPAPI_API_KEY` | SerpAPI key for Google search integration | ✅ Yes |
| `OPENWEATHERMAP_API_KEY` | OpenWeatherMap API key for weather data | ✅ Yes |

### ✅ Deployment Readiness

Upon successful pipeline completion, you'll see:
```
🎉 BUILD SUCCESSFUL!
✅ All linting checks passed
✅ Security scans completed
✅ Dependencies verified
✅ Environment secrets validated
✅ Project structure confirmed
🚀 The application is verified and ready for Streamlit Cloud deployment!
```

### 📈 Continuous Improvement

The CI/CD pipeline helps maintain:
- **Code Quality:** Consistent coding standards
- **Security:** Early detection of vulnerabilities
- **Reliability:** Automated testing before deployment
- **Speed:** Cached dependencies for faster builds
- **Confidence:** Verified deployment readiness

---

## 
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
| **Framework** | smolagents | Agent Orchestration |
| **Frontend** | Streamlit | Web UI |
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
- Clear, descriptive names
- Type Hints for all parameters
- Detailed docstrings with Args section

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
