from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
from datetime import datetime
import os

app = Flask(__name__)

# ================= Paths & folders =================
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

LOG_FILE = "predictions_log.csv"

# ================= Load ML artifacts =================
model = joblib.load("artifacts/best_model.pkl")
scaler = joblib.load("artifacts/scaler.pkl")
feature_columns = joblib.load("artifacts/feature_columns.pkl")

HISTORY_COLUMNS = [
    "timestamp",
    "annual_income",
    "debt_to_income_ratio",
    "credit_score",
    "loan_amount",
    "interest_rate",
    "gender",
    "marital_status",
    "education_level",
    "employment_status",
    "loan_purpose",
    "grade_subgrade",
    "prediction",
    "probability"
]

# ================= Helper: preprocess =================
def preprocess(df: pd.DataFrame):
    encoded = pd.get_dummies(df)
    encoded = encoded.reindex(columns=feature_columns, fill_value=0)
    scaled = scaler.transform(encoded)
    return scaled

# ================= Home =================
@app.route("/")
def home():
    return render_template("index.html")

# ================= Single Prediction =================
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    df = pd.DataFrame([data])

    X = preprocess(df)
    prob = model.predict_proba(X)[0][1]
    prediction = "Will Pay Back" if prob >= 0.5 else "Will NOT Pay Back"

    log_entry = {
        "timestamp": datetime.now().isoformat(),
        **data,
        "prediction": prediction,
        "probability": round(prob, 4)
    }

    pd.DataFrame([log_entry], columns=HISTORY_COLUMNS).to_csv(
        LOG_FILE,
        mode="a",
        header=not os.path.exists(LOG_FILE),
        index=False
    )

    return jsonify({
        "prediction": prediction,
        "probability": round(prob, 4)
    })

# ================= Batch Upload Page =================
@app.route("/batch")
def batch_page():
    return render_template("batch.html")

# ================= Batch Prediction (UI) =================
@app.route("/predict-batch-ui", methods=["POST"])
def predict_batch_ui():
    if "file" not in request.files:
        return "No file uploaded", 400

    file = request.files["file"]
    if file.filename == "":
        return "Empty filename", 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    df = pd.read_csv(filepath)

    required_columns = [
        "annual_income",
        "debt_to_income_ratio",
        "credit_score",
        "loan_amount",
        "interest_rate",
        "gender",
        "marital_status",
        "education_level",
        "employment_status",
        "loan_purpose",
        "grade_subgrade"
    ]

    missing = [c for c in required_columns if c not in df.columns]
    if missing:
        return f"Missing columns: {missing}", 400

    X = preprocess(df)
    probs = model.predict_proba(X)[:, 1]
    preds = ["Will Pay Back" if p >= 0.5 else "Will NOT Pay Back" for p in probs]

    results = df.copy()
    results["prediction"] = preds
    results["probability"] = probs.round(4)
    results["timestamp"] = datetime.now().isoformat()

    # Save all rows to history
    results[HISTORY_COLUMNS].to_csv(
        LOG_FILE,
        mode="a",
        header=not os.path.exists(LOG_FILE),
        index=False
    )

    return render_template(
        "batch_results.html",
        results=results.to_dict(orient="records")
    )

# ================= History =================
@app.route("/history")
def history():
    if not os.path.exists(LOG_FILE):
        return render_template("history.html", records=None)

    df = pd.read_csv(LOG_FILE)
    return render_template(
        "history.html",
        records=df.to_dict(orient="records")
    )

# ================= Run =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
