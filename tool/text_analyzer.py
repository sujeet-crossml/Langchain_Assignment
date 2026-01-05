"""
Text Analyzer Tool
Provides word count, character count, and basic sentiment.
"""

from langchain.tools import tool


@tool
def analyze_text(text: str) -> dict:
    """
Summary:
    Analyze text to compute basic statistics and sentiment.

Args:
    text (str): Input text to be analyzed.

Returns:
    dict: A dictionary containing word count, character count,
          and sentiment, or an error message if analysis fails.
"""
    try:
        words = text.split()
        char_count = len(text)

        positive_words = ["good", "great", "excellent", "happy", "love"]
        negative_words = ["bad", "poor", "sad", "hate", "terrible"]

        sentiment_score = 0
        for word in words:
            if word.lower() in positive_words:
                sentiment_score += 1
            elif word.lower() in negative_words:
                sentiment_score -= 1

        sentiment = "Neutral"
        if sentiment_score > 0:
            sentiment = "Positive"
        elif sentiment_score < 0:
            sentiment = "Negative"

        return {
            "word_count": len(words),
            "character_count": char_count,
            "sentiment": sentiment
        }

    except Exception as e:
        return {"error": str(e)}