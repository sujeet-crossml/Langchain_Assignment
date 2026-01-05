"""
Date Utility Tool
Calculates future dates.
"""

from datetime import datetime, timedelta

from langchain.tools import tool


@tool
def future_date(days: int) -> str:
    """
    Returns date after N days from today.
    """
    try:
        target_date = datetime.today() + timedelta(days=days)
        return target_date.strftime("%Y-%m-%d")
    except Exception as e:
        return f"Error calculating date: {str(e)}"
