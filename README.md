---
title: SmolAgents AI Assistant
emoji: 🚀
colorFrom: red
colorTo: blue
sdk: docker
app_port: 8501
tags:
  - streamlit
  - ai-agent
  - smolagents
  - huggingface
pinned: false
short_description: A smart AI Assistant built with SmolAgents and Streamlit
license: mit
---

# 🤖 SmolAgents AI Assistant

<div align="center">

![SmolAgents Logo](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/smolagents/smolagents.png)

[![Deploy](https://img.shields.io/badge/🚀_Live_Demo-HF_Spaces-FF4B4B?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/muk0644/smolagents-ai-assistant)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions)](https://github.com/muk0644/smolagents-ai-assistant/actions)
[![Build Status](https://img.shields.io/github/actions/workflow/status/muk0644/smolagents-ai-assistant/ci-cd.yml?branch=feature/cicd-workflow&style=for-the-badge&logo=github)](https://github.com/muk0644/smolagents-ai-assistant/actions)
[![Python](https://img.shields.io/badge/Python-3.10-green?style=for-the-badge&logo=python)](https://www.python.org/)
[![HF Spaces](https://img.shields.io/badge/HF_Spaces-Docker-FF4B4B?style=for-the-badge&logo=huggingface)](https://huggingface.co/spaces/muk0644/smolagents-ai-assistant)
[![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow?style=for-the-badge)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)
[![Code Quality](https://img.shields.io/badge/Code_Quality-Flake8-blue?style=for-the-badge)](https://github.com/PyCQA/flake8)
[![Security](https://img.shields.io/badge/Security-Bandit-red?style=for-the-badge)](https://github.com/PyCQA/bandit)

**An intelligent AI agent with advanced features for web search, weather queries, image generation and more!**

🌐 **[Try the Live Demo](https://huggingface.co/spaces/muk0644/smolagents-ai-assistant)**

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
👉 **[smolagents-ai-agent.streamlit.app](https://smolagents-ai-agent.streamlit.app/)** 👈

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
- Ephemeral file system (images converted to base64)
- High-resolution output with download buttons
- Stored in session history as base64 strings

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
├── app.py                  # Streamlit Frontend (Multi-session UI)
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
├── user_data/            # Per-user JSON session storage
│   └── user_example_com.json  # Email-based session files
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml     # GitHub Actions CI/CD pipeline
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
- Ephemeral storage (converted to base64)
- Displayed in chat with download button

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

### `app.py` - Streamlit Frontend (Production-Ready UI)

**Overview:**  
`app.py` is the complete Streamlit application deployed on [Streamlit Cloud](https://smolagents-ai-agent.streamlit.app/) featuring a production-grade multi-session chat interfac UI

#### 🎨 **UI Architecture**

**1. Authentication System (Email-Based)**
```python
# Centered login screen with professional styling
- Email validation (requires '@' symbol)
- Session persistence across page reloads
- Clean, minimalist design with centered layout
```

**2. Ultra-Compact Sidebar (ChatGPT/Gemini Style)**
```css
/* Custom CSS injection for professional appearance */
- Gap: 0.25rem between elements
- Padding: 0.4-0.5rem for compact spacing
- Font sizes: 0.75-0.85rem for dense information
- Hover effects on image thumbnails (80px height)
```

**Sidebar Components:**
- ✅ **User Status**: Display logged-in email (0.8rem, subtle)
- 🔢 **Global Tool Counter**: `{usage}/{MAX_TOOL_LIMIT}` with color indicator
- ⏰ **Timer**: Minutes remaining until auto-reset
- ➕ **New Chat Button**: Primary action (full width)
- 🖼️ **Your Contents Gallery**: Latest 3 generated images as thumbnails
- 📚 **Chats History**: Session list with active indicator (● vs ○)
- 🗑️ **Reset Button**: Clear all sessions and counters
- 🚪 **Logout Button**: Return to login screen

**3. Multi-Session Management**
```python
# Per-user JSON storage in user_data/
User Data Schema:
{
  "global_tool_usage": 3,            # Shared across all sessions
  "last_reset_time": "ISO timestamp",
  "sessions": [                       # Max 5 sessions (auto-rotation)
    {
      "session_id": "millisecond_timestamp",
      "title": "Weather in Berlin",   # Auto-generated from first message
      "messages": [...]                # Full chat history
    }
  ]
}
```

**4. Ephemeral Image System**
```python
# Security-first image handling
Flow:
1. Agent generates image → local file created
2. Read image file into memory (bytes)
3. DELETE file immediately (ephemeral)
4. Convert to base64 string
5. Store base64 in JSON (portable, persistent)
6. Display with download button

Benefits:
- Zero disk usage (no folder accumulation)
- Portable JSON files
- Secure (no file path leakage)
```

**5. Global Tool Quota System**
```python
# Cross-session tool limiting
MAX_TOOL_LIMIT = 10
RESET_INTERVAL_MINUTES = 60

Logic:
- Tracks tool usage GLOBALLY per email (not per session)
- Auto-resets after 60 minutes
- Robust detection via agent.memory.steps inspection
- Visual warnings when limit reached
```

**6. Professional Chat Interface**
```python
Features:
- Custom avatars: Agent (Hugging Face logo) + User (👤)
- Message history rendering with role-based styling
- Spinner with "Thinking..." during agent execution
- Error handling with user-friendly messages
- Auto-scroll to latest message
- Download buttons for generated images
```

#### 🚀 **Deployment Features**

**Streamlit Cloud Integration:**
- Environment variables via Streamlit secrets (`st.secrets`)
- `HF_TOKEN` required for Hugging Face model access
- `SERPAPI_API_KEY` for Google search integration
- `OPENWEATHERMAP_API_KEY` for weather data

**Production Optimizations:**
- Session state persistence with `@st.cache_resource`
- Agent instance caching for performance
- JSON-based storage for serverless compatibility
- Automatic UI updates with `st.rerun()`

#### 🎯 **Key Implementation Highlights**

**Tool Detection Algorithm:**
```python
def did_agent_use_tools(agent) -> bool:
    """Scans agent.memory.steps in REVERSE to detect tool usage"""
    # Inspects actual execution log (not keywords)
    # Excludes 'final_answer' (not a tool)
    # Returns True only if real tools were invoked
```

**Time-Based Auto-Reset:**
```python
# Automatic quota reset after 60 minutes
elapsed_time = datetime.now() - st.session_state.last_reset_time
if elapsed_minutes >= RESET_INTERVAL_MINUTES:
    reset_global_counter_and_save()
```

**Session Rotation:**
```python
# Keeps only latest 5 sessions per user
if len(all_sessions) > MAX_SESSIONS_PER_USER:
    all_sessions.pop(0)  # Remove oldest
```

#### 📊 **Technical Stack**
- **Frontend Framework**: Streamlit 1.53.0
- **Styling**: Custom CSS with `unsafe_allow_html=True`
- **Storage**: JSON files (`user_data/` directory)
- **Authentication**: Email-based (no external auth service)
- **Deployment**: Streamlit Cloud (serverless)

#### 🔐 **Security Features**
- No hardcoded secrets (uses `.env` locally, Streamlit secrets in cloud)
- Ephemeral image handling (no persistent files)
- Input validation on email field
- Proper error handling and user feedback

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
→ Converts: Image to base64 (ephemeral file deleted)
→ Displays: Image in chat with download button
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

## � Deployment & Workflow Guide

### 📋 Overview: Complete Deployment Pipeline

This project supports **two deployment scenarios**:

1. **Manual: Local → HF Spaces** (for testing/development)
2. **Automated: GitHub → HF Spaces via CI/CD** (recommended for production)

---

### **Scenario 1: Manual Deployment (Local to HF Spaces)**

#### **When to use:**
- Quick testing of changes
- Development/debugging locally
- Before pushing to GitHub

#### **Step-by-Step Process:**

```bash
# Step 1: Make code changes locally
# Edit any file (e.g., app.py, tools.py, requirements.txt)

# Step 2: Test locally
streamlit run app.py

# Step 3: Commit to your feature branch
git checkout feature/hugging-face-spaces
git add .
git commit -m "Your meaningful commit message"

# Step 4: Push to HF Spaces hub
git push https://muk0644:YOUR_REPO_PUSH_TOKEN@huggingface.co/spaces/muk0644/smolagents-ai-assistant feature/hugging-face-spaces:main
```

#### **Authentication (HF Spaces):**

**Token Type:** `repo_push` token (write-enabled)

```bash
# Get your token from:
# https://huggingface.co/settings/tokens
# Create token with "repo" scope for write access
```

**Security Best Practices:**
- ✅ Store token in `.env` file locally (protected by `.gitignore`)
- ✅ Never commit token to git
- ✅ Use environment variable in scripts: `$REPO_PUSH_TOKEN`
- ❌ Never paste token in commit messages or comments

#### **What Happens After Push:**

1. **Code reaches HF Spaces repo** (main branch)
2. **Docker Container builds** (using your Dockerfile)
   - Pulls Python 3.10-slim base image
   - Installs system dependencies (build-essential)
   - Installs Python packages from requirements.txt
   - Copies your code (app.py, agent.py, tools.py)
3. **Streamlit server starts** on port 8501
4. **Your app is live!** 
   - URL: `https://huggingface.co/spaces/muk0644/smolagents-ai-assistant`
   - Takes ~2-5 minutes from push to live

---

### **Scenario 2: Automated Deployment (GitHub → HF Spaces via CI/CD)**

#### **When to use:**
- Production deployments
- Automated testing before deployment
- Synchronized GitHub and HF Spaces
- Team collaboration

#### **Complete Workflow:**

```
┌─────────────────────────────────────────────────────────────┐
│ YOU: Edit code locally (app.py, tools.py, etc.)            │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ YOU: git push origin feature/hugging-face-spaces            │
│ (Push to GitHub - NOT to HF Spaces)                         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ GITHUB ACTIONS: CI/CD Pipeline Triggers                    │
│ ✅ Checkout code                                             │
│ ✅ Setup Python 3.10                                         │
│ ✅ Lint with flake8 (code quality)                          │
│ ✅ Security scan with bandit                                │
│ ✅ Check dependencies (safety)                              │
│ ✅ Validate secrets/environment                             │
│ ✅ Verify Python syntax                                     │
└────────────────────────┬────────────────────────────────────┘
                         │
                ┌────────┴────────┐
                │                 │
             ✅ PASS          ❌ FAIL
                │                 │
                ▼                 ▼
        ┌──────────────┐   ┌──────────────┐
        │ CICD SUCCESS │   │ BUILD FAILED │
        └──────┬───────┘   └──────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────────────┐
│ GITHUB ACTIONS: Deploy to HF Spaces                        │
│ (Automatic - NO additional push needed!)                   │
│                                                             │
│ Command executed by GitHub Actions:                        │
│ git push https://USER:HF_REPO_TOKEN@huggingface.co/...     │
│                                                             │
│ ✅ Your code automatically syncs to HF Spaces main branch  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ HF SPACES: Docker Build & Deployment                       │
│ ✅ Docker container builds (2-5 minutes)                    │
│ ✅ Python packages installed                                │
│ ✅ Your app is LIVE! 🚀                                     │
└─────────────────────────────────────────────────────────────┘
```

#### **Step-by-Step Process:**

```bash
# Step 1: Make code changes
# Edit any file (app.py, tools.py, requirements.txt, etc.)

# Step 2: Test locally (optional but recommended)
streamlit run app.py

# Step 3: Commit to feature branch
git add .
git commit -m "Add new feature: weather alerts"

# Step 4: Push to GITHUB (NOT HF Spaces!)
git push origin feature/hugging-face-spaces

# Step 5: Wait for GitHub Actions to complete
# Check status at: https://github.com/muk0644/smolagents-ai-assistant/actions

# Step 6: GitHub Actions automatically updates HF Spaces
# NO additional push needed!

# Step 7: Check deployment
# Open: https://huggingface.co/spaces/muk0644/smolagents-ai-assistant
```

#### **How CI/CD Triggers HF Spaces Deployment:**

```yaml
# This is configured in .github/workflows/ci-cd.yml
# The workflow includes a deployment step that runs:

- name: Deploy to Hugging Face Spaces
  if: success()  # Only if all checks pass
  run: |
    git push https://muk0644:${{ secrets.HF_REPO_PUSH_TOKEN }}@huggingface.co/spaces/muk0644/smolagents-ai-assistant feature/hugging-face-spaces:main
```

---

### **Container Build Process (HF Spaces)**

#### **What happens when you push:**

1. **Docker reads your Dockerfile**
   ```dockerfile
   FROM python:3.10-slim
   WORKDIR /app
   RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY . .
   EXPOSE 8501
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build stages:**
   - ✅ **Stage 1:** Pull Python 3.10-slim image (300MB base)
   - ✅ **Stage 2:** Install system packages (build tools)
   - ✅ **Stage 3:** Copy requirements.txt
   - ✅ **Stage 4:** Install Python packages (smolagents, streamlit, etc.)
   - ✅ **Stage 5:** Copy your code
   - ✅ **Stage 6:** Expose port 8501
   - ✅ **Stage 7:** Start Streamlit server

3. **Container runtime:**
   - App runs as Docker container
   - Streamlit server listens on 0.0.0.0:8501
   - HF Spaces proxy routes traffic to your container
   - App is accessible via HTTPS

#### **Build Time:**
- **First build:** 3-5 minutes
- **Subsequent builds:** 1-2 minutes (cached layers)

#### **Environment Variables:**
HF Spaces automatically provides:
- `STREAMLIT_SERVER_PORT=8501`
- Your custom secrets (HF_TOKEN, SERPAPI_API_KEY, etc.)

---

### **Token Requirements & Security**

| Token | Purpose | Scope | Required |
|-------|---------|-------|----------|
| `HF_TOKEN` | Hugging Face API access (models, inference) | Read | ✅ Yes |
| `REPO_PUSH_TOKEN` | Write access to HF Spaces repo | Write | ✅ Yes (for deployment) |
| `SERPAPI_API_KEY` | Google Search integration | Search | ⚠️ Optional |
| `OPENWEATHERMAP_API_KEY` | Weather data | Weather | ⚠️ Optional |

#### **Setting up GitHub Actions Secrets:**

```bash
# For automated CI/CD → HF Spaces deployment:
# 1. Go to GitHub repo Settings → Secrets and variables → Actions
# 2. Add these secrets:
#    - HF_REPO_PUSH_TOKEN = your_repo_push_token
#    - HF_TOKEN = your_huggingface_token
#    - SERPAPI_API_KEY = your_serpapi_key
#    - OPENWEATHERMAP_API_KEY = your_weather_key
```

---

### **Troubleshooting Deployment**

#### **Container won't start:**
```bash
# Check Dockerfile syntax
docker build -t test-image .

# Check requirements.txt for conflicts
pip install -r requirements.txt

# Review logs at HF Spaces
# https://huggingface.co/spaces/muk0644/smolagents-ai-assistant/logs
```

#### **Push fails with authentication error:**
```bash
# Verify token is correct
# Ensure token has "write" scope (repo_push)
# Check token hasn't expired

# Test authentication
git clone https://muk0644:YOUR_TOKEN@huggingface.co/spaces/muk0644/smolagents-ai-assistant test-repo
```

#### **CI/CD pipeline fails:**
```bash
# Check GitHub Actions logs
# https://github.com/muk0644/smolagents-ai-assistant/actions

# Common issues:
# - Linting errors (flake8)
# - Security issues (bandit)
# - Missing dependencies
# - Invalid Python syntax
```

---

## �🐛 Troubleshooting

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
# Check HF_TOKEN in .env
echo $HF_TOKEN

# Verify text-to-image tool is loaded
# Check agent.py for load_tool("agents-course/text-to-image")

# Ensure sufficient disk space (for temporary files)
df -h
```
