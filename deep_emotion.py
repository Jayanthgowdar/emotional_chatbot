from transformers import pipeline

# Load model only once
emotion_model = pipeline("text-classification", 
                         model="j-hartmann/emotion-english-distilroberta-base", 
                         top_k=1)

def detect_deep_emotion(text):
    try:
        result = emotion_model(text)
        emotion = result[0][0]["label"]
        score = result[0][0]["score"]
        return emotion, score
    except Exception as e:
        return "unknown", 0.0
