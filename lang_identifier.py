from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0  # makes detection consistent

def detect_language(text):
    try:
        lang = detect(text)
        return lang  # e.g., 'en', 'hi'
    except:
        return "unknown"
