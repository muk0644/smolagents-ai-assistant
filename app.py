#front end developed using streamlit
import streamlit as st
import os
from dotenv import load_dotenv
from agent import initialize_agent  # Import the agent setup function

# 1. PAGE CONFIG
st.set_page_config(
    page_title="SmolAgents", 
    page_icon="🕵️", 
    layout="wide"
)
load_dotenv()

# 2. SECURITY CHECK
if not os.environ.get("HF_TOKEN"):
    st.error("❌ HF_TOKEN not found in .env file.")
    st.stop()

# 3. INITIALIZE AGENT (Cached)
@st.cache_resource
def get_cached_agent():
    return initialize_agent()

agent = get_cached_agent()

# 4. SIDEBAR
def reset_conversation():
    st.session_state.messages = []

with st.sidebar:
    st.header("Capabilities")
    if st.button("🗑️ New Chat", on_click=reset_conversation, type="primary"):
        st.write("Chat cleared!")
    st.caption("Powered by smolagents")

# 5. MAIN INTERFACE

# --- HEADER LOGO ---
HEADER_LOGO = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/smolagents/smolagents.png"
st.image(HEADER_LOGO, width=300)

st.markdown("""
### Welcome! I am your intelligent agent. 

Ask questions related to:

* **🌤️ REAL WEATHER**: 'Weather in Erkner right now'
* **🔍 WEB SEARCH**: 'Who is the CEO of Hugging Face?'
* **🎨 IMAGE GEN**: 'Generate an image of a cyberpunk city'
* **🧮 MATH & PYTHON**: 'Calculate sqrt(123456789) * pi'
* **🎉 PARTY & EVENTS**: 'Plan a superhero party for Batman'
""")

# --- CHAT LOGIC ---
AGENT_AVATAR = "https://debuggercafe.com/wp-content/uploads/2025/01/smolagents-logo.png"
USER_AVATAR = "👤"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    avatar_icon = AGENT_AVATAR if message["role"] == "assistant" else USER_AVATAR
    with st.chat_message(message["role"], avatar=avatar_icon):
        st.markdown(message["content"])
        if "image_path" in message:
            st.image(message["image_path"])

if prompt := st.chat_input("Type your message..."):
    st.chat_message("user", avatar=USER_AVATAR).markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant", avatar=AGENT_AVATAR):
        with st.spinner("Thinking..."):
            try:
                response = agent.run(prompt)
                response_str = str(response)
                
                if response_str.endswith(('.png', '.jpg', '.jpeg', '.webp')) and os.path.exists(response_str):
                    st.image(response_str, caption="Generated Image")
                    st.success(f"Image saved at: {response_str}")
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": "Here is the generated image:", 
                        "image_path": response_str
                    })
                else:
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"An error occurred: {e}")