import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("dataset/depression_dataset_reddit_cleaned.csv")

print(df.head())

# Features
X = df["clean_text"]

# Labels
y = df["is_depression"]

# TF-IDF
vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

X = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Accuracy
pred = model.predict(X_test)

print("Accuracy :", accuracy_score(y_test, pred))

# Save Model
joblib.dump(model, "ai/model.pkl")
joblib.dump(vectorizer, "ai/vectorizer.pkl")

print("✅ Model Saved Successfully")
print("✅ Vectorizer Saved Successfully")