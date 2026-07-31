from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

from models import user
from models.user import User
from database.db import db

auth = Blueprint("auth", __name__)

# ---------------- REGISTER ----------------
@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash("Email already registered", "danger")
            return redirect(url_for("auth.register"))

        hashed_password = generate_password_hash(password)

        user = User(
            name=name,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration Successful! Please Login.", "success")

        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


# ---------------- LOGIN ----------------
@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        print("Email:", email)
        print("Password:", password)

        user = User.query.filter_by(email=email).first()

        print("User Found:", user)

        if user:
            print("ID:", user.id)
            print("Email:", user.email)
            print("Stored Hash:", user.password)
            print("Hash OK:", check_password_hash(user.password, password))

        if user and check_password_hash(user.password, password):

            print("✅ Login Successful")

            session["user_id"] = user.id
            session["user_name"] = user.name

            print("Session:", session)

            return redirect(url_for("dashboard.home"))

        print("❌ Login Failed")
        flash("Invalid Email or Password", "danger")

    return render_template("auth/login.html")