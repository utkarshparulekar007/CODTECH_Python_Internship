import nltk
import string
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# Knowledge Base
# -------------------------------
corpus = [
    "Python is a programming language.",
    "NLP stands for Natural Language Processing.",
    "Chatbots are programs that communicate with users.",
    "Machine learning is a subset of artificial intelligence.",
    "NLTK is a Python library for natural language processing."
]

lemmatizer = WordNetLemmatizer()

# -------------------------------
# Text Cleaning
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(text)
    return [lemmatizer.lemmatize(word) for word in tokens]

# -------------------------------
# Intent-based Responses (FIX)
# -------------------------------
def intent_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    if "python" in user_input:
        return "Python is a popular programming language."

    if "nlp" in user_input:
        return "NLP means Natural Language Processing."

    if "chatbot" in user_input:
        return "A chatbot is a program that chats with humans."

    if "machine learning" in user_input:
        return "Machine learning is a part of artificial intelligence."

    return None

# -------------------------------
# NLP Fallback Response
# -------------------------------
def nlp_response(user_input):
    sentences = corpus + [user_input]

    vectorizer = TfidfVectorizer(tokenizer=clean_text)
    vectors = vectorizer.fit_transform(sentences)

    similarity = cosine_similarity(vectors[-1], vectors[:-1])
    index = similarity.argmax()

    if similarity[0][index] < 0.2:
        return "Sorry, I am still learning. Can you rephrase?"

    return corpus[index]

# -------------------------------
# Chat Loop
# -------------------------------
print("Chatbot: Hello! Type 'bye' to exit.\n")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    # 1️⃣ Try intent match first
    reply = intent_response(user)

    # 2️⃣ If no intent matched, use NLP
    if reply is None:
        reply = nlp_response(user)

    print("Chatbot:", reply)
