# 🤖 SmolAgents AI Assistant

<div align="center">

![SmolAgents Logo](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/smolagents/smolagents.png)

[![Deploy](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://smolagents-ai-assistant-up.streamlit.app/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions)](https://github.com/muk0644/smolagents-ai-assistant/actions)
[![Build Status](https://img.shields.io/github/actions/workflow/status/muk0644/smolagents-ai-assistant/ci-cd.yml?branch=feature/cicd-workflow&style=for-the-badge&logo=github)](https://github.com/muk0644/smolagents-ai-assistant/actions)
[![Python](https://img.shields.io/badge/Python-3.10-green?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)](https://smolagents-ai-assistant-up.streamlit.app/)
[![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow?style=for-the-badge)](https://huggingface.co/)
[![smolagents](https://img.shields.io/badge/smolagents-Agent_Framework-1f72be?style=for-the-badge)](https://github.com/huggingface/smolagents)
[![LangChain](https://img.shields.io/badge/LangChain-Integration-00a86b?style=for-the-badge)](https://www.langchain.com/)
[![RAG](https://img.shields.io/badge/RAG-BM25_Retrieval-ff6b6b?style=for-the-badge)](https://en.wikipedia.org/wiki/Okapi_BM25)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)
[![Code Quality](https://img.shields.io/badge/Code_Quality-Flake8-blue?style=for-the-badge)](https://github.com/PyCQA/flake8)
[![Security](https://img.shields.io/badge/Security-Bandit-red?style=for-the-badge)](https://github.com/PyCQA/bandit)

**An intelligent AI agent with advanced features for web search, weather queries, image generation and more!**

🌐 **[Try the Live Demo](https://smolagents-ai-assistant-up.streamlit.app/)**

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

This project is a **fully functional Agentic RAG (Retrieval Augmented Generation) system** combining **smolagents** orchestration with **LangChain** semantic search capabilities. It features **dual LLM models** via an easy-to-use dropdown selector and is deployed across **dual cloud platforms** with an enterprise-grade **LLMOps pipeline**.

**Core Technologies:**
- **Agent Framework**: smolagents (Hugging Face)
- **Retrieval Engine**: LangChain (SerpAPI + Custom Knowledge Base RAG)
- **Semantic Search**: BM25 algorithm with document chunking
- **LLM Models**: Qwen2.5-Coder-32B-Instruct + Gemini 2.5 Flash

**Supported Models:**
- **Qwen2.5-Coder-32B-Instruct** (HuggingFace - Free)
- **Gemini 2.5 Flash** (Google - Free with API key)

### 🚀 Dual Cloud Deployment

The application is deployed on two platforms, optimized for different use cases:

**1. Streamlit Cloud (Rapid Prototyping)**
- 👉 **[smolagents-ai-assistant-up.streamlit.app](https://smolagents-ai-assistant-up.streamlit.app/)** 
- Branch: `cicd-workflow2`
- Quick iteration and real-time updates

**2. HuggingFace Spaces (Production MLOps)**
- Docker containerized deployment
- Branch: `feature/hugging-face-spaces`
- Automated CI/CD pipeline with GitHub Actions
- Continuous testing, validation, and real-time deployment

The agent can:
- 🌐 **Perform web research** (DuckDuckGo, Google, LangChain SerpAPI)
- 📚 **Query knowledge base** (Semantic search with RAG retrieval)
- 🌤️ **Retrieve real-time weather data**
- 🎨 **Generate images** (Text-to-Image)
- 🧮 **Execute Python code** for mathematical calculations
- 🎉 **Generate party plans** (Specialized party planning with retrieved ideas)
- 📊 **Retrieve Hugging Face Hub statistics**
- ⏰ **Provide timezone information**

---

## 🔄 LLMOps & CI/CD Pipeline

This project implements a **comprehensive LLMOps pipeline** using **GitHub Actions** to ensure code quality, security, testing, and automated deployment of LLM-powered applications.

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
✅ retrieval.py - RAG/Retrieval module (Party Planning KB)
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
├── retrieval.py           # RAG/Retrieval module (Party Planning KB)
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

## 🤖 Agentic RAG Architecture

This project implements an **advanced Retrieval Augmented Generation (RAG)** system that enhances LLM reasoning with dynamic information retrieval:

### RAG Components:

**1. Retrieval Layer** (Multiple Sources)
- **Web Search**: DuckDuckGo, Google, LangChain SerpAPI
- **Knowledge Base**: Semantic search via BM25 algorithm
- **Webpage Content**: VisitWebpageTool for detailed information extraction

**2. Augmentation Layer** (Context Enhancement)
- Retrieved documents automatically injected into LLM context
- Agent synthesizes retrieved information with reasoning
- Multi-step retrieval for complex queries

**3. Generation Layer** (LLM Response)
- Qwen2.5-Coder or Gemini 2.5 Flash generates answer
- Uses retrieved context for factual accuracy
- Maintains conversation history for coherence

### Benefits:
✅ **Accurate Responses**: Grounded in actual data
✅ **Current Information**: Web search for latest trends
✅ **Specialized Knowledge**: Custom knowledge base for domain expertise
✅ **Flexible Sources**: Can combine multiple retrieval methods
✅ **Verifiable**: Responses traceable to source documents

---

## 📚 Knowledge Retrieval System: Two Types of RAG Tools

This project features **two complementary RAG approaches** for different use cases:

### **Type 1: Static Knowledge Base (PartyPlanningRetrieverTool)**

**Purpose**: Fast, offline access to curated domain knowledge

- **Source**: Built-in JSON data embedded in `retrieval.py`
- **Data**: 10 curated party planning ideas for superhero-themed events
- **Algorithm**: BM25 (probabilistic relevance ranking)
- **Retrieval**: Top 5 most relevant suggestions
- **Use Case**: Party planning queries, entertainment ideas, catering suggestions
- **Advantages**: 
  - ⚡ No internet required
  - 🔐 No external API dependencies
  - 🚀 Instant retrieval
  - 📦 Self-contained knowledge base

**Example Query**:
```
"Find luxury superhero party ideas with entertainment and catering"
```

---

### **Type 2: Vector Database Integration (GuestInfoRetrieverTool)**

**Purpose**: Semantic search with embeddings for guest information using Chroma DB

- **Source**: Local JSON file (`guests.json`) stored in Git repository
- **Database**: Chroma Vector Database (in-memory, no external server needed)
- **Data Structure**: Guest information with 4 fields per record
- **Algorithm**: Vector embeddings with semantic similarity search
- **Retrieval**: Top 3 most relevant guests based on semantic similarity
- **Use Case**: Guest management, contact information, party invitations

**Data Storage Architecture**:
```
GitHub Repository (Git)
└── guests.json (5 guests with embeddings)
    │
    └─> Streamlit Cloud / Local App Startup
        ├─ Loads JSON file
        ├─ Initializes Chroma DB in-memory
        ├─ Embeds guest data
        └─ Ready for semantic search ✅
```

**Guest Fields**:
```yaml
Name: String (Guest's full name)
  - Example: "Ada Lovelace", "Dr. Nikola Tesla", "Marie Curie"

Relation: String (How the guest is related to the host)
  - Examples: "best friend", "old friend from university days", "no relation"

Description: String (Biography or interesting facts about the guest)
  - Example: "Lady Ada Lovelace is my best friend. She is an esteemed 
    mathematician and pioneering computer scientist..."

Email: String (Contact information)
  - Example: "ada.lovelace@example.com"
```

**Current Guest Dataset**:
| Name | Relation | Email |
|------|----------|-------|
| Ada Lovelace | best friend | ada.lovelace@example.com |
| Dr. Nikola Tesla | old friend from university days | nikola.tesla@gmail.com |
| Marie Curie | no relation | marie.curie@example.com |
| Leonardo da Vinci | distant cousin | leonardo.davinci@renaissance.it |
| Alan Turing | colleague from work | alan.turing@bletchley.uk |

**Advantages**:
- 🟣 **Chroma Vector DB**: No external server required
- 📄 **JSON Versioning**: Guest data stored in Git, version controlled
- ⚡ **Fast Startup**: Initializes from JSON on app start (0.1 seconds)
- 🔐 **No External APIs**: Works entirely locally
- ☁️ **Cloud Compatible**: Works perfectly on Streamlit Cloud
- 🎯 **Semantic Search**: Vector embeddings for intelligent matching
- 📝 **Editable**: Simply edit `guests.json` to add/update guests

**How It Works**:
1. **On App Startup**: JSON file is read from the repository
2. **Chroma Initialization**: Vector embeddings are generated in-memory
3. **Semantic Search**: Queries matched against guest descriptions using vectors
4. **Result Ranking**: Top 3 most relevant guests returned by similarity score

**Example Queries**:
```
"Who is Ada Lovelace and how do I contact her?"
"Tell me about my old friend from university days"
"Find guests related to mathematics and computing"
"What's the email of the colleague from work?"
```

---

### **Architecture Comparison**

| Feature | Static KB (BM25) | Vector DB (Chroma) |
|---------|------------------|---------------------|
| **Source** | Embedded in code | JSON file in Git |
| **Search Method** | BM25 ranking | Vector embeddings |
| **External Server** | ❌ No | ❌ No |
| **Dependencies** | Minimal | chromadb package |
| **Cloud Deployment** | ✅ Works | ✅ Works perfectly |
| **Latency** | ⚡ Very Fast | ⚡ Fast (embedded) |
| **Semantic Understanding** | Good | ✅ Excellent |
| **Editability** | Code changes | Edit JSON easily |
| **Scalability** | Limited | Good (for embeddings) |
| **Use Case** | Party ideas | Guest management |

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

### LangChain Integration Tools
| Tool | Description | Usage |
|------|--------------|------------|
| `SerpAPI Search` | Advanced web search via LangChain | Luxury entertainment, events, recommendations |
| `Party Planning Retriever` | Semantic search knowledge base (BM25) | Party ideas, themes, catering, entertainment |
| `Guest Info Retriever` | Guest database from HuggingFace dataset | Guest information, relations, contact details |

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

#### 7️⃣ **LangChain SerpAPI Search Tool** 🔍
```python
# Usage by agent
"Search for luxury entertainment ideas for a superhero-themed event"
```
- Advanced web search using SerpAPI integration via LangChain
- Real-time search results with structured data
- Requires: `SERPAPI_API_KEY` in `.env`
- More powerful alternative to basic web search tools
- Returns: Comprehensive search results with snippets and links

#### 8️⃣ **Party Planning Knowledge Base Retriever** 📚
```python
# Usage by agent
"Find luxury superhero party ideas with entertainment and catering"
```
- Semantic search through curated party planning knowledge base
- Uses BM25 retrieval algorithm for relevant results
- Returns top 5 most relevant suggestions
- Covers: Entertainment, catering, decorations, venues, beverages
- No external API needed - built-in knowledge base
- Perfect for event planning queries

#### 9️⃣ **Guest Information Retriever** 👥
```python
# Usage by agent
"Who is Ada Lovelace and how do I contact her?"
"Tell me about my old friend from university days"
```
- Retrieves guest information from HuggingFace dataset (`agents-course/unit3-invitees`)
- Uses BM25 retrieval for semantic search by name or relation
- Returns: Name, relation to host, biography, email address
- Automatically downloads dataset on first use
- Returns top 3 most relevant matches
- Perfect for party guest management and invitations

#### 🔟 **Text-to-Image Generation** 🎨
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
def initialize_agent(selected_model_id="qwen"):
    """
    Creates and configures the CodeAgent with:
    - Qwen2.5-Coder-32B-Instruct (HuggingFace)
    - OR Gemini 2.5 Flash (Google)
    - All standard and custom tools
    - max_steps=10 for complex tasks
    - verbosity_level=1 for debugging
    """
```

**Key Features:**
- Multi-model support (Qwen + Gemini)
- Model selector dropdown in sidebar
- Dynamic model switching
- Error handling for missing API keys

### `app.py` - Streamlit Frontend (Production-Ready UI)

**Overview:**  
`app.py` is the complete Streamlit application deployed on [Streamlit Cloud](https://smolagents-ai-assistant-up.streamlit.app/) featuring a production-grade multi-session chat interface UI

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
- 🤖 **Model Selector**: Choose between Qwen or Gemini 2.5 Flash
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
| **LLM** | Qwen2.5-Coder-32B-Instruct | Inference Engine (Free) |
| | Gemini 2.5 Flash | Alternative AI Model (Free) |
| **APIs** | Hugging Face Inference | Qwen Model Hosting |
| | Google Generative AI | Gemini Model Hosting |
| | OpenWeatherMap | Weather data |
| | SerpAPI | Google Search |
| **Integration** | langchain-community | LangChain tool integration |
| | langchain-text-splitters | Document chunking for retrieval |
| | rank-bm25 | BM25 semantic search algorithm |
| **Language** | Python 3.8+ | Core Logic |
| **Libraries** | pytz | Timezones |
| | requests | HTTP Calls |
| | huggingface_hub | Hub Integration |
| | litellm | LLM Routing |
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

#### 3. SerpAPI Key (OPTIONAL for Google Search & LangChain)
```env
SERPAPI_API_KEY=xxxxxxxxxxxxxxxxxxxxx
```
**How to obtain:**
- Register at [SerpAPI](https://serpapi.com)
- Free plan: 100 searches/month
- **Used by:** Standard GoogleSearchTool + LangChain SerpAPI integration tool

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
# Check HF_TOKEN in .env
echo $HF_TOKEN

# Verify text-to-image tool is loaded
# Check agent.py for load_tool("agents-course/text-to-image")

# Ensure sufficient disk space (for temporary files)
df -h
```
