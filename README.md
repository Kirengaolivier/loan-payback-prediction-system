[README.md](https://github.com/user-attachments/files/24324396/README.md)

## Loan Payback Prediction System

A full-stack machine learning web application that predicts whether a loan applicant is likely to **pay back a loan or not**, using both **single predictions** and **batch file uploads**.
The system is deployed online and accessible via a public URL.

 **Live Demo:**
 [https://loan-payback-prediction-system.onrender.com/](https://loan-payback-prediction-system.onrender.com/)

## Project Overview

The **Loan Payback Prediction System** helps financial institutions or analysts evaluate loan applicants using historical data and machine learning.
Instead of manually evaluating each applicant, the system provides:

* Instant predictions
* Probability scores
* Batch processing for large datasets
* Prediction history storage

## Features

### Single Prediction

* Enter applicant details using a form
* Get:

  * Prediction result (Will Pay Back / Will NOT Pay Back)
  * Probability score

### Batch Prediction (Bulk Upload)

* Upload a CSV file containing **multiple applicants**
* The system:

  * Generates predictions for each record
  * Displays results in a table
  * Stores all predictions in history

### Prediction History

* View all previous predictions
* Includes:

  * Input values
  * Prediction result
  * Probability
  * Timestamp

### Navigation

* Predict Loan
* Upload Batch
* View Prediction History
* Back buttons for smooth navigation

## Machine Learning Model

* **Type:** Classification model
* **Purpose:** Predict loan payback behavior
* **Outputs:**

  * Prediction label
  * Confidence probability
* Model is loaded on the backend and used by API endpoints.

## System Architecture

```
Frontend (HTML / CSS / JS)
        |
        | HTTP Requests (Fetch API)
        ↓
Backend API (Python - Flask)
        |
        | ML Inference
        ↓
Machine Learning Model
        |
        ↓
Prediction Results + History Storage
```

## Tech Stack

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask (REST API)

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Deployment

* **Render (Cloud Platform)**
* GitHub (Version Control)

## API Endpoints

| Endpoint         | Method | Description                     |
| ---------------- | ------ | ------------------------------- |
| `/predict`       | POST   | Single loan prediction          |
| `/predict-batch` | POST   | Batch prediction via CSV upload |
| `/history`       | GET    | Fetch prediction history        |

## Batch File Format (CSV)

The uploaded CSV file must contain the following columns:

```csv
annual_income,credit_score,loan_amount,loan_purpose
```

### Example:

```csv
45000,680,12000,Debt consolidation
60000,720,15000,Home
30000,610,8000,Medical
```

---

## Live Deployment

The application is deployed and publicly accessible:

 **[https://loan-payback-prediction-system.onrender.com/](https://loan-payback-prediction-system.onrender.com/)**

Users can:

* Predict loans online
* Upload batch files
* View prediction history without local installation

## How to Run Locally (Optional)

```bash
git clone https://github.com/YOUR_USERNAME/loan_payback_api.git
cd loan_payback_api
pip install -r requirements.txt
python app.py
```

Then open:

```
http://localhost:5000
```

## Academic Purpose

This project was developed as part of an **academic machine learning and software engineering assignment**, demonstrating:

* ML model integration
* REST API development
* Frontend–backend communication
* Batch data processing
* Cloud deployment

## Final Note

This project demonstrates a **real-world ML deployment workflow**, from model training to cloud hosting, and supports scalable prediction through batch uploads.


## Author

- **NAME:** *KIRENGA Olivier*
- **REGNO:** *25RP18669*
- **CLASS:** *L8 YEAR 4 (BTECH) IT*
- **COURSE:** *ITLML801 MACHINE LEARNING*
- **SCHOOL:** *RP/HUYE COLLEGE*
