import re
from wordnet_helper import contains_emotion
from deep_emotion import detect_deep_emotion

class ChatState:
    GREETING = "GREETING"
    ASK_EMOTION = "ASK_EMOTION"
    RESPOND_EMOTION = "RESPOND_EMOTION"
    CLOSING = "CLOSING"

class FSMManager:
    def __init__(self):
        self.state = ChatState.GREETING

    def next_state(self, user_input):
        user_input = user_input.lower()

        if self.state == ChatState.GREETING:
            self.state = ChatState.ASK_EMOTION
            return "Hello! I'm here for you. How are you feeling today?"

        elif self.state == ChatState.ASK_EMOTION:
            # Use deep emotion model
            deep_emotion, confidence = detect_deep_emotion(user_input)
            if deep_emotion != "unknown" and confidence > 0.3:
                self.state = ChatState.RESPOND_EMOTION
                return None

            # Fallback to keyword-based emotion detection
            if contains_emotion(user_input):
                self.state = ChatState.RESPOND_EMOTION
                return None

            return "I'm listening. Can you tell me how you're feeling in a word?"

        elif self.state == ChatState.RESPOND_EMOTION:
            # Exit-related
            if any(re.search(rf"\b{word}\b", user_input) for word in ["bye", "goodbye", "exit", "quit"]):
                self.state = ChatState.CLOSING
                return "Take care. Remember, I'm always here to listen. 💛"

            # Negative response
            elif any(re.search(rf"\b{word}\b", user_input) for word in ["no", "nah", "nothing", "none"]):
                self.state = ChatState.CLOSING
                return "That's okay. You're always welcome to come back and talk. 😊"

            # Fun or upbeat phrases
            elif any(word in user_input for word in ["dance", "sing", "music", "move", "party"]):
                return "Sounds like you're in a lively mood! 🎶💃🕺"

            # Small talk
            elif any(phrase in user_input for phrase in ["how are you", "what about you"]):
                return "Thanks for asking! I'm just a bot, but I'm happy to be here for you. 😊"

            # Fallback
            else:
                return "Is there anything else on your mind?"

        elif self.state == ChatState.CLOSING:
            return "Goodbye!"

        return "I'm not sure what to say."
