# 🧠 Mindpulse Health App – Smart Health & Well-being Predictor

**Mindpulse** is a web-based health risk assessment app that uses machine learning to predict the likelihood of chronic diseases such as **Diabetes**, **Heart Disease**, and **Breast Cancer**. It also provides personalized wellness recommendations based on mental health and lifestyle indicators like **PHQ-9**, **GAD-7**, **sleep duration**, and **screen time**.

This project aligns with **UN Sustainable Development Goal 3 (SDG 3)**: _Good Health and Well-being_ – promoting early detection, lifestyle awareness, and mental health care.

---

## 📌 Table of Contents

- [🚀 Live Demo](#-live-demo)
- [🎯 Features](#-features)
- [📊 Inputs & Predictions](#-inputs--predictions)
- [🛠️ Technologies Used](#️-technologies-used)
- [📂 Project Structure](#-project-structure)
- [💻 How to Run Locally](#-how-to-run-locally)
- [🌍 How to Deploy Publicly](#-how-to-deploy-publicly)
- [👨‍💻 Developer](#-developer)

---

## 🚀 Live Demo

> 🔗 Try the live app :  
📍 **https://mindpulse-health-app-gwdtjtybwzekuoy6kjqypg.streamlit.app/**

---

## 🎯 Features

- ✅ Predicts risk **in percentage** for:
  - 🩸 **Diabetes**
  - ❤️ **Heart Disease**
  - 🧬 **Breast Cancer** (placeholder model)
- 🧠 Accepts both mental and physical health metrics:
  - Sleep, Screen Time, PHQ-9, GAD-7, Activity Level
- 📊 Real-time predictions using trained ML models
- 💡 Personalized health and wellness suggestions
- 🎨 Gradient UI, dark mode, emoji-rich design
- 🌐 Fully deployable and shareable via Streamlit Cloud

---

## 📊 Inputs & Predictions

| Category         | Fields Collected                                      |
|------------------|--------------------------------------------------------|
| 👤 Personal Info | Age, BMI, Sleep Duration, Screen Time                  |
| 🧠 Mental Health | PHQ-9 Score, GAD-7 Score, Mood Score, Stress Level     |
| 🏃 Activity       | Physical Activity Level, Social Interactions          |
| 🧪 Medical Data   | Glucose, Blood Pressure, Cholesterol                  |
| 📈 Output         | Predicted Risk (%) + Actionable Health Suggestions    |

---

## 🛠️ Technologies Used

| Tool            | Purpose                        |
|-----------------|--------------------------------|
| Python 🐍        | Core backend & ML logic        |
| Streamlit       | Interactive web UI             |
| scikit-learn    | ML model training & inference  |
| pandas, numpy   | Data handling                  |
| joblib          | Model serialization            |
| GitHub          | Version control & hosting      |

---

## 📂 Project Structure

```bash
Mindpulse-Health-App/
├── app.py                      # intropage (main entry point)
├── pages/
│   ├── 1_🏠_Home.py     # Homepage
│   ├── 2_🏥_Health_Check.py     # Health input form
│   ├── 3_📊_Results.py          # Prediction and tips
│   └── 4_ℹ️_About.py            # About the app
├── utils/
│   ├── preprocess.py           # Input transformation logic
│   └── ml_models.py            # Model loading functions
├── models/
│   ├── diabetes_model.pkl
│   ├── heart_model.pkl
│   └── cancer_model.pkl
├── assets/
│   ├── custom.css              # Custom theme styling
│   ├── bg.jpg                  # Background image
│   └── logo.png                # App logo
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
