import streamlit as st
import datetime
from utils.preprocess import transform_inputs
from utils.ml_models import load_models
import pandas as pd
import base64

# Page config
st.set_page_config(page_title="Mindpulse Health Risk Results", layout="centered")

# Load custom CSS
def load_local_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_local_css("assets/custom.css")



# Apply gradient background and black text only to main content
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to top left, #f3f4f6, #e0e7ff);
        background-size: cover;
        color: #000 !important;
    }

    [data-testid="stSidebar"] * {
        color: inherit !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🧠 Mindpulse Health Risk Results")

if not st.session_state.get("submitted", False):
    st.warning("⚠️ Please complete the health check on the **'Health Check'** page before viewing results.")
    st.stop()

# Get inputs from session
data = {
    'age': st.session_state.get("age", 30),
    'gender': st.session_state.get("gender", 0),
    'sleep_hours': st.session_state.get("sleep_hours", 2),
    'screen_time': st.session_state.get("screen_time", 2),
    'activity_level': st.session_state.get("activity_level", 1),
    'mood_score': st.session_state.get("mood_score", 2),
    'phq9': st.session_state.get("phq9", 5),
    'gad7': st.session_state.get("gad7", 4),
    'social_freq': st.session_state.get("social_freq", 2),
    'academic_stress': st.session_state.get("academic_stress", 1),
    'glucose': st.session_state.get("glucose", 100),
    'blood_pressure': st.session_state.get("blood_pressure", 120),
    'bmi': st.session_state.get("bmi", 22.5),
    'cholesterol': st.session_state.get("cholesterol", 180)
}

# Predict
X = transform_inputs(**data)

with st.spinner("Loading ML models..."):
    diabetes_model, heart_model, cancer_model = load_models()

diabetes_risk = diabetes_model.predict_proba(X)[0][1] * 100
heart_risk = heart_model.predict_proba(X)[0][1] * 100
cancer_risk = cancer_model.predict_proba(X)[0][1] * 100

st.success("✅ Prediction Complete")

# Risk Metrics
st.subheader("🩺 Health Risk Percentages")
st.metric("Diabetes Risk", f"{diabetes_risk:.2f}%")
st.metric("Heart Disease Risk", f"{heart_risk:.2f}%")
st.metric("Cancer Risk", f"{cancer_risk:.2f}%")
st.info("ℹ️ Risk is calculated based on your input lifestyle and health metrics.")

# Personalized Activity Plan
plans = {
    0: "Sedentary: Start with 10-15 min daily walking, gradually increase.",
    1: "Moderate: Maintain 30 min cardio 5 days/week plus light strength training.",
    2: "High: Mix cardio, strength, and flexibility workouts 5-6 days/week."
}
st.subheader("🏃 Personalized Weekly Activity Plan")
st.info(plans.get(data['activity_level'], "Maintain a healthy activity routine!"))

# Health Tips
st.subheader("💡 Personalized Health Tips")

def risk_advice(risk, condition):
    if risk > 50:
        st.warning(f"🚨 High {condition} risk")
    elif risk > 25:
        st.info(f"⚠️ Moderate {condition} risk")
    else:
        st.success(f"✅ Low {condition} risk")

    if condition == "diabetes" and risk > 25:
        st.markdown("**Precautions:** Limit sugar, carbs; monitor glucose.")
        st.markdown("**Foods:** Leafy greens, legumes, whole grains.")
        st.markdown("**Exercise:** Walking, swimming, strength training.")
    elif condition == "heart" and risk > 25:
        st.markdown("**Precautions:** Avoid fats, reduce stress, check BP.")
        st.markdown("**Foods:** Oats, salmon, olive oil, almonds.")
        st.markdown("**Exercise:** Jogging, yoga, cardio.")
    elif condition == "cancer" and risk > 25:
        st.markdown("**Precautions:** Avoid tobacco, alcohol, processed food.")
        st.markdown("**Foods:** Berries, broccoli, garlic, tomatoes.")
        st.markdown("**Exercise:** Aerobics and strength training.")

risk_advice(diabetes_risk, "diabetes")
risk_advice(heart_risk, "heart")
risk_advice(cancer_risk, "cancer")

# Visual Risk Bars
st.subheader("📊 Visualized Health Risks")

def risk_color(risk):
    return '🔴 High' if risk > 50 else '🟠 Moderate' if risk > 25 else '🟢 Low'

st.write(f"**Diabetes Risk:** {diabetes_risk:.2f}% {risk_color(diabetes_risk)}")
st.progress(min(diabetes_risk / 100, 1.0))

st.write(f"**Heart Disease Risk:** {heart_risk:.2f}% {risk_color(heart_risk)}")
st.progress(min(heart_risk / 100, 1.0))

st.write(f"**Cancer Risk:** {cancer_risk:.2f}% {risk_color(cancer_risk)}")
st.progress(min(cancer_risk / 100, 1.0))

# Save result
if "history" not in st.session_state:
    st.session_state.history = []

current_result = {
    "date": datetime.date.today().isoformat(),
    "diabetes": diabetes_risk,
    "heart": heart_risk,
    "cancer": cancer_risk
}

if st.button("💾 Save This Result"):
    st.session_state.history.append(current_result)
    st.success("Result saved!")

# History display
if st.session_state.history:
    st.subheader("📈 Past Results")
    for record in st.session_state.history:
        st.write(f"{record['date']}: Diabetes {record['diabetes']:.1f}%, Heart {record['heart']:.1f}%, Cancer {record['cancer']:.1f}%")


# Download as CSV
csv = pd.DataFrame([current_result]).to_csv(index=False).encode('utf-8')
download_html = f"""
    <a href="data:text/csv;base64,{base64.b64encode(csv).decode()}" 
       download="mindpulse_health_report.csv">
        <button style="
            background-color: #1e40af;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            margin-top: 10px;
        ">
            📥 Download Report as CSV
        </button>
    </a>
"""
st.markdown(download_html, unsafe_allow_html=True)

# Reset session
if st.button("🔄 Reset and Start Over"):
    for key in ["submitted", "age", "gender", "sleep_hours", "screen_time", "activity_level", "mood_score", "phq9", "gad7", "social_freq", "academic_stress", "glucose", "blood_pressure", "bmi", "cholesterol"]:
        st.session_state.pop(key, None)
    st.success("Session cleared. Refresh the page or return to Health Check.")
