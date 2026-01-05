from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent


from cred import gemini_api_key
from tool.weather import get_weather
from .multi_tools import llm


api_agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt='You are helpful assistance.'
)