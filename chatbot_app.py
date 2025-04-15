import streamlit as st
import openai
import pyttsx3  # For Speech Synthesis
import threading
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
from datetime import datetime
from nltk.util import ngrams
from nltk import pos_tag
import re
import os

# Set up local download path for NLTK
nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

nltk.data.path.append(nltk_data_path)

# Download necessary resources locally
nltk_packages = ['punkt', 'averaged_perceptron_tagger', 'wordnet', 'omw-1.4']
for pkg in nltk_packages:
    try:
        nltk.data.find(f'tokenizers/{pkg}' if pkg == 'punkt' else f'corpora/{pkg}')
    except LookupError:
        nltk.download(pkg, download_dir=nltk_data_path)

# Initialize OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Replace with your OpenAI API Key

# Initialize speech engine
def speak(text):
    """Function to speak the given text using pyttsx3."""
    engine = pyttsx3.init()  # Initialize a new engine instance each time
    engine.setProperty('rate', 150)
    engine.say(text)
    try:
        engine.runAndWait()
    except RuntimeError:
        pass  # Ignore the RuntimeError caused by multiple calls


def generate_ngrams(text, n):
    words = word_tokenize(text)
    return list(ngrams(words, n))


def perform_pos_tagging(text):
    words = word_tokenize(text)
    return pos_tag(words)


def regex_match(text):
    if re.search(r'\b(sad|depressed|unhappy|angry)\b', text.lower()):
        return "I'm sorry you're feeling that way. Would you like to talk more about it?"
    return None


def morphological_analysis(word):
    suffixes = ['ing', 'ed', 's', 'es', 'er', 'est', 'ly']
    base_word = word
    for suffix in suffixes:
        if word.endswith(suffix):
            base_word = word[: -len(suffix)]
            break
    return base_word


def morphological_synthesis(base_word, suffix):
    return base_word + suffix


# Page configuration
st.set_page_config(page_title="Emotional Support Chatbot", page_icon="💬", layout="wide")

# Styling the app
st.markdown("""
    <style>
        .stTextInput > div > input {
            font-size: 18px;
            padding: 10px;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border-radius: 4px;
            border: none;
        }
        .stMarkdown {
            font-size: 16px;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Emotional Support Chatbot")
st.markdown("Feel free to share what's on your mind. I'm here to listen.")

# Initialize conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

# Display chat history
def display_history():
    for chat in st.session_state.history:
        if chat["role"] == "user":
            st.markdown(f"🧑 You: {chat['content']}")
        else:
            st.markdown(f"🤖 Bot: {chat['content']}")

display_history()

# User input box
user_input = st.text_input("Type your message here:")

if st.button("Send") and user_input.strip() != "":
    # Display user message
    st.session_state.history.append({"role": "user", "content": user_input})

    # Regex Matching
    regex_response = regex_match(user_input)
    if regex_response:
        bot_reply = regex_response
    else:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a compassionate therapist who provides emotional support."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=150,
                temperature=0.7,
            )

            bot_reply = response['choices'][0]['message']['content']

        except Exception as e:
            bot_reply = f"Error using OpenAI API: {e}"

    st.session_state.history.append({"role": "assistant", "content": bot_reply})

    # Trigger speech synthesis
    speak_thread = threading.Thread(target=speak, args=(bot_reply,))
    speak_thread.start()

    # Display updated chat history
    display_history()

    # Display N-gram Analysis
    unigrams = generate_ngrams(user_input, 1)
    bigrams = generate_ngrams(user_input, 2)
    trigrams = generate_ngrams(user_input, 3)

    st.write("Unigrams:", unigrams)
    st.write("Bigrams:", bigrams)
    st.write("Trigrams:", trigrams)

    # Display POS Tags
    pos_tags = perform_pos_tagging(user_input)
    st.write("POS Tags:", pos_tags)

    # Display Morphological Analysis
    word_list = word_tokenize(user_input)
    base_words = {word: morphological_analysis(word) for word in word_list}
    st.write("Morphological Analysis:", base_words)

    # Example Morphological Synthesis
    st.write("Example Morphological Synthesis:", morphological_synthesis('walk', 'ing'))
