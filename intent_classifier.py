import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# 🚀 Train the model
def train_intent_model(csv_path="data/intent_dataset.csv"):
    df = pd.read_csv(csv_path)
    X = df["text"]
    y = df["intent"]

    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    model.fit(X, y)
    joblib.dump(model, "src/intent_model.joblib")
    print("✅ Trained and saved intent_model.joblib")
    return model

# 🧠 Load the trained model
def load_intent_model():
    return joblib.load("src/intent_model.joblib")

# 🔍 Predict the intent for a new input
def predict_intent(text, model):
    return model.predict([text])[0]
