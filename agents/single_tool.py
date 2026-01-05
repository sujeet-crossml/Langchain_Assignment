"""
Agent that intelligently selects ONE tool.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from cred import gemini_api_key
from tool.math import math_calculator
from tool.text_analyzer import analyze_text
from tool.date import future_date


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0
)



# Create agent
single_tool_agent = create_agent(
    model=llm,
    tools=[math_calculator]
)
