import os

from dotenv import load_dotenv

# Loading environment variable
load_dotenv()

# Getting gemini api key
gemini_api_key = os.getenv("GEMINI_API_KEY", "")

if not gemini_api_key:
    raise EnvironmentError("Gemini API Key is not found.")