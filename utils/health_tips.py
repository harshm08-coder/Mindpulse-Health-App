def get_health_tips(disease, risk_percent, inputs):
    tips = []

    # Base advice (shown if risk is high)
    if risk_percent >= 50:
        tips.append("Consult a healthcare professional for further tests.")
        tips.append("Maintain a detailed health log for at least 2 weeks.")
    elif risk_percent >= 30:
        tips.append("Monitor symptoms closely and adopt healthy lifestyle changes.")
    else:
        tips.append("Keep up the good work! Continue regular check-ups.")

    # Specific suggestions
    if disease == "diabetes":
        if float(inputs["glucose"]) > 140:
            tips.append("Reduce sugar and refined carbs in your diet.")
        if float(inputs["bmi"]) > 25:
            tips.append("Consider a weight management plan with more physical activity.")
        tips.append("Include fiber-rich foods like oats, veggies, and legumes.")
        tips.append("Stay hydrated and limit sweetened beverages.")

    elif disease == "heart":
        if float(inputs["blood_pressure"]) > 130:
            tips.append("Reduce salt intake and processed foods.")
        if float(inputs["cholesterol"]) > 200:
            tips.append("Eat heart-healthy fats (nuts, avocado, olive oil).")
        tips.append("Engage in at least 30 minutes of physical activity daily.")
        tips.append("Avoid smoking and limit alcohol.")

    elif disease == "cancer":
        tips.append("Perform monthly self-exams and attend regular screenings.")
        tips.append("Avoid exposure to known carcinogens (e.g., tobacco, radiation).")
        tips.append("Increase intake of antioxidant-rich foods like berries and leafy greens.")
        tips.append("Maintain a healthy BMI and reduce inflammation-causing foods.")

    # Lifestyle tips based on inputs
    if inputs["sleep_hours"] in ["<5", "5-6"]:
        tips.append("Aim for 7–8 hours of quality sleep each night.")
    if inputs["screen_time"] in ["4–6", "6+"]:
        tips.append("Take regular screen breaks and practice eye exercises.")
    if inputs["academic_stress"] == "High":
        tips.append("Try stress management techniques like journaling or breathing exercises.")
    if inputs["mood_score"] <= 2:
        tips.append("Stay socially active and engage in hobbies you enjoy.")

    return tips
