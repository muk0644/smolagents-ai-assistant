#front end developed using streamlit
import streamlit as st
import os
import json
import base64
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv
from agent import initialize_agent  # Import the agent setup function

# 1. PAGE CONFIG
st.set_page_config(
    page_title="SmolAgents", 
    page_icon="🕵️", 
    layout="wide"
)
load_dotenv()

# 2. CUSTOM CSS FOR ULTRA-COMPACT SIDEBAR (ChatGPT/Gemini Style)
st.markdown("""
<style>
    /* === SIDEBAR CONTAINER PADDING === */
    [data-testid="stSidebar"] {
        padding-top: 0.5rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0.5rem !important;
    }
    
    /* === VERTICAL SPACING REDUCTION === */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0.25rem !important;
    }
    
    [data-testid="stSidebar"] .element-container {
        margin-bottom: 0.25rem !important;
    }
    
    /* === HEADER SPACING === */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4 {
        margin-top: 0.3rem !important;
        margin-bottom: 0.3rem !important;
        padding: 0 !important;
    }
    
    /* === BUTTON STYLING (COMPACT) === */
    [data-testid="stSidebar"] button {
        margin-bottom: 0.2rem !important;
        padding: 0.4rem 0.5rem !important;
        font-size: 0.85rem !important;
    }
    
    /* === DIVIDER (HR) SPACING === */
    [data-testid="stSidebar"] hr {
        margin-top: 0.4rem !important;
        margin-bottom: 0.4rem !important;
    }
    
    /* === IMAGE THUMBNAILS (FIXED SIZE) === */
    [data-testid="stSidebar"] img {
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.2s ease;
        max-height: 80px !important;
        object-fit: cover;
        border: 2px solid transparent;
    }
    
    [data-testid="stSidebar"] img:hover {
        transform: scale(1.08);
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
        border-color: #ff4b4b;
    }
    
    /* === COLUMN SPACING (FOR THUMBNAILS) === */
    [data-testid="stSidebar"] [data-testid="column"] {
        padding: 0.1rem !important;
    }
    
    /* === CAPTION/TEXT SPACING === */
    [data-testid="stSidebar"] .caption,
    [data-testid="stSidebar"] p {
        margin-top: 0.1rem !important;
        margin-bottom: 0.1rem !important;
    }
    
    /* === INFO BOXES (COMPACT) === */
    [data-testid="stSidebar"] [data-testid="stNotification"] {
        padding: 0.4rem !important;
        margin: 0.2rem 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# 2. SECURITY CHECK
if not os.environ.get("HF_TOKEN"):
    st.error("❌ HF_TOKEN not found in .env file.")
    st.stop()

# 3. CONSTANTS
MAX_TOOL_LIMIT = 10  # Maximum tool-usage per email (global across all sessions)
RESET_INTERVAL_MINUTES = 60  # Auto-reset quota after 60 minutes
USER_DATA_DIR = Path("user_data")
MAX_SESSIONS_PER_USER = 5  # Store only latest 5 chat sessions per user

# Create user_data directory if it doesn't exist
USER_DATA_DIR.mkdir(exist_ok=True)

# 4. EMAIL LOGIN SYSTEM - MAIN PAGE CENTERED
# Initialize email in session state if not present
if "user_email" not in st.session_state:
    st.session_state.user_email = None

# ============================================================================
# LOGGED OUT STATE: Show centered login screen
# ============================================================================
if st.session_state.user_email is None:
    # Create centered layout with columns
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Wrap login interface in a container for better styling
        with st.container():
            # Welcome header with vertical padding
            st.markdown("""
            <div style='text-align: center; padding: 80px 0 40px 0;'>
                <h1 style='font-size: 3rem; margin-bottom: 10px;'>🕵️ SmolAgents Portal</h1>
                <p style='font-size: 1.2rem; color: #666;'>Your Intelligent AI Assistant</p>
                <p style='font-size: 0.9rem; color: #999; margin-top: 20px;'>Sign in with your email to get started</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Email input field
            email_input = st.text_input(
                "Email Address",
                placeholder="user@example.com",
                key="email_login_input",
                label_visibility="collapsed"
            )
            
            # Continue button
            if st.button("Continue", type="primary", use_container_width=True):
                if email_input and "@" in email_input:
                    st.session_state.user_email = email_input
                    st.rerun()
                else:
                    st.error("⚠️ Please enter a valid email address")
            
            # Footer info
            st.markdown("""
            <div style='text-align: center; padding: 40px 0 0 0; color: #999; font-size: 0.85rem;'>
                <p>Powered by <strong>smolagents</strong> & Hugging Face</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.stop()  # Stop execution until logged in

# ============================================================================
# LOGGED IN STATE: Main application
# ============================================================================
else:
    # User is authenticated - proceed with app
    user_email = st.session_state.user_email
    user_filename = user_email.replace("@", "_").replace(".", "_") + ".json"
    user_file_path = USER_DATA_DIR / user_filename

    # 5. USER DATA PERSISTENCE FUNCTIONS
    def load_user_data(email_file_path: Path) -> dict:
        """
        Load user-specific data from JSON file.
        New schema with global tool quota and multiple chat sessions:
        {
            "global_tool_usage": 3,
            "last_reset_time": "2026-01-20T15:30:00",
            "sessions": [
                {
                    "session_id": "1234567890",
                    "title": "Weather in Berlin",
                    "messages": [...]
                }
            ]
        }
        """
        if email_file_path.exists():
            try:
                with open(email_file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print(f"📂 [DEBUG] Loaded data for {email_file_path.name}: {data.get('global_tool_usage', 0)} global tools used, {len(data.get('sessions', []))} sessions")
                    return data
            except Exception as e:
                print(f"⚠️ [DEBUG] Error loading user data: {e}")
        return {
            "global_tool_usage": 0,
            "last_reset_time": datetime.now().isoformat(),
            "sessions": []
        }

    def save_user_data(email_file_path: Path, global_tool_usage: int, last_reset_time: datetime, sessions: list):
        """
        Save user-specific data to JSON file with new schema.
        Keeps only the latest MAX_SESSIONS_PER_USER sessions.
        """
        # Keep only the latest N sessions
        limited_sessions = sessions[-MAX_SESSIONS_PER_USER:] if len(sessions) > MAX_SESSIONS_PER_USER else sessions
        
        data = {
            "global_tool_usage": global_tool_usage,
            "last_reset_time": last_reset_time.isoformat(),
            "sessions": limited_sessions
        }
        
        try:
            with open(email_file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"💾 [DEBUG] Saved data for {email_file_path.name}: {global_tool_usage} global tools, {len(limited_sessions)} sessions")
        except Exception as e:
            print(f"⚠️ [DEBUG] Error saving user data: {e}")

    def get_session_title(messages: list) -> str:
        """Generate session title from first user message (first 30 chars)"""
        if messages:
            first_user_msg = next((msg for msg in messages if msg.get("role") == "user"), None)
            if first_user_msg:
                content = first_user_msg.get("content", "New Chat")
                return content[:30] + "..." if len(content) > 30 else content
        return "New Chat"

    def create_new_session() -> dict:
        """Create a new empty session with unique ID"""
        return {
            "session_id": str(int(datetime.now().timestamp() * 1000)),  # Millisecond timestamp as ID
            "title": "New Chat",
            "messages": []
        }

    # 6. SESSION STATE INITIALIZATION WITH PERSISTENCE
    # Professional architecture: Each user session gets its own isolated agent instance
    # This prevents cross-user contamination and enables per-session quota tracking

    # Load user-specific data from JSON
    user_data = load_user_data(user_file_path)

    if "agent" not in st.session_state:
        st.session_state.agent = initialize_agent()
        print(f"🤖 [DEBUG] Initialized new agent instance for {user_email}")

    # Initialize or load global tool usage (shared across all sessions)
    if "global_tool_usage" not in st.session_state:
        st.session_state.global_tool_usage = user_data.get("global_tool_usage", 0)
        print(f"🌐 [DEBUG] Loaded GLOBAL tool_usage for {user_email}: {st.session_state.global_tool_usage}/{MAX_TOOL_LIMIT}")

    # Initialize or load last reset time (global for user)
    if "last_reset_time" not in st.session_state:
        try:
            st.session_state.last_reset_time = datetime.fromisoformat(user_data.get("last_reset_time", datetime.now().isoformat()))
        except:
            st.session_state.last_reset_time = datetime.now()
        print(f"⏰ [DEBUG] Last reset time for {user_email}: {st.session_state.last_reset_time}")

    # Load all sessions from JSON
    if "all_sessions" not in st.session_state:
        st.session_state.all_sessions = user_data.get("sessions", [])
        if not st.session_state.all_sessions:
            # Create first session if none exist
            st.session_state.all_sessions = [create_new_session()]
        print(f"📚 [DEBUG] Loaded {len(st.session_state.all_sessions)} sessions for {user_email}")

    # Track current active session ID
    if "current_session_id" not in st.session_state:
        # Load the most recent session by default
        st.session_state.current_session_id = st.session_state.all_sessions[-1]["session_id"]
        print(f"📍 [DEBUG] Set current session to: {st.session_state.current_session_id}")

    # Load messages for current session
    if "messages" not in st.session_state:
        current_session = next((s for s in st.session_state.all_sessions if s["session_id"] == st.session_state.current_session_id), None)
        st.session_state.messages = current_session["messages"] if current_session else []
        print(f"📜 [DEBUG] Loaded {len(st.session_state.messages)} messages for current session")

    # 7. TIME-BASED AUTO-RESET LOGIC (GLOBAL FOR USER)
    # Automatically reset the GLOBAL tool usage quota after RESET_INTERVAL_MINUTES
    elapsed_time = datetime.now() - st.session_state.last_reset_time
    elapsed_minutes = elapsed_time.total_seconds() / 60

    if elapsed_minutes >= RESET_INTERVAL_MINUTES:
        # Auto-reset triggered - resets GLOBAL counter for ALL sessions
        st.session_state.global_tool_usage = 0
        st.session_state.last_reset_time = datetime.now()
        st.session_state.agent.memory.steps = []
        # Save reset to JSON
        save_user_data(user_file_path, 0, st.session_state.last_reset_time, st.session_state.all_sessions)
        print(f"🔄 [DEBUG] GLOBAL auto-reset triggered for {user_email} after {elapsed_minutes:.1f} minutes - Counter reset to 0/{MAX_TOOL_LIMIT}")

    # 8. HELPER FUNCTIONS
    def did_agent_use_tools(agent) -> bool:
        """
        Inspects the agent's memory to determine if tools were actually used.
        This is more robust than keyword-based detection as it checks the actual
        execution log from smolagents.
        
        Scans agent.memory.steps in REVERSE order to detect tool usage.
        Returns True if it finds ANY action that is:
        - NOT None
        - NOT 'final_answer' (which is just the agent's response, not a tool)
        - NOT empty
        
        This ensures we detect tool usage even if the agent adds a final
        conversational step after the tool call.
        """
        try:
            if hasattr(agent, 'memory') and hasattr(agent.memory, 'steps') and agent.memory.steps:
                # Scan steps in reverse order to find tool usage
                for step in reversed(agent.memory.steps):
                    if hasattr(step, 'action') and step.action is not None and step.action != '':
                        # Get the action name (tool name)
                        action_name = step.action if isinstance(step.action, str) else getattr(step.action, 'tool_name', str(step.action))
                        
                        # Only count if it's NOT the final_answer tool
                        if action_name and action_name != 'final_answer':
                            print(f"🔍 [DEBUG] Tool detected in memory: {action_name}")
                            return True
            return False
        except Exception as e:
            print(f"⚠️ [DEBUG] Error checking agent memory: {e}")
            return False

    def get_time_remaining() -> int:
        """Calculate minutes remaining until auto-reset"""
        elapsed_time = datetime.now() - st.session_state.last_reset_time
        elapsed_minutes = elapsed_time.total_seconds() / 60
        return max(0, int(RESET_INTERVAL_MINUTES - elapsed_minutes))

    def load_session(session_id: str):
        """Load a specific session by ID"""
        session = next((s for s in st.session_state.all_sessions if s["session_id"] == session_id), None)
        if session:
            st.session_state.current_session_id = session_id
            st.session_state.messages = session["messages"].copy()
            st.session_state.agent.memory.steps = []  # Clear agent memory
            print(f"📂 [DEBUG] Loaded session {session_id}: {session.get('title', 'Untitled')}")

    def save_current_session():
        """Save current messages to the active session in all_sessions list"""
        for session in st.session_state.all_sessions:
            if session["session_id"] == st.session_state.current_session_id:
                session["messages"] = st.session_state.messages
                # Update title if messages exist
                if st.session_state.messages and session["title"] == "New Chat":
                    session["title"] = get_session_title(st.session_state.messages)
                break

    def create_and_switch_to_new_session():
        """Create a new session and switch to it"""
        new_session = create_new_session()
        st.session_state.all_sessions.append(new_session)
        
        # Rotate: keep only latest MAX_SESSIONS_PER_USER
        if len(st.session_state.all_sessions) > MAX_SESSIONS_PER_USER:
            st.session_state.all_sessions.pop(0)  # Remove oldest
            print(f"🔄 [DEBUG] Rotated sessions - removed oldest, kept {MAX_SESSIONS_PER_USER}")
        
        st.session_state.current_session_id = new_session["session_id"]
        st.session_state.messages = []
        st.session_state.agent.memory.steps = []
        print(f"✨ [DEBUG] Created new session: {new_session['session_id']}")
        
        # Save immediately
        save_user_data(user_file_path, st.session_state.global_tool_usage, st.session_state.last_reset_time, st.session_state.all_sessions)

    def reset_conversation():
        """
        Manual reset: Clear GLOBAL tool counter, reset timer, and create fresh session
        """
        # Reset global counter
        st.session_state.global_tool_usage = 0
        st.session_state.last_reset_time = datetime.now()
        
        # Clear all sessions
        st.session_state.all_sessions = [create_new_session()]
        st.session_state.current_session_id = st.session_state.all_sessions[0]["session_id"]
        st.session_state.messages = []
        st.session_state.agent.memory.steps = []
        
        # Clear the user's JSON file and save fresh state
        if user_file_path.exists():
            user_file_path.unlink()
            print(f"🗑️ [DEBUG] Deleted JSON file for {user_email}")
        
        save_user_data(user_file_path, 0, st.session_state.last_reset_time, st.session_state.all_sessions)
        print(f"🔄 [DEBUG] FULL RESET for {user_email} - All sessions cleared, counter: 0/{MAX_TOOL_LIMIT}")
    
    def logout():
        """
        Logout: Clear session state (except agent) and return to login screen
        """
        # Clear all session-specific data except agent instance
        keys_to_clear = ['user_email', 'global_tool_usage', 'last_reset_time', 
                        'all_sessions', 'current_session_id', 'messages']
        for key in keys_to_clear:
            if key in st.session_state:
                del st.session_state[key]
        print(f"🚪 [DEBUG] User {user_email} logged out")

    # 9. SIDEBAR - ULTRA-COMPACT CHATGPT/GEMINI STYLE
    with st.sidebar:
        # === TOP: LOGIN & CAPABILITIES (MINIMAL) ===
        st.markdown(f"<div style='font-size: 0.8rem; color: #666; margin: 0; padding: 0;'>✅ {user_email}</div>", unsafe_allow_html=True)
        
        # Capabilities (inline, single line)
        usage_color = "🟢" if st.session_state.global_tool_usage < MAX_TOOL_LIMIT else "🔴"
        minutes_remaining = get_time_remaining()
        st.markdown(f"""
        <div style='font-size: 0.75rem; margin: 0.25rem 0 0.4rem 0; color: #888;'>
            {usage_color} {st.session_state.global_tool_usage}/{MAX_TOOL_LIMIT} • ⏰ {minutes_remaining}m
        </div>
        """, unsafe_allow_html=True)
        
        # === PRIMARY ACTION: NEW CHAT BUTTON ===
        if st.button("➕ New Chat", type="primary", use_container_width=True, key="primary_new_chat"):
            create_and_switch_to_new_session()
            st.rerun()
        
        st.markdown("<div style='border-top: 1px solid #ddd; margin: 0.5rem 0;'></div>", unsafe_allow_html=True)
        
        # === YOUR CONTENTS: COMPACT IMAGE GALLERY ===
        st.markdown("<div style='font-size: 0.85rem; font-weight: 600; margin: 0.4rem 0 0.3rem 0;'>Your Contents</div>", unsafe_allow_html=True)
        
        # Collect all images from all sessions
        all_images = []
        for session in st.session_state.all_sessions:
            for msg in session.get("messages", []):
                if "image_base64" in msg:
                    all_images.append({
                        "base64": msg["image_base64"],
                        "timestamp": msg.get("timestamp", "image"),
                        "session_id": session["session_id"]
                    })
        
        # Display latest 3 images as compact thumbnails
        if all_images:
            latest_images = all_images[-3:]  # Get last 3 images
            cols = st.columns(len(latest_images))
            
            for idx, img_data in enumerate(latest_images):
                with cols[idx]:
                    try:
                        image_bytes = base64.b64decode(img_data["base64"])
                        st.image(image_bytes, use_container_width=True)
                    except Exception as e:
                        st.caption("⚠️")
        else:
            st.markdown("<div style='font-size: 0.75rem; color: #999; margin: 0.2rem 0;'>🖼️ No images yet</div>", unsafe_allow_html=True)
        
        st.markdown("<div style='border-top: 1px solid #ddd; margin: 0.5rem 0;'></div>", unsafe_allow_html=True)
        
        # === CHATS HISTORY (COMPACT) ===
        st.markdown("<div style='font-size: 0.85rem; font-weight: 600; margin: 0.4rem 0 0.3rem 0;'>Chats</div>", unsafe_allow_html=True)
        
        # Display sessions in reverse order (newest first)
        for session in reversed(st.session_state.all_sessions):
            is_active = session["session_id"] == st.session_state.current_session_id
            # Remove redundant pin emoji from button - use simple indicator
            button_label = f"{'●' if is_active else '○'} {session['title']}"
            
            if st.button(button_label, key=f"session_{session['session_id']}", use_container_width=True):
                if not is_active:
                    load_session(session["session_id"])
                    st.rerun()
        
        st.markdown("<div style='border-top: 1px solid #ddd; margin: 0.5rem 0;'></div>", unsafe_allow_html=True)
        
        # === BOTTOM: COMPACT ACTION BUTTONS ===
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ Reset", use_container_width=True, help="Clear all data"):
                reset_conversation()
                st.rerun()
        with col2:
            if st.button("🚪 Logout", use_container_width=True, help="Sign out"):
                logout()
                st.rerun()
        
        st.markdown("<div style='text-align: center; font-size: 0.65rem; color: #aaa; margin-top: 0.4rem;'>Powered by smolagents</div>", unsafe_allow_html=True)

    # 10. MAIN INTERFACE

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

    # Display warning if GLOBAL tool limit reached (but don't block input)
    # User can still send messages, but agent may not be able to use tools
    if st.session_state.global_tool_usage >= MAX_TOOL_LIMIT:
        minutes_remaining = get_time_remaining()
        st.warning(f"""
        ⚠️ **Global tool limit reached for your account.**  
        You've used {st.session_state.global_tool_usage}/{MAX_TOOL_LIMIT} tools across ALL your chat sessions.  
        Tools will automatically reset in **{minutes_remaining} minutes**.
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
            
            # Handle base64-encoded images (ephemeral image system)
            if "image_base64" in message:
                try:
                    # Decode base64 string to bytes
                    image_bytes = base64.b64decode(message["image_base64"])
                    st.image(image_bytes, caption="Generated Image")
                    
                    # Add download button for the image
                    st.download_button(
                        label="💾 Download Image",
                        data=image_bytes,
                        file_name=f"generated_image_{message.get('timestamp', 'image')}.png",
                        mime="image/png"
                    )
                except Exception as e:
                    st.error(f"Error displaying image: {e}")

    if prompt := st.chat_input("Type your message..."):
        # Display the user's message
        st.chat_message("user", avatar=USER_AVATAR).markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Process the query with the session-specific agent
        # Note: We no longer pre-check the prompt with keywords. Instead, we inspect
        # the agent's memory after execution to accurately determine if tools were used.
        with st.chat_message("assistant", avatar=AGENT_AVATAR):
            with st.spinner("Thinking..."):
                try:
                    # Always allow the agent to process the request
                    # Use the session-specific agent instance
                    response = st.session_state.agent.run(prompt)
                    response_str = str(response)
                    
                    # ROBUST TOOL DETECTION: Check agent's memory for actual tool usage
                    # This is more accurate than keyword-based detection as it inspects
                    # the agent's execution log (agent.memory.steps) to see if any tools
                    # were actually invoked during the response generation.
                    # We scan in reverse order and exclude 'final_answer' to avoid false positives
                    tool_was_used = did_agent_use_tools(st.session_state.agent)
                    
                    # Track if we need to update the UI
                    should_rerun = False
                    
                    if tool_was_used:
                        st.session_state.global_tool_usage += 1
                        should_rerun = True  # Flag for UI update
                        print(f"🔧 [DEBUG] Tool was used - GLOBAL Counter: {st.session_state.global_tool_usage}/{MAX_TOOL_LIMIT}, Time remaining: {get_time_remaining()}min")
                        
                        # Show limit warning after this response if we just hit the limit
                        if st.session_state.global_tool_usage >= MAX_TOOL_LIMIT:
                            minutes_remaining = get_time_remaining()
                            st.info(f"ℹ️ You've reached the GLOBAL tool usage limit across all sessions. Auto-reset in {minutes_remaining} minutes.")
                    else:
                        print(f"💬 [DEBUG] No tools used - GLOBAL Counter unchanged: {st.session_state.global_tool_usage}/{MAX_TOOL_LIMIT}")
                    
                    # Display the response (regardless of limit status)
                    # EPHEMERAL IMAGE HANDLING: Read image, delete file, convert to base64
                    if response_str.endswith(('.png', '.jpg', '.jpeg', '.webp')) and os.path.exists(response_str):
                        try:
                            # Read image file into memory
                            with open(response_str, 'rb') as img_file:
                                image_bytes = img_file.read()
                            
                            # IMMEDIATELY DELETE the local file (ephemeral)
                            os.remove(response_str)
                            print(f"🗑️ [DEBUG] Deleted ephemeral image file: {response_str}")
                            
                            # Convert to base64 for storage
                            image_base64 = base64.b64encode(image_bytes).decode('utf-8')
                            
                            # Display image in chat
                            st.image(image_bytes, caption="Generated Image")
                            
                            # Provide download button
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            st.download_button(
                                label="💾 Download Image",
                                data=image_bytes,
                                file_name=f"generated_image_{timestamp}.png",
                                mime="image/png"
                            )
                            
                            # Store base64 in messages (NOT file path)
                            st.session_state.messages.append({
                                "role": "assistant",
                                "content": "Here is the generated image:",
                                "image_base64": image_base64,
                                "timestamp": timestamp
                            })
                        except Exception as e:
                            st.error(f"Error handling image: {e}")
                            print(f"❌ [DEBUG] Image handling error: {e}")
                    else:
                        # Regular text response
                        st.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})
                    
                    # SAVE CURRENT SESSION AND USER DATA TO JSON AFTER EACH INTERACTION
                    # Update current session with latest messages
                    save_current_session()
                    
                    # Save all sessions with global counter to JSON
                    save_user_data(user_file_path, st.session_state.global_tool_usage, st.session_state.last_reset_time, st.session_state.all_sessions)
                    
                    # STREAMLIT UI UPDATE FIX:
                    # Force a rerun to immediately update the sidebar's tool_usage counter.
                    # Why? Streamlit renders top-to-bottom, so the sidebar was already rendered
                    # before we updated tool_usage. By calling st.rerun(), we trigger a fresh
                    # render cycle, ensuring the sidebar displays the updated counter immediately.
                    if should_rerun:
                        st.rerun()
                        
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    print(f"❌ [DEBUG] Error occurred: {e}")