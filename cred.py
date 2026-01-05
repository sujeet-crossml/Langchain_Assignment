import os

from dotenv import load_dotenv

# Loading environment variable
load_dotenv()

# Getting gemini api key
gemini_api_key = os.getenv("GEMINI_API_KEY", "")

# Getting weather api key
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")

if not gemini_api_key:
    raise EnvironmentError("Gemini API Key is not found!")

if not WEATHER_API_KEY:
    raise EnvironmentError("Weather API Key not found!")