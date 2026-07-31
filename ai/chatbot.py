def ask_gemini(message):

    msg = message.lower()

    if any(word in msg for word in ["sad", "depressed", "alone", "cry", "hopeless"]):
        return (
            "I'm sorry you're feeling this way. ❤️ "
            "Try talking to someone you trust, take some rest, "
            "and remember that difficult feelings can improve with support."
        )

    elif any(word in msg for word in ["stress", "exam", "pressure", "anxiety"]):
        return (
            "It sounds like you're under stress. "
            "Take a short break, drink some water, "
            "and try completing one small task at a time."
        )

    elif any(word in msg for word in ["happy", "good", "great", "fine"]):
        return (
            "That's wonderful to hear! 😊 "
            "Keep doing the things that make you feel positive."
        )

    elif any(word in msg for word in ["hello", "hi", "hey"]):
        return (
            "Hello! 👋 I'm MindSense AI. "
            "How are you feeling today?"
        )

    else:
        return (
            "Thank you for sharing. 💙 "
            "I'm here to listen. "
            "Can you tell me a little more about how you're feeling?"
        )