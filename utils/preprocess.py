import pandas as pd

def transform_inputs(
    age, gender, sleep_hours, screen_time, activity_level,
    mood_score, phq9, gad7, social_freq, academic_stress,
    glucose, blood_pressure, bmi, cholesterol
):
    feature_names = [
        'Age', 'gender', 'sleep_hours', 'screen_time', 'activity_level',
        'mood_score', 'phq9', 'gad7', 'social_freq', 'academic_stress',
        'Glucose', 'blood_pressure', 'BMI', 'cholesterol'
    ]

    values = [[
        int(age), int(gender), int(sleep_hours), int(screen_time), int(activity_level),
        int(mood_score), int(phq9), int(gad7), int(social_freq), int(academic_stress),
        float(glucose), float(blood_pressure), float(bmi), float(cholesterol)
    ]]

    return pd.DataFrame(values, columns=feature_names)
