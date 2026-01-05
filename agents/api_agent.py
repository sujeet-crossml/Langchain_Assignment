from langchain.agents import create_agent


from tool.weather import get_weather
from .multi_tools import llm
from prompts import system_prompt

# creatin agent for model calling with tools
api_agent = create_agent(
    model = llm,
    tools = [get_weather],
    system_prompt = system_prompt
)