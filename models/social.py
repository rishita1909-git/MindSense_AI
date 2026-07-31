from database.db import db
from datetime import datetime


class Social(db.Model):

    __tablename__ = "social"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, nullable=False)

    text = db.Column(db.Text, nullable=False)

    sentiment = db.Column(db.String(50))

    emotion = db.Column(db.String(50))

    risk = db.Column(db.String(50))

    prediction = db.Column(db.String(50))

    confidence = db.Column(db.Float)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )