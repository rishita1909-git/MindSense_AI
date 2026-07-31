from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from database.db import db
from models.journal import Journal
from ai.sentiment import analyze_sentiment
from ai.chatbot import ask_gemini
from ai.predict import predict_depression

from collections import Counter

dashboard = Blueprint("dashboard", __name__)


# ================= Dashboard =================

@dashboard.route("/dashboard")
def home():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    journals = Journal.query.filter_by(
        user_id=session["user_id"]
    ).order_by(
        Journal.created_at.desc()
    ).all()

    # ---------------- Mood Count ----------------

    mood_count = {
        "Happy 😊": 0,
        "Sad 😔": 0,
        "Angry 😡": 0,
        "Stressed 😣": 0,
        "Excited 😄": 0
    }

    for j in journals:
        if j.mood in mood_count:
            mood_count[j.mood] += 1

    # ---------------- Statistics ----------------

    total_entries = len(journals)

    latest_entry = (
        journals[0].created_at.strftime("%d %b %Y")
        if journals else "No Entries"
    )

    most_common_mood = (
        Counter([j.mood for j in journals]).most_common(1)[0][0]
        if journals else "No Mood"
    )

    # ---------------- Weekly Chart ----------------

    chart_labels = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    chart_values = [0, 0, 0, 0, 0, 0, 0]

    for j in journals:
        day = j.created_at.weekday()  # Monday = 0
        chart_values[day] += 1

    return render_template(
        "dashboard.html",
        name=session.get("user_name"),
        mood_count=mood_count,
        total_entries=total_entries,
        latest_entry=latest_entry,
        most_common_mood=most_common_mood,
        chart_labels=chart_labels,
        chart_values=chart_values
    )

# ================= Journal =================

@dashboard.route("/journal", methods=["GET", "POST"])
def journal():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    prediction = None
    confidence = None

    if request.method == "POST":

        mood = request.form.get("mood")
        text = request.form.get("journal")

        sentiment = analyze_sentiment(text)

        # ML Prediction
        prediction, confidence = predict_depression(text)

        entry = Journal(
            user_id=session["user_id"],
            mood=mood,
            journal=text,
            sentiment=sentiment
        )

        db.session.add(entry)
        db.session.commit()

        flash(
            f"Journal Saved! AI Prediction: {prediction} ({confidence}%)",
            "success"
        )

        journals = Journal.query.filter_by(
            user_id=session["user_id"]
        ).order_by(
            Journal.created_at.desc()
        ).all()

        return render_template(
            "journal/journal.html",
            journals=journals,
            prediction=prediction,
            confidence=confidence
        )

    journals = Journal.query.filter_by(
        user_id=session["user_id"]
    ).order_by(
        Journal.created_at.desc()
    ).all()

    return render_template(
        "journal/journal.html",
        journals=journals,
        prediction=prediction,
        confidence=confidence
    )

# ================= AI Chatbot =================

@dashboard.route("/chatbot", methods=["GET", "POST"])
def chatbot():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if "chat_history" not in session:
        session["chat_history"] = []

    if request.method == "POST":

        user_message = request.form.get("message")

        if user_message:

            ai_response = ask_gemini(user_message)

            history = session["chat_history"]

            history.append({
                "user": user_message,
                "ai": ai_response
            })

            session["chat_history"] = history

    return render_template(
        "chatbot/chatbot.html",
        chat_history=session["chat_history"]
    )

@dashboard.route("/clear_chat")
def clear_chat():

    session.pop("chat_history", None)

    return redirect(url_for("dashboard.chatbot"))

# ================= Face Detection =================

@dashboard.route("/face")
def face():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template("coming_soon.html", feature="Face Detection")


@dashboard.route("/voice")
def voice():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template("coming_soon.html", feature="Voice Analysis")

# ================= Settings =================

@dashboard.route("/settings")
def settings():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("settings/settings.html")