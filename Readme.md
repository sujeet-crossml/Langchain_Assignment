# LANGCHAIN_ASSIGNMENT

This repository demonstrates the implementation of **LangChain tool-based agents** using **Google Gemini models**.  
The project showcases how Large Language Models (LLMs) can dynamically choose and invoke **single tools, multiple tools, and API-based tools** to solve user queries.

---

## 📌 Project Objective

The goal of this assignment is to:
- Understand **LangChain Agents**
- Implement **custom tools**
- Explore **single-tool vs multi-tool agents**
- Integrate **external APIs** with LLMs
- Learn practical **agent orchestration** using Google Gemini

---

## 🧠 Agents Implemented

### 1️⃣ Single Tool Agent
- Uses **one tool only**
- Suitable for focused tasks like calculations

### 2️⃣ Multi Tool Agent
- Uses **multiple tools**
- LLM decides which tool to call based on user intent

### 3️⃣ API Agent
- Integrates **external APIs**
- Example: Weather information retrieval

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Framework:** LangChain
- **LLM:** Google Gemini  
  - `gemini-2.5-flash`
  - `gemini-2.5-flash-lite`
- **Environment:** Virtual Environment (`venv`)
- **API:** OpenWeatherMap

---

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

            git clone https://github.com/sujeet-crossml/Langchain_Assignment.git
            cd Langchain_Assignment

### 2️⃣ Create & Activate Virtual Environment

      python -m venv myenv
      source myenv/bin/activate     # Linux / macOS
      myenv\Scripts\activate        # Windows

### 🔐 API Key Configuration

Add your Gemini API Key in cred.py:

    gemini_api_key = "YOUR_GEMINI_API_KEY"


### ⚠️ Important:
Do not commit your real API key to GitHub.
Use .env and environment variables for production projects.

### ▶️ How to Run

Run the main application:

    python main.py


The agent will:
- Understand the user query
- Select the appropriate tool
- Execute the tool
- Return the final response

### 📌 Example Use Cases

- Solve mathematical calculations
- Find future dates
- Analyze text content
- Fetch weather information
- Dynamically choose tools based on query intent

### 🧪 Learning Outcomes

- Practical understanding of LangChain Agents
- Tool invocation and orchestration
- Differences between single-tool and multi-tool agents
- API integration with LLMs
- Clean project structuring for AI applications

