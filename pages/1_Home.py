import streamlit as st
import random
import base64

# Set page config
st.set_page_config(page_title="Mindpulse Health App", layout="centered")

# Load CSS
def load_local_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_local_css("assets/custom.css")

# Dark mode toggle
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

# Set background image
def get_base64_bg(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

bg_image = get_base64_bg("assets/bg.jpg")
st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: url("data:image/jpg;base64,{bg_image}") no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Daily health tip
tips = [
    "Drink at least 8 glasses of water daily.",
    "Take short breaks every hour to stretch.",
    "Include leafy greens in your meals.",
    "Aim for 7-8 hours of quality sleep.",
    "Practice deep breathing to reduce stress.",
]
st.info(f"💡 Daily Health Tip: {random.choice(tips)}")

# ✅ Gradient card content (fully wrapped in HTML)
st.markdown("""<div class="gradient-card"><h1>🏠 Welcome to Mindpulse</h1> <h3>A smart, AI-powered way to monitor your health risks and improve your well-being.</h3> <p>Mindpulse predicts your likelihood of developing:</p> <ul><li>🩸 <b>Diabetes</b></li><li>❤️ <b>Heart Disease</b></li>
        <li>🧬 <b>Cancer</b></li></ul><p>...based on your lifestyle, mental health, and basic vitals.</p><p><b>👉 Use the sidebar and start your Health Check now.</b></p></div>""", unsafe_allow_html=True)

# Optional footer
st.markdown("""<hr><p style='text-align:center'>Made with ❤️ for <b>SDG 3 - Good Health & Well-being</b><br>© 2025 Mindpulse by Harsh Mistry</p>""", unsafe_allow_html=True)
