import os

def load_nrc_lexicon(filepath):
    lexicon = {}
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            word, emotion, association = line.strip().split('\t')
            if int(association) == 1:
                if word not in lexicon:
                    lexicon[word] = []
                lexicon[word].append(emotion)
    return lexicon

def detect_emotions(text, lexicon):
    emotions_found = {}
    words = text.lower().split()

    for word in words:
        if word in lexicon:
            for emotion in lexicon[word]:
                emotions_found[emotion] = emotions_found.get(emotion, 0) + 1

    return sorted(emotions_found.items(), key=lambda x: x[1], reverse=True)
