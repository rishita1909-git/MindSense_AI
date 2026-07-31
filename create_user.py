from app import app
from database.db import db
from models.user import User
from werkzeug.security import generate_password_hash

with app.app_context():

    user = User(
        name="Test User",
        email="test@gmail.com",
        password=generate_password_hash("123456")
    )

    db.session.add(user)
    db.session.commit()

    print("✅ User Created Successfully")