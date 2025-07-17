import streamlit as st
import base64

# Page config
st.set_page_config(page_title="About Mindpulse", layout="wide")

# Load custom CSS
def load_local_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_local_css("assets/custom.css")

# Theme toggle
dark_mode = st.sidebar.toggle("🌙Enable Dark Mode")

# Inject dark/light mode JS
if dark_mode:
    st.markdown("""
        <script>
        document.body.classList.add('dark-mode');
        document.body.classList.remove('light-theme');
        </script>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <script>
        document.body.classList.add('light-theme');
        document.body.classList.remove('dark-mode');
        </script>
    """, unsafe_allow_html=True)

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

# ---------- Page Content ----------
st.markdown("# 💬 About Mindpulse Health App")

st.markdown("""
Mindpulse is a smart web-based health screening tool designed to help users understand their risk of developing **chronic diseases** like:

- 🩸 Diabetes  
- ❤️ Heart Disease  
- 🧬 Breast Cancer  

It uses trained **machine learning models** on medical + lifestyle data and provides **personalized tips** to improve well-being.

---

### 🔍 Features:
- Predict disease risks from health/lifestyle input
- Suggests healthy habits tailored to your lifestyle
- Clean UI for all age groups
- 100% private – no data storage

---

### 🚀 Built Using:
- Python 🐍  
- Streamlit (for UI)  
- Scikit-Learn (ML models)  
- Pandas + NumPy (data prep)

---

### 📚 Inspired By:
**UN SDG 3: Good Health and Well-Being**  
This project aims to promote awareness, prevention, and proactive care for all age groups using AI/ML tools.

---
""")
