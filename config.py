import os

# Flask Secret Key
SECRET_KEY = os.getenv("SECRET_KEY", "mindsense_secret_key")

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")

# Database
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False