# 🕸️ ReviewNetX – AI-Based Fake Review Network Detection

ReviewNetX is an AI-powered system that detects **fake reviews and coordinated review networks** using
text similarity analysis and graph-based behavior modeling.

Built as a **hackathon MVP**, the project focuses on explainability, simplicity, and real-world applicability
for e-commerce and review platforms.

---

## 🚀 Features

- 📂 Upload CSV review data
- 🧠 Detect similar / copy-paste reviews using NLP
- 🕸️ Identify fake review rings using network graph analysis
- ⚠️ Assign risk scores to each review
- 📊 Visual dashboard highlighting suspicious reviews

---

## 🏗️ Tech Stack

### Backend
- FastAPI
- Python
- Pandas
- Scikit-learn
- NetworkX

### Frontend
- HTML
- CSS
- JavaScript

---

## 📁 Project Structure

reviewnetx/
│
├── backend/
│ ├── main.py
│ ├── review_analyzer.py
│ ├── network_detector.py
│ ├── database.py
│ ├── models.py
│ └── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── app.js
│ └── style.css
│
├── sample_data/
│ └── reviews.csv
│
└── README.md

yaml
Copy code

---


🎯 Use Cases
E-commerce fake review detection

Marketplace trust & safety

Product review moderation

Fraud analysis systems

🏆 Hackathon Value
Real-world problem

Explainable AI approach

Scalable architecture

Strong demo visualization

📌 Future Improvements
Database persistence

User behavior timeline analysis

Advanced NLP models (BERT)

Real-time review ingestion

Graph visualization UI
