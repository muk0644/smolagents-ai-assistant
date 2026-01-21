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
- [Deployment & Workflow Guide](#-deployment--workflow-guide)
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

### Hugging Face Tokens

#### **HF_TOKEN** (Read Access)
1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Create a new Access Token with **Read** permission
3. Copy the token to the `.env` file
```env
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxx
```

#### **HF_REPO_PUSH_TOKEN** (Write Access - for Deployment)
1. Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
2. Create a **NEW** Access Token with **`repo_push`** permission (write-enabled)
3. Store in **TWO** places:
   - **Local `.env` file** for manual deployment:
   ```env
   HF_REPO_PUSH_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxx
   ```
   - **GitHub Secret** for automated CI/CD (Step 14):
     - Go to: GitHub Repo → Settings → Secrets and variables → Actions
     - Name: `HF_REPO_PUSH_TOKEN`
     - Value: Your HF write token

**Why two separate tokens?**
- Follows security best practices (principle of least privilege)
- Read token accesses Hub only
- Write token can modify HF Spaces repository
- Keeps permissions compartmentalized

### OpenWeatherMap API Key
1. Register at [OpenWeatherMap](https://openweathermap.org/api)
2. Generate a free API key
3. Add it to the `.env` file
```env
OPENWEATHERMAP_API_KEY=xxxxxxxxxxxxxxxxxxxxx
```

### SerpAPI Key (Optional)
1. Register at [SerpAPI](https://serpapi.com/)
2. Get your API key
3. Add it to the `.env` file
```env
SERPAPI_API_KEY=xxxxxxxxxxxxxxxxxxxxx
```

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

#### 2. HF_REPO_PUSH_TOKEN (REQUIRED for Automated Deployment)
```env
HF_REPO_PUSH_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxx
```
**How to obtain:**
- Register at [Hugging Face](https://huggingface.co)
- Go to Settings → Access Tokens
- Create a **NEW** token with `repo_push` permission (write-enabled)
- This token is different from HF_TOKEN - it has **write permissions**

**Where it's used:**
- 🚀 **GitHub Actions Secret:** Used by Step 14 to deploy to HF Spaces
- 📝 **Local Manual Deployment:** Use for manual `git push` to HF Spaces
- ✅ Must have "repo_push" scope enabled

**Why separate tokens?**
- **HF_TOKEN** (read-only): For reading models, datasets, accessing Hub
- **HF_REPO_PUSH_TOKEN** (write): For pushing code to HF Spaces repository
- **Security:** Follows principle of least privilege - each token has specific permissions

#### 3. OpenWeatherMap API Key (REQUIRED for weather)
```env
OPENWEATHERMAP_API_KEY=xxxxxxxxxxxxxxxxxxxxx
```
**How to obtain:**
- Register at [OpenWeatherMap](https://openweathermap.org)
- Go to API Keys
- Free plan: 1,000 calls/day

#### 4. SerpAPI Key (OPTIONAL for Google Search)
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
# Token name: HF_REPO_PUSH_TOKEN (for consistency)
```

**Token Storage & Security:**
- 🔐 **GitHub Secret:** Stored as `HF_REPO_PUSH_TOKEN` in GitHub Actions (for Step 14)
- 📝 **Local Development:** Store token in `.env` file locally (protected by `.gitignore`)
- ✅ Use environment variable in scripts: `$HF_REPO_PUSH_TOKEN`
- ❌ Never commit token to git
- ❌ Never paste token in commit messages or comments

**Why This Token is Important:**
- This is a **Hugging Face Hub write token** with `repo_push` permissions
- Allows automated deployment to HF Spaces without manual intervention
- GitHub Actions (Step 14) uses this token via `${{ secrets.HF_REPO_PUSH_TOKEN }}`
- Essential for automated CI/CD pipeline to work

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
# 🚀 Deployment & Workflow Guide

## Overview
This section explains how the SmolAgents AI Assistant is deployed to **Hugging Face Spaces** with **automated CI/CD**. The application automatically deploys when code changes are pushed to the `feature/hugging-face-spaces` branch.

## Deployment Architecture

```
Local Development
        ↓ (git push)
GitHub Repository (feature/hugging-face-spaces)
        ↓ (GitHub Actions CI/CD Pipeline)
13 Automated Checks (Lint, Security, Syntax, Docker Build, etc.)
        ↓ (if all checks pass)
Step 14: Automatic Deployment to HF Spaces
        ↓
HF Spaces Repository (https://huggingface.co/spaces/muk0644/smolagents-ai-assistant)
        ↓ (auto-detected)
Docker Container Rebuild & Restart
        ↓
Live Application Available
```

## How It Works: Step-by-Step

### **1. Local Development**
You develop and commit code locally:
```bash
# Make changes to your code
git add .
git commit -m "Add new feature"
git push origin feature/hugging-face-spaces
```

### **2. GitHub Actions Triggers**
When code reaches GitHub, GitHub Actions automatically:
- ✅ **Step 1:** Set up Python 3.10 environment
- ✅ **Step 2:** Run Flake8 linting (code quality)
- ✅ **Step 3:** Run Bandit security scan
- ✅ **Step 4:** Check for hardcoded secrets
- ✅ **Step 5:** Validate project structure
- ✅ **Step 6:** Check Python syntax
- ✅ **Step 7:** Build Docker image (test)
- ✅ **Steps 8-13:** Additional validation checks
- 🚀 **Step 14:** Deploy to HF Spaces (if all checks pass)

### **3. Step 14: Automatic HF Spaces Deployment**

**What Step 14 Does:**
```yaml
- name: 🚀 Deploy to Hugging Face Spaces
  if: github.ref == 'refs/heads/feature/hugging-face-spaces' && success()
  env:
    HF_REPO_TOKEN: ${{ secrets.HF_REPO_PUSH_TOKEN }}
  run: |
    git config user.email "github-actions[bot]@users.noreply.github.com"
    git config user.name "GitHub Actions"
    git remote add hf-spaces https://muk0644:${HF_REPO_TOKEN}@huggingface.co/spaces/muk0644/smolagents-ai-assistant.git || true
    git fetch hf-spaces main || true
    git push hf-spaces HEAD:main
```

**Step 14 Breakdown:**

| Component | Purpose |
|-----------|---------|
| `if: github.ref == 'refs/heads/feature/hugging-face-spaces' && success()` | Only runs on `feature/hugging-face-spaces` branch AND only if all CI/CD checks pass |
| `HF_REPO_TOKEN` | GitHub secret containing your HF write token for authentication |
| `git config user.email` | Sets bot email for commit attribution |
| `git config user.name` | Sets bot username for commit attribution |
| `git remote add hf-spaces` | Adds HF Spaces repo as a remote (with `\|\| true` to avoid errors if already added) |
| `git fetch hf-spaces main` | Fetches latest commits from HF Spaces (with `\|\| true` to allow first deploy) |
| `git push hf-spaces HEAD:main` | **THE KEY STEP:** Pushes exact same commit to HF Spaces' main branch |

### **4. HF Spaces Auto-Detects Update**
When Step 14 pushes the commit:
- 🔔 HF Spaces detects new commit on `main` branch
- 📦 HF Spaces reads the `README.md` metadata (SDK type, port, etc.)
- 🐳 HF Spaces triggers automatic Docker container rebuild
- ✅ New container deployed with your latest code

### **5. Application Goes Live**
Your app is instantly available at:
```
https://huggingface.co/spaces/muk0644/smolagents-ai-assistant
```

## 🎯 The One Key Fact About Step 14

**The same commit that's on GitHub is copied to HF Spaces:**
- ✅ Identical commit hash (e.g., `a6b6e72`)
- ✅ Same code, same metadata
- ✅ No modifications or rebuilding of code
- ✅ HF Spaces simply restarts the container with new code

**Visual Flow:**
```
GitHub Commit: a6b6e72 (Your Code)
         ↓ (Step 14 copies)
HF Spaces Commit: a6b6e72 (Exact Same)
         ↓ (HF Spaces auto-detects)
Docker Rebuild with New Code
         ↓
App Restarted & Live
```

## 📋 Complete Deployment Workflow

### **Scenario 1: Manual Deployment (Original Method - No Longer Needed)**

Before Step 14, manual deployment required:
```bash
# 1. Develop locally
git add .
git commit -m "new feature"

# 2. Push to GitHub
git push origin feature/hugging-face-spaces

# 3. Manually push to HF Spaces (annoying!)
git push https://muk0644:HF_TOKEN@huggingface.co/spaces/muk0644/smolagents-ai-assistant feature/hugging-face-spaces:main

# 4. Wait for HF Spaces rebuild
```

**❌ Problem:** Required manual HF Spaces push every time  
**❌ Problem:** Easy to forget  
**❌ Problem:** Manual token management  

### **Scenario 2: Automated Deployment (Current - Recommended)**

With Step 14, deployment is automatic:
```bash
# 1. Develop locally
git add .
git commit -m "new feature"

# 2. Push to GitHub (that's it!)
git push origin feature/hugging-face-spaces

# 3. GitHub Actions automatically:
#    - Runs all CI/CD checks
#    - If checks pass: Step 14 copies to HF Spaces
#    - HF Spaces automatically restarts container
#    - App is live
```

**✅ Advantage:** One command: `git push`  
**✅ Advantage:** Fully automated, no manual steps  
**✅ Advantage:** Guaranteed code quality (checks first)  
**✅ Advantage:** Automatic failsafe (doesn't deploy if checks fail)  

## 🔐 Setting Up Automated Deployment

To enable Step 14 automation, you need one GitHub secret:

### **1. Create HF Write Token (on Hugging Face)**
```bash
# Go to: https://huggingface.co/settings/tokens
# Create new token with "write" permissions
# Example token: hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### **2. Add Secret to GitHub**
```bash
# Go to: GitHub Repo → Settings → Secrets and variables → Actions
# Create new secret:
# Name: HF_REPO_PUSH_TOKEN
# Value: hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### **3. That's It!**
Once the secret is added, Step 14 automatically runs on every push to `feature/hugging-face-spaces`.

## 📊 Complete GitHub Actions Pipeline (14 Steps)

| Step | Name | Purpose | Time |
|------|------|---------|------|
| 1 | Checkout Code | Get latest code from repo | <1s |
| 2 | Setup Python | Install Python 3.10 | ~5s |
| 3 | Cache Pip | Speed up installs | ~2s |
| 4 | Install Dependencies | pip install requirements | ~15s |
| 5 | Lint with Flake8 | Check code quality | ~3s |
| 6 | Security Scan (Bandit) | Check for vulnerabilities | ~4s |
| 7 | Check Secrets | Detect hardcoded secrets | ~2s |
| 8 | Validate Structure | Check project layout | ~1s |
| 9 | Syntax Check | Validate Python syntax | ~2s |
| 10 | Docker Build Test | Build container image | ~8s |
| 11 | Docker Image Analysis | Check image size/efficiency | ~2s |
| 12 | Dependency Audit | Verify dependency health | ~2s |
| 13 | Summary | Generate report | ~1s |
| 14 | Deploy to HF Spaces | **Push to HF Spaces** | ~3s |
| | **Total** | **Full pipeline** | **~45 seconds** |

## 🎬 Example Complete Workflow

Here's what happens when you push code:

```bash
# 1. Local: Make a change
echo "# New feature" >> README.md

# 2. Local: Commit
git add .
git commit -m "Add new feature"

# 3. Local: Push to GitHub (that's all you need to do!)
git push origin feature/hugging-face-spaces

# ⏳ GitHub Actions automatically:
# - ✅ Step 1-13: Run all CI/CD checks (45 seconds)
# - ✅ All checks pass
# - 🚀 Step 14: Push exact commit to HF Spaces
# - 🔔 HF Spaces detects new commit
# - 📦 HF Spaces rebuilds Docker container
# - ✨ Your app is live with changes!

# 4. User can immediately:
# - Visit: https://huggingface.co/spaces/muk0644/smolagents-ai-assistant
# - See: New feature deployed
# - Test: Updated functionality
```

## 🚨 If CI/CD Checks Fail

If any check fails, Step 14 **WILL NOT RUN**:
```bash
# Example: Flake8 detects syntax error in Step 5
# Result:
# - ❌ Pipeline stops
# - ❌ Step 14 does not execute
# - ❌ Code NOT deployed to HF Spaces
# - ✅ You get error message to fix

# Fix and push again
git add .
git commit -m "Fix syntax error"
git push origin feature/hugging-face-spaces
# Now Step 14 runs if all checks pass
```

## 📱 Monitoring Deployment

### **Check GitHub Actions Logs**
1. Go to: GitHub Repo → Actions
2. Select latest workflow run
3. Click on workflow name
4. View all 14 steps
5. Check Step 14 logs for HF Spaces push result

### **Check HF Spaces Update**
1. Go to: https://huggingface.co/spaces/muk0644/smolagents-ai-assistant
2. Look at "Files" section
3. Check commit history
4. See same commit hash as GitHub

### **Verify Deployment Success**
```bash
# 1. Check commit appears on HF Spaces
git log --oneline | head -1  # GitHub commit
# Output: a6b6e72 Add new feature

# 2. Check HF Spaces has same commit
cd ../hf-spaces-smolagents  # if cloned locally
git log --oneline | head -1
# Output: a6b6e72 Add new feature
```

## 🐛 Troubleshooting Deployment

### **Problem: Step 14 didn't run**
**Possible Causes:**
- ❌ Pushing to wrong branch (not `feature/hugging-face-spaces`)
- ❌ One of Steps 1-13 failed
- ❌ `HF_REPO_PUSH_TOKEN` secret not set

**Solution:**
```bash
# 1. Verify branch
git branch

# 2. Check GitHub Actions logs for errors
# Visit: GitHub Repo → Actions → Latest run

# 3. Verify secret exists
# GitHub → Settings → Secrets and variables → Actions → HF_REPO_PUSH_TOKEN
```

### **Problem: HF Spaces didn't update**
**Possible Causes:**
- ❌ Step 14 failed (check logs)
- ❌ HF_TOKEN doesn't have write permissions
- ❌ HF Spaces spaces URL changed

**Solution:**
```bash
# 1. Verify secret token is correct
# Test manual push (one time):
git push https://username:HF_TOKEN@huggingface.co/spaces/muk0644/smolagents-ai-assistant feature/hugging-face-spaces:main

# 2. Check token has write permissions
# Visit: https://huggingface.co/settings/tokens
```

### **Problem: Commit hash doesn't match on HF Spaces**
**Possible Causes:**
- ❌ Manual push interfered with Step 14
- ❌ HF Spaces force-pushed different commit
- ❌ Network issue during Step 14

**Solution:**
```bash
# 1. Sync local with both repos
git fetch origin
git fetch hf-spaces main

# 2. Verify latest commits match
git log origin/feature/hugging-face-spaces --oneline | head -1
git log hf-spaces/main --oneline | head -1

# 3. If different, manually sync
git push hf-spaces origin/feature/hugging-face-spaces:main
```

## 💡 Key Takeaways

1. **One Push, Everything Works:** `git push origin feature/hugging-face-spaces` triggers full pipeline
2. **Automatic Quality Control:** All checks run before deployment
3. **Same Commit Everywhere:** Git ensures identical code on GitHub and HF Spaces
4. **Zero Manual Steps:** Step 14 handles HF Spaces deployment automatically
5. **Instant Live:** Container restart happens immediately after commit
6. **Safety First:** Failed checks prevent broken code deployment

## 🔄 Git Workflow Summary

```bash
# Complete workflow for deploying new feature:

# 1. Create/checkout feature branch
git checkout -b feature/my-new-feature

# 2. Make changes
nano app.py

# 3. Commit locally
git add .
git commit -m "Add amazing feature"

# 4. Push to feature/hugging-face-spaces
git push origin feature/hugging-face-spaces

# 5. GitHub Actions runs (automatic):
#    - Runs 13 checks (syntax, security, etc.)
#    - If all pass → Step 14 deploys to HF Spaces
#    - HF Spaces auto-rebuilds
#    - App is live!

# 6. Verify deployment
#    - Check GitHub Actions logs
#    - Visit HF Spaces URL
#    - Test app functionality
```
