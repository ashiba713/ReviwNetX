from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def analyze_text_similarity(df):
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(df["text"])

    similarity_matrix = cosine_similarity(tfidf)
    risk_scores = []

    for i in range(len(df)):
        similar_count = (similarity_matrix[i] > 0.85).sum()
        risk = min(similar_count / 5, 1.0)
        risk_scores.append(risk)

    return risk_scores
