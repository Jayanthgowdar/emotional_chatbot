import os
from regex_agent import regex_response
from fsm_manager import FSMManager, ChatState
from emotion_detector import load_nrc_lexicon, detect_emotions
from lang_identifier import detect_language

def run_chat():
    fsm = FSMManager()

    # Load NRC Emotion Lexicon
    lexicon_path = os.path.join("..", "data", "NRC-Emotion-Lexicon-Wordlevel-v0.92.txt")
    nrc_lexicon = load_nrc_lexicon(lexicon_path)

    print("Emotional Support Bot:", fsm.next_state(""))  # initial greeting

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Emotional Support Bot: Take care. Remember, I'm always here to listen. 💛")
            break

        # 🔍 Language Detection
        language = detect_language(user_input)

        if language == "hi":
            print("Emotional Support Bot: मुझे समझ आ रहा है कि आप कैसा महसूस कर रहे हैं। मैं आपकी मदद करने के लिए यहाँ हूँ।")
        elif language == "unknown":
            print("Emotional Support Bot: I'm having trouble understanding the language. Could you rephrase that?")
            continue  # skip further processing for this turn

        # 🔄 FSM Response
        state_response = fsm.next_state(user_input)

        if state_response:
            print("Emotional Support Bot:", state_response)
        else:
            # Emotion Detection with NRC
            emotions = detect_emotions(user_input, nrc_lexicon)
            if emotions:
                top_emotion = emotions[0][0]
                if top_emotion != emotion:  # optionally compare if using both
                    print(f"Emotional Support Bot: I sense you're feeling {top_emotion}.")
            else:
                print("Emotional Support Bot: I'm trying to understand how you feel.")

            # 💬 Regex-based emotional response
            print("Emotional Support Bot:", regex_response(user_input))

if __name__ == "__main__":
    run_chat()
