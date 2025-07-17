import streamlit as st
import os
import base64

# Load CSS
def load_local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_local_css("assets/custom.css")

# Page setup
st.set_page_config(page_title="Mindpulse Health App", layout="centered")
dark_mode = st.sidebar.toggle("🌙 Enable Dark Mode")

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
# Mode switch
mode_class = "dark-mode" if dark_mode else "light-theme"
st.markdown(f"<body class='{mode_class}'>", unsafe_allow_html=True)

# Set background
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

    /* Make "Enable Dark Mode" toggle label white */
    section[data-testid="stSidebar"] label[data-testid="stMarkdownContainer"] p {{
        color: white !important;
        font-weight: 600;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Logo
logo_path = os.path.join("assets", "logo.png")
if os.path.exists(logo_path):
    st.image(logo_path, width=120)

# App Intro Card
st.markdown("""
<div class="gradient-card">
    <h1>🧠 Mindpulse Health App</h1>
    <h3>Your smart well-being assistant</h3>
    <p>Predict the risk of chronic diseases and get personalized health advice based on your daily habits.</p>
    <p><b>👉 Use the sidebar to begin your health check.</b></p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<hr>
<p style='text-align:center'>
Made with ❤️ for <b>SDG 3 - Good Health & Well-being</b><br>
© 2025 Mindpulse by Harsh Mistry
</p>
""", unsafe_allow_html=True)
