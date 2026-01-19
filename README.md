# Python AI Agent 🤖

A modular Python-based AI agent that interacts with users via text and performs multiple tasks using simple NLP (keyword-based intent detection).  
The project includes both a **Command Line Interface (CLI)** version and a **Flask-based Web UI** with chat history.

---

## ✨ Features

- Accepts natural language text input
- Keyword-based intent detection (lightweight NLP)
- Multiple built-in capabilities:
  - Basic arithmetic calculations
  - Wikipedia search and short summaries
  - To-do list management
  - Jokes
- Maintains conversational context during a session
- Modular and easily extensible design
- Available as:
  - CLI application
  - Web application (Flask UI)

---

## 🖥️ CLI Version

The CLI version focuses on validating core agent logic and functionality.

### How to Run

```bash
pip install -r requirements.txt
python main.py
```

### Example Commands

```text
calculate 10 + 5
wiki Artificial Intelligence
add todo buy groceries
show todo
tell me a joke
exit
```

### CLI Design Notes

- Infinite input loop for continuous interaction
- Intent detection handled by a central agent module
- Each functionality implemented in a separate module
- To-do list stored in memory for the session

---

## 🌐 Web Version (Flask UI)

The web version extends the same core AI agent logic with a browser-based interface.

### How to Run

```bash
pip install -r requirements.txt
python web_app.py
```

Open your browser at:

```
http://127.0.0.1:5000
```

### Web UI Features

- Dark, tech-inspired UI theme
- Chat-style conversation layout
- Persistent chat history during the session
- Reuses the same agent logic as the CLI version

### Web Design Notes

- Flask used for lightweight backend routing
- Server-side rendering using Jinja templates
- Chat history stored in memory for simplicity
- No duplication of business logic between CLI and Web versions

---

## 🧠 Architecture & Design Decisions

- **Modular Design**  
  Each capability (calculator, Wikipedia search, to-do list, jokes) is implemented as a separate module.

- **Single Agent Controller**  
  A central agent class handles intent detection and routes user input to the appropriate module.

- **Keyword-Based NLP**  
  Simple keyword matching is used for intent detection to keep the system lightweight, interpretable, and easy to extend.

- **Reusability**  
  The same core agent logic is reused across CLI and web interfaces without modification.

- **Session Context**  
  Chat history and to-do list are maintained in memory for the duration of a session.

---

## 🤖 LLM Integration (Bonus)

The agent includes an optional LLM-based fallback for handling open-ended or general user queries.

- Keyword-based intent detection is applied first for deterministic tasks such as calculations, Wikipedia search, and to-do management.
- If no intent matches, the query is forwarded to an LLM along with recent conversation history to preserve context.
- The LLM is integrated as a **fallback mechanism**, ensuring core functionality remains lightweight and interpretable.

### Error Handling & Quota Awareness
- API quota and rate-limit errors are handled gracefully.
- If the LLM service is unavailable, the agent returns a clear fallback message instead of failing.
- With a valid API key and available credits, the same integration seamlessly enables LLM-powered responses.

This hybrid approach combines rule-based reliability with the flexibility of large language models.

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Backend Framework:** Flask
- **Libraries & Tools:**
  - wikipedia (Wikipedia API wrapper)
- **Frontend:**
  - HTML
  - CSS (dark tech theme)
- **Architecture Style:**
  - Modular, layered design
  - Separation of concerns (UI vs logic)

---

## 🚀 Possible Extensions

- Replace keyword-based intent detection with ML/NLP models
- Integrate an LLM API (e.g., OpenAI) for general question answering
- Persist chat history and to-do items using a database
- Add authentication and multi-user support
- Deploy to a cloud platform

---

## 📌 Author

**Shruti Paulastye**  
Final Year B.Tech CSE Student
IIIT SURAT
