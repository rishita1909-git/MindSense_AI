from textblob import TextBlob


def analyze_social(text):

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.2:
        sentiment = "Positive"
    elif polarity < -0.2:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    t = text.lower()

    if any(word in t for word in [
        "happy", "great", "excited", "love", "awesome"
    ]):
        emotion = "Happy 😊"

    elif any(word in t for word in [
        "sad", "cry", "alone", "depressed", "lonely"
    ]):
        emotion = "Sad 😔"

    elif any(word in t for word in [
        "angry", "hate", "furious"
    ]):
        emotion = "Angry 😡"

    elif any(word in t for word in [
        "stress", "anxiety", "exam", "pressure"
    ]):
        emotion = "Stressed 😣"

    else:
        emotion = "Neutral 😐"

    risk_words = [
        "suicide",
        "die",
        "kill myself",
        "worthless",
        "hopeless"
    ]

    if any(word in t for word in risk_words):
        risk = "High ⚠"

    elif sentiment == "Negative":
        risk = "Medium"

    else:
        risk = "Low"

    return sentiment, emotion, risk