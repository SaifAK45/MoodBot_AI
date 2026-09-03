# 🤖 MoodBot AI

A personality-based AI chatbot built using **LangChain, Groq, and Streamlit**.

MoodBot allows users to chat with an AI that changes its response style based on the selected personality: **Angry 😡, Funny 😂, or Sad 😢**.

---

## ✨ Features

- 🤖 AI-powered conversational chatbot
- 🎭 Multiple AI personalities
  - 😡 Angry Mode
  - 😂 Funny Mode
  - 😢 Sad Mode
- 💬 Maintains conversation history
- 🧠 Uses LangChain message types
- ⚡ Powered by Groq LLM API
- 🎨 Modern Streamlit chat interface
- 🗑️ Clear conversation option
- 🔐 Secure API key management using `.env`
- 🔄 Personality switching

---

## 🧠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| LangChain | LLM application framework |
| Groq | LLM API |
| Streamlit | Web interface |
| Python-dotenv | Environment variable management |

---

## 🏗️ Project Architecture

```text
                    👤 User
                      │
                      ▼
              ┌───────────────┐
              │  Streamlit UI │
              └───────┬───────┘
                      │
                      ▼
              🎭 Select Personality
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       😡 Angry    😂 Funny     😢 Sad
          │           │           │
          └───────────┼───────────┘
                      ▼
              ┌───────────────┐
              │ SystemMessage│
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ HumanMessage  │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │    ChatGroq   │
              │      LLM      │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │   AIMessage   │
              └───────┬───────┘
                      │
                      ▼
              💬 AI Response