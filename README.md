# 🩺 Medical Disease Prediction System

This is a Streamlit-based web application that predicts potential medical conditions based on user-input symptoms and provides relevant recommendations, such as precautions, medications, diet, and workouts.

## 📌 Features

- 🌡️ Symptom-based disease prediction
- 🧠 ML model (Random Forest) trained on symptom severity data
- 💊 Suggestions for medications, precautions, and workouts
- 🥗 Diet recommendations for diagnosed diseases
- 📋 Clean UI built with Streamlit and custom CSS

## 🚀 Tech Stack

- **Frontend:** Streamlit, CSS
- **Backend:** Python
- **ML Model:** Random Forest Classifier (trained using scikit-learn)
- **Data Handling:** Pandas, NumPy
- **Visualization:** Streamlit UI components

## 🗂️ Project Structure

```bash
recommendation-main/
│
├── app.py                     # Main Streamlit app
├── assets/style.css           # Custom styling
├── data/                      # CSV datasets (symptoms, diets, etc.)
│   ├── rf_model.pkl           # Trained Random Forest model
│   └── *.csv                  # Data sources (symptom severity, medication, diet, etc.)
├── helpers/                   # Backend logic
│   ├── model_loader.py        # Model loading utilities
│   ├── predictor.py           # Prediction logic
│   └── disease_info.py        # Disease metadata handler
└── README.md                  # Project documentation
