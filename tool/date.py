"""
Date Utility Tool
Calculates future dates.
"""

from datetime import datetime, timedelta

from langchain.tools import tool

# for getting the future date
@tool
def future_date(days: int) -> str:
    """
    Summary:
        Calculate the date after a given number of days from today.

    Args:
        days (int): Number of days to add to the current date.

    Returns:
        str: Future date in YYYY-MM-DD format, or an error message if calculation fails.
    """
    try:
        target_date = datetime.today() + timedelta(days=days)
        return target_date.strftime("%Y-%m-%d")
    except Exception as e:
        return f"Error calculating date: {str(e)}"
