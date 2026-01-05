"""
Agent that intelligently selects ONE tool.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from cred import gemini_api_key
from tool.math import math_calculator
from tool.text_analyzer import analyze_text
from tool.date import future_date

# defining chat model for gemini with api key config
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0
)


# creating agent for model calling with real api tools
single_tool_agent = create_agent(
    model=llm,
    tools=[math_calculator]
)
