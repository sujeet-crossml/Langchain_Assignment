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
- **Weather API:** OpenWeatherMap


---

## 📂 Project Structure

LANGCHAIN_ASSIGNMENT/
│
├── agents/
│ ├── api_agent.py # Agent using external API tool (weather)
│ ├── multi_tools.py # Agent using multiple tools
│ ├── single_tool.py # Agent using a single tool
│
├── tool/
│ ├── math.py # Math calculation tool
│ ├── date.py # Date / future date tool
│ ├── text_analyzer.py # Text analysis tool
│ ├── weather.py # Weather API tool
│
├── cred.py # Gemini API key configuration
├── main.py # Application entry point
├── requirements.txt # Project dependencies
├── .env # Environment variables (ignored by git)
├── .gitignore
└── Readme.md

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/sujeet-crossml/Langchain_Assignment.git
cd Langchain_Assignment
2️⃣ Create & Activate Virtual Environment
bash
Copy code
python -m venv myenv
source myenv/bin/activate     # Linux / macOS
myenv\Scripts\activate        # Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
🔐 API Key Configuration
Add your Gemini API Key in cred.py:

python
Copy code
gemini_api_key = "YOUR_GEMINI_API_KEY"
⚠️ Important:
Do not commit your real API key to GitHub.
Use .env and environment variables for production projects.

▶️ How to Run
Run the main application:

bash
Copy code
python main.py
The agent will:

Understand the user query

Select the appropriate tool

Execute the tool

Return the final response

📌 Example Use Cases
Solve mathematical calculations

Find future dates

Analyze text content

Fetch weather information

Dynamically choose tools based on query intent

🧪 Learning Outcomes
Practical understanding of LangChain Agents

Tool invocation and orchestration

Differences between single-tool and multi-tool agents

API integration with LLMs

Clean project structuring for AI applications