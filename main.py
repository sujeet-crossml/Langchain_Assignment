

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from cred import gemini_api_key

model = ChatGoogleGenerativeAI(model = "gemini-3-flash-preview", api_key = gemini_api_key)

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model = model,
    tools = [get_weather],
    system_prompt = "You are a helpful assistant",
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)

print(response['messages'])