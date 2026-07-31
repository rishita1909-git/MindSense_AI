from database.db import db
from datetime import datetime


class Journal(db.Model):

    __tablename__ = "journal"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        nullable=False
    )

    mood = db.Column(
        db.String(30),
        nullable=False
    )

    journal = db.Column(
        db.Text,
        nullable=False
    )

    sentiment = db.Column(
        db.String(20),
        nullable=False
    )

    # AI Prediction
    prediction = db.Column(
        db.String(50),
        nullable=True
    )

    confidence = db.Column(
        db.Float,
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )