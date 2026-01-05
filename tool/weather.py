"""
Weather Tool using OpenWeatherMap API
"""

import requests

from langchain.tools import tool

from cred import WEATHER_API_KEY


@tool
def get_weather(city: str) -> dict:
    """
    Fetches live weather data for a city.
    """
    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
        )
        response = requests.get(url)
        data = response.json()

        return {
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }
    except Exception as e:
        return {"error": str(e)}
