import streamlit as st
import base64

st.set_page_config(page_title="Health Check", layout="centered")

# Load custom CSS
def load_local_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_local_css("assets/custom.css")

# Gradient background (no image)
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to right, #dbeafe, #f0fdf4);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Theme toggle
dark_mode = st.sidebar.toggle("🌙 Enable Dark Mode")
mode_class = "dark-mode" if dark_mode else "light-theme"
st.markdown(f"<body class='{mode_class}'>", unsafe_allow_html=True)
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
# Wrapped Form in white box
st.markdown("""<div class="form-container"><h2>🧪 Health Check</h2><p>Please fill out the following details to assess your health risks:</p>""", unsafe_allow_html=True)

# Row 1
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
with col2:
    sleep_hours = st.selectbox("Sleep Duration (hrs/day)", ["<5", "5-6", "6-8", "8+"])
    screen_time = st.selectbox("Daily Screen Time (hrs)", ["<2", "2–4", "4–6", "6+"])


# Row 2
col3, col4 = st.columns(2)
with col3:
    activity_level = st.radio("Physical Activity Level", ["Sedentary 🪑", "Moderate 🚶", "High 🏃"])
    mood_score = st.radio("Mood Score Today", [1, 2, 3, 4, 5], horizontal=True)
with col4:
    social_freq = st.selectbox("Social Interactions per Week", ["Rarely", "Sometimes", "Often", "Daily"])
    academic_stress = st.radio("Academic/Work Stress Level", ["Low", "Moderate", "High"])

# Row 3
col5, col6 = st.columns(2)
with col5:
    phq9 = st.slider("PHQ-9 Depression Score (0–27)", 0, 27)
    glucose = st.number_input("Glucose Level (mg/dL)", 50, 300)
with col6:
    gad7 = st.slider("GAD-7 Anxiety Score (0–21)", 0, 21)
    blood_pressure = st.number_input("Blood Pressure (mmHg)", 80, 200)

# Row 4
col7, col8 = st.columns(2)
with col7:
    bmi = st.number_input("BMI", 10.0, 50.0)
with col8:
    cholesterol = st.number_input("Cholesterol Level (mg/dL)", 100, 400)

# Submit button
submit = st.button("🔍 Run Predictions")

if submit:
    st.session_state['age'] = age
    st.session_state['gender'] = {"Male": 0, "Female": 1, "Other": 2}.get(gender, 0)
    st.session_state['sleep_hours'] = {"<5": 0, "5-6": 1, "6-8": 2, "8+": 3}.get(sleep_hours, 2)
    st.session_state['screen_time'] = {"<2": 0, "2–4": 1, "4–6": 2, "6+": 3}.get(screen_time, 1)
    st.session_state['activity_level'] = {"Sedentary 🪑": 0, "Moderate 🚶": 1, "High 🏃": 2}.get(activity_level, 1)
    st.session_state['mood_score'] = mood_score
    st.session_state['phq9'] = phq9
    st.session_state['gad7'] = gad7
    st.session_state['social_freq'] = {"Rarely": 0, "Sometimes": 1, "Often": 2, "Daily": 3}.get(social_freq, 1)
    st.session_state['academic_stress'] = {"Low": 0, "Moderate": 1, "High": 2}.get(academic_stress, 1)
    st.session_state['glucose'] = glucose
    st.session_state['blood_pressure'] = blood_pressure
    st.session_state['bmi'] = bmi
    st.session_state['cholesterol'] = cholesterol
    st.session_state['submitted'] = True
    st.success("✅ Inputs saved! Go to the **Results** page to see predictions.")

# Close container
st.markdown("</div>", unsafe_allow_html=True)
