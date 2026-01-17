from fastapi import FastAPI, UploadFile, File
import pandas as pd
from review_analyzer import analyze_text_similarity
from network_detector import detect_review_networks

app = FastAPI(title="ReviewNetX")

@app.post("/analyze")
async def analyze_reviews(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    # Text similarity risk
    text_risks = analyze_text_similarity(df)
    df["risk_score"] = text_risks
    df["flag_reason"] = ""

    # Network detection
    suspicious_users = detect_review_networks(df)

    for i, row in df.iterrows():
        reasons = []
        if row["risk_score"] > 0.6:
            reasons.append("High text similarity")

        if f"user_{row['user']}" in suspicious_users:
            reasons.append("Part of review network")

        df.at[i, "flag_reason"] = ", ".join(reasons)

    return df.to_dict(orient="records")
