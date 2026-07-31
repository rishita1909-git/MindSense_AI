from flask import Flask, render_template, session, redirect, url_for

from database.db import db
from routes.report import report
# Import Routes
from routes.auth import auth
from routes.dashboard import dashboard
from routes.social import social

# Create Flask App
app = Flask(__name__, template_folder="templates")

# Secret Key
app.config["SECRET_KEY"] = "mindsense_ai_secret_key"

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Database
db.init_app(app)

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(social)
app.register_blueprint(report)
# Home Page
@app.route("/")
def home():
    return render_template("home/index.html")


@app.route("/hello")
def hello():
    return "HELLO"


# Logout
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))


# Create Database Tables
with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully")


if __name__ == "__main__":
    app.run(debug=True)