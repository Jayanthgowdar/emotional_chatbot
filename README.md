# 🤖 Emotional Support Chatbot

Welcome to the Emotional Support Chatbot – a Streamlit-based AI chatbot designed to provide users with a comforting, empathetic, and supportive conversational experience.

---

## 🌟 Features

- 🧠 Powered by OpenAI's GPT-3.5 for natural, empathetic dialogue
- 🎙️ Text-to-speech using `pyttsx3`
- 🧩 NLP processing using `NLTK` and `regex`
- 📊 POS Tagging, N-gram generation, Morphological Analysis
- 🎯 Regex-based emotional pattern recognition
- 🔄 Finite-State Automaton (FSA) for dialogue management

---

## 🛠️ Tech Stack

| Tool | Description |
|------|-------------|
| **Streamlit** | For creating a responsive web UI |
| **OpenAI GPT-3.5** | For conversational response generation |
| **NLTK** | For POS tagging, parsing, tokenization, morphology |
| **pyttsx3** | For speech synthesis |
| **Regex** | For pattern-based dialogue |
| **Joblib** | For loading trained intent classification models |

---

## 📂 Folder Structure

```
emotional-chatbot/
├── src/
│   ├── chatbot_app.py              # Main Streamlit app
│   ├── intent_classifier.py        # Intent classification logic
│   ├── emotion_detector.py         # Emotion recognition using NRC
│   ├── regex_agent.py              # Regex dialogue agent
│   ├── toxic_filter.py             # Toxic content filtering
│   ├── fsm_manager.py              # Finite-State Automaton manager
│   ├── wordnet_helper.py           # WordNet integration
│   ├── lang_identifier.py          # Language detection (if used)
│   └── deep_emotion.py             # Deep learning placeholder (optional)
├── nltk_data/                      # Locally downloaded NLTK files
├── requirements.txt                # Python dependencies
├── intent_model.joblib             # Trained intent classifier
├── intent_dataset.csv              # Dataset for intent classification
├── NRC-Emotion-Lexicon-Wordlevel-v0.92.txt  # NRC Emotion Lexicon
└── README.md                       # You're here!
```

---

## 🧪 How to Run

### 🖥️ 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/emotional_chatbot.git
cd emotional_chatbot
```

### 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure you also have `nltk_data`. If not, run:

```python
# In Python shell
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

### 🔑 3. Set Your OpenAI API Key

Create a `.env` file or set an environment variable:

```bash
export OPENAI_API_KEY="sk-...your_key..."
```

### 🚀 4. Run the Chatbot

```bash
streamlit run src/chatbot_app.py
```

---

## 📌 Tasks Covered

- ✅ Regex Dialogue Agent
- ✅ POS Tagging
- ✅ N-gram Language Modeling
- ✅ Morphological Analysis & Synthesis
- ✅ Text Parsing
- ✅ Finite-State Automaton
- ✅ Speech Synthesis
- ✅ Vector Semantics (Word2Vec/GloVe)
- ✅ Emotion Detection via NRC Lexicon

---

## 📄 License

This project is intended for educational purposes only and is not a substitute for professional mental health support.

---

## 🙋‍♂️ Authors

- Jayanth Gowda R
- [Western Michigan University | CS 6030 - NLP Project Group]
