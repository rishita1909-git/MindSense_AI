from flask import Blueprint, render_template, request, session, redirect, url_for

from database.db import db
from models.social import Social

from ai.sentiment import analyze_sentiment
from ai.predict import predict_depression

social = Blueprint("social", __name__)


# ================= Social Media Analysis =================

@social.route("/social", methods=["GET", "POST"])
def social_page():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    result = None

    if request.method == "POST":

        text = request.form.get("text")

        # ---------------- Sentiment ----------------
        sentiment = analyze_sentiment(text)

        # ---------------- Emotion ----------------
        text_lower = text.lower()

        if any(word in text_lower for word in [
            "happy", "great", "awesome", "excited", "love", "good"
        ]):
            emotion = "Happy 😊"

        elif any(word in text_lower for word in [
            "sad", "cry", "depressed", "alone", "hopeless"
        ]):
            emotion = "Sad 😔"

        elif any(word in text_lower for word in [
            "angry", "hate", "annoyed", "furious"
        ]):
            emotion = "Angry 😡"

        elif any(word in text_lower for word in [
            "stress", "anxiety", "worried", "pressure"
        ]):
            emotion = "Stressed 😣"

        else:
            emotion = "Neutral 😐"

        # ---------------- ML Prediction ----------------
        prediction, confidence = predict_depression(text)

        # ---------------- Risk ----------------
        if prediction == "Depressed":
            risk = "High Risk 🔴"
        else:
            risk = "Low Risk 🟢"

        # ---------------- Save Database ----------------
        social_data = Social(

            user_id=session["user_id"],

            text=text,

            sentiment=sentiment,

            emotion=emotion,

            risk=risk,

            prediction=prediction,

            confidence=confidence

        )

        db.session.add(social_data)
        db.session.commit()

        result = {

            "sentiment": sentiment,

            "emotion": emotion,

            "risk": risk,

            "prediction": prediction,

            "confidence": round(confidence, 2)

        }

    history = Social.query.filter_by(
        user_id=session["user_id"]
    ).order_by(
        Social.created_at.desc()
    ).all()

    return render_template(

        "social/social.html",

        result=result,

        history=history

    )