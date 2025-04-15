import re
from wordnet_helper import emotion_keywords

def regex_response(user_input):
    user_input = user_input.lower()

    for emotion, keywords in emotion_keywords.items():
        for kw in keywords:
            if re.search(rf"\b{kw}\b", user_input):
                if emotion == "sad":
                    return "I'm really sorry you're feeling this way. Want to talk about it?"
                elif emotion == "happy":
                    return "That's wonderful! Tell me more!"
                elif emotion == "angry":
                    return "It's okay to feel this way. Want to share what's bothering you?"
                elif emotion == "anxious":
                    return "That sounds stressful. I'm here for you."
                elif emotion == "okay":
                    return "I'm glad to hear that. Still, I'm here if you want to talk!"
    
    return "I'm here to listen. Please, go on."
