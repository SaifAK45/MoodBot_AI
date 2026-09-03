# 🤖 MoodBot AI

A simple AI chatbot built with **LangChain, Groq, and Streamlit** that can change its personality based on the selected mood.

The user can choose between **Angry 😡, Funny 😂, and Sad 😢** modes and chat with the AI using a modern Streamlit interface.

---


## 📌 Features

- 🤖 AI-powered chatbot
- 🎭 Three different AI personalities
  - 😡 Angry Mode
  - 😂 Funny Mode
  - 😢 Sad Mode
- 💬 Conversation history
- 🧠 LangChain message handling
- ⚡ Groq API for fast LLM responses
- 🎨 Modern Streamlit chat interface
- 🗑️ Clear chat functionality
- ⚙️ Easy personality switching
- 🔐 API key stored using `.env`

---

## 🛠️ Tech Stack

### AI / LLM

- Groq
- OpenAI GPT-OSS 120B
- LangChain

### Backend

- Python
- LangChain
- LangChain Groq

### Frontend

- Streamlit
- Custom CSS

### Environment

- Python-dotenv
- `.env`

---

## 🏗️ Project Architecture

```text
              ┌──────────────────┐
              │      User        │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │  Streamlit UI    │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Select Personality│
              │                  │
              │ 😡 Angry         │
              │ 😂 Funny         │
              │ 😢 Sad           │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ SystemMessage    │
              │ Personality      │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ HumanMessage     │
              │ User Input       │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │    ChatGroq      │
              │   LLM Model      │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   AIMessage      │
              │   AI Response    │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Streamlit Chat   │
              │      UI          │
              └──────────────────┘
