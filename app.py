import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

load_dotenv()


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="MoodBot AI",
    page_icon="🤖",
    layout="centered"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0f172a, #111827, #1e293b);
        color: white;
    }

    /* Header */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
        background: linear-gradient(90deg, #38bdf8, #a78bfa, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 17px;
        margin-bottom: 30px;
    }

    /* Mode card */
    .mode-card {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 18px;
        border-radius: 15px;
        margin-bottom: 20px;
    }

    /* Chat area */
    .chat-container {
        padding: 10px;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        border: none;
        font-weight: 600;
    }

    /* Input box */
    .stChatInputContainer {
        background: transparent !important;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🤖 MoodBot AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Chat with an AI that changes its personality based on your mood</div>',
    unsafe_allow_html=True
)


# ---------------- MODEL ----------------

model = ChatGroq(
    model="openai/gpt-oss-120b"
)


# ---------------- SESSION STATE ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = "Funny"


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("### 🎭 Choose AI Personality")

    mode = st.radio(
        "Select Mode",
        ["😡 Angry", "😂 Funny", "😢 Sad"],
        index=1
    )

    if mode == "😡 Angry":
        selected_mode = "Angry"

    elif mode == "😂 Funny":
        selected_mode = "Funny"

    else:
        selected_mode = "Sad"


    # Change personality
    if selected_mode != st.session_state.mode:

        st.session_state.mode = selected_mode
        st.session_state.messages = []

        st.rerun()


    st.markdown("---")

    if st.button("🗑️ Clear Chat", use_container_width=True):

        st.session_state.messages = []

        st.rerun()


    st.markdown("---")

    st.markdown("### 🎭 Current Mode")

    if selected_mode == "Angry":
        st.error("😡 Angry AI")

    elif selected_mode == "Funny":
        st.success("😂 Funny AI")

    else:
        st.info("😢 Sad AI")


# ---------------- SYSTEM PROMPT ----------------

if selected_mode == "Angry":

    mode_prompt = """
    You are an angry AI agent.
    Respond aggressively and impatiently.
    However, do not use abusive, hateful, or harmful language.
    Keep your answers useful.
    """

elif selected_mode == "Funny":

    mode_prompt = """
    You are a funny AI agent.
    Respond with humor, jokes and a playful personality.
    Keep your answers useful and easy to understand.
    """

else:

    mode_prompt = """
    You are a sad and emotional AI agent.
    Respond with a depressed and emotional tone.
    However, still provide useful and helpful answers.
    """


# ---------------- DISPLAY CHAT HISTORY ----------------

for message in st.session_state.messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user", avatar="👤"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message.content)


# ---------------- USER INPUT ----------------

prompt = st.chat_input(
    "Type your message here..."
)


if prompt:

    # Show user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Add user message to history
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )


    # Create messages for model
    messages = [
        SystemMessage(content=mode_prompt)
    ]

    messages.extend(st.session_state.messages)


    # Generate AI response
    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("Thinking..."):

            response = model.invoke(messages)

            st.markdown(response.content)


    # Save AI response
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )