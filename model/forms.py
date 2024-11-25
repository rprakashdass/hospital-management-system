from django import forms

# Define choices based on training data encodings
SYMPTOM_CHOICES = [
    (0, 'Symptom A'),
    (1, 'Symptom B'),
    (2, 'Symptom C'),  # Add all relevant symptom choices
]

EXISTING_CONDITION_CHOICES = [
    (0, 'Condition A'),
    (1, 'Condition B'),
    (2, 'Condition C'),  # Add all relevant condition choices
]

class SymptomsForm(forms.Form):
    height_cm = forms.FloatField(label="Height (cm)", required=True)
    weight_kg = forms.FloatField(label="Weight (kg)", required=True)
    blood_pressure = forms.FloatField(label="Blood Pressure", required=True)
    temperature_c = forms.FloatField(label="Temperature (°C)", required=True)
    heart_rate = forms.FloatField(label="Heart Rate", required=True)
    cholesterol_mg_dl = forms.FloatField(label="Cholesterol (mg/dL)", required=True)
    blood_sugar_mg_dl = forms.FloatField(label="Blood Sugar (mg/dL)", required=True)

    # Dropdown for symptoms and existing conditions
    symptoms = forms.ChoiceField(label="Symptoms", choices=SYMPTOM_CHOICES, required=True)
    existing_conditions = forms.ChoiceField(label="Existing Conditions", choices=EXISTING_CONDITION_CHOICES, required=True)

    # Binary fields
    family_history_heart_disease = forms.ChoiceField(
        label="Family History of Heart Disease",
        choices=[(0, 'No'), (1, 'Yes')],
        required=True
    )
    smoking_status = forms.ChoiceField(
        label="Smoking Status",
        choices=[(0, 'Non-Smoker'), (1, 'Smoker')],
        required=True
    )
