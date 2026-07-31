from flask import Blueprint, session, redirect, url_for, send_file
from io import BytesIO

from models.user import User
from models.journal import Journal
from models.social import Social

from utils.pdf_generator import generate_pdf

report = Blueprint("report", __name__)


@report.route("/download_report")
def download_report():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    user = User.query.get(session["user_id"])

    journals = Journal.query.filter_by(
        user_id=session["user_id"]
    ).order_by(
        Journal.created_at.desc()
    ).all()

    social_history = Social.query.filter_by(
        user_id=session["user_id"]
    ).order_by(
        Social.created_at.desc()
    ).all()

    pdf = generate_pdf(
        user.name,
        journals,
        social_history
    )

    return send_file(
        BytesIO(pdf),
        as_attachment=True,
        download_name="MindSense_Report.pdf",
        mimetype="application/pdf"
    )