
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent


from cred import gemini_api_key
from tool.math import math_calculator
from tool.date import future_date
from tool.text_analyzer import analyze_text


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=gemini_api_key,
    temperature=0
)

tools = [math_calculator, future_date, analyze_text]

multi_tool_agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt='You are helpful assistance.'
)
