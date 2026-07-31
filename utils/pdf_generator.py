from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO


def generate_pdf(user_name, journals, social_history):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>MindSense AI Report</b>", styles["Title"]))

    story.append(Paragraph(f"User : {user_name}", styles["Heading2"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Journal Entries</b>", styles["Heading2"]))

    for j in journals:

        story.append(
            Paragraph(
                f"""
                <b>Date:</b> {j.created_at}<br/>
                <b>Mood:</b> {j.mood}<br/>
                <b>Sentiment:</b> {j.sentiment}<br/>
                <b>Journal:</b> {j.journal}<br/><br/>
                """,
                styles["BodyText"]
            )
        )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>Social Media Analysis</b>", styles["Heading2"]))

    for s in social_history:

        story.append(
            Paragraph(
                f"""
                <b>Date:</b> {s.created_at}<br/>
                <b>Sentiment:</b> {s.sentiment}<br/>
                <b>Emotion:</b> {s.emotion}<br/>
                <b>Risk:</b> {s.risk}<br/>
                <b>Prediction:</b> {s.prediction}<br/>
                <b>Confidence:</b> {s.confidence}%<br/><br/>
                """,
                styles["BodyText"]
            )
        )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf