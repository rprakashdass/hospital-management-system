from django import forms

class SymptomsForm(forms.Form):
    # Define the fields the user needs to input
    height_cm = forms.IntegerField(label='Height (cm)', required=True)
    weight_kg = forms.IntegerField(label='Weight (kg)', required=True)
    blood_pressure = forms.IntegerField(label='Blood Pressure', required=True)
    temperature_c = forms.FloatField(label='Temperature (°C)', required=True)
    heart_rate = forms.IntegerField(label='Heart Rate', required=True)
    
    # Symptoms choices (assuming they are already encoded)
    SYMPTOMS_CHOICES = [
        (0, 'Unknown'),
        (1, 'Chest Pain'),
        (2, 'Dizziness'),
        (3, 'Fatigue'),
        (4, 'Nausea'),
        (5, 'Palpitations'),
        (6, 'Shortness of Breath')
    ]
    symptoms = forms.ChoiceField(choices=SYMPTOMS_CHOICES, required=True)

    # Existing conditions choices (encoded)
    EXISTING_CONDITION_CHOICES = [
        (0, 'Asthma'),
        (1, 'Diabetes'),
        (2, 'High Cholesterol'),
        (3, 'Hypertension'),
        (4, 'Thyroid'),
        (5, 'None')
    ]
    existing_conditions = forms.ChoiceField(choices=EXISTING_CONDITION_CHOICES, required=True)

    cholesterol_mg_dl = forms.IntegerField(label='Cholesterol (mg/dl)', required=True)
    blood_sugar_mg_dl = forms.IntegerField(label='Blood Sugar (mg/dl)', required=True)
    
    # Family history of heart disease (1 for Yes, 0 for No)
    family_history_heart_disease = forms.IntegerField(label='Family History of Heart Disease', required=True)

    # Smoking status (1 for smoker, 0 for non-smoker)
    smoking_status = forms.IntegerField(label='Smoking Status', required=True)
