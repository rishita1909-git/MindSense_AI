import joblib
import os

BASE_DIR = os.path.dirname(__file__)

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))


def predict_depression(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)[0]
    probability = model.predict_proba(text_vector)[0][1]

    if prediction == 1:
        label = "Depressed 😔"
    else:
        label = "Not Depressed 😊"

    return label, round(probability * 100, 2)