from nltk.corpus import wordnet
import re

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().lower())
    return list(synonyms)

# Base emotion categories (manually extended with critical emotion words)
emotion_keywords = {
    "sad": ["sad", "unhappy", "depressed", "down", "miserable"],
    "happy": ["happy", "excited", "joyful", "glad", "cheerful"],
    "angry": ["angry", "mad", "frustrated", "furious", "enraged"],
    "anxious": ["anxious", "nervous", "worried", "scared", "uneasy"],
    "okay": ["good", "fine", "okay", "well"]
}


# Expand emotion keywords with synonyms
# Expand emotion keywords with synonyms
for emotion, words in emotion_keywords.items():
    expanded = set(words)
    for word in words:
        expanded.update(get_synonyms(word))
    emotion_keywords[emotion] = list(expanded)


def contains_emotion(text):
    text = text.lower()
    print(f"[DEBUG] Checking for emotion in: {text}")  # Add this line

    for emotion, keywords in emotion_keywords.items():
        for kw in keywords:
            if re.search(rf"\b{kw}\b", text):
                print(f"[DEBUG] Matched keyword: {kw} for emotion: {emotion}")  # Add this
                return emotion
    print("[DEBUG] No emotion detected.")  # Add this
    return None

