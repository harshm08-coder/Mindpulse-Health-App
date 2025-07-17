import joblib

def load_models():
    diabetes_model = joblib.load("models/diabetes_model.pkl")
    heart_model = joblib.load("models/heart_model.pkl")
    cancer_model = joblib.load("models/cancer_model.pkl")
    return diabetes_model, heart_model, cancer_model
