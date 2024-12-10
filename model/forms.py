from django import forms

class SymptomsForm(forms.Form):     
    height = forms.FloatField(
        label="Height (cm)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter height in cm',
            'min': 50,
            'max': 250,
            'step': 0.1
        })
    )
    weight = forms.FloatField(
        label="Weight (kg)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter weight in kg',
            'min': 20,
            'max': 200,
            'step': 0.1
        })
    )
    temperature = forms.FloatField(
        label="Temperature (°C)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter body temperature',
            'min': 30,
            'max': 45,
            'step': 0.1
        })
    )
    heart_rate = forms.FloatField(
        label="Heart Rate (bpm)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter heart rate in bpm',
            'min': 40,
            'max': 200
        })
    )
    cholestrol = forms.FloatField(
        label="Cholesterol (mg/dL)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter cholesterol level',
            'min': 100,
            'max': 300
        })
    )
    blood_sugar = forms.FloatField(
        label="Blood Sugar (mg/dL)",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter blood sugar level',
            'min': 50,
            'max': 500
        })
    )
    systolic = forms.FloatField(
        label="Systolic Pressure",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter systolic pressure',
            'min': 80,
            'max': 200
        })
    )
    diastolic = forms.FloatField(
        label="Diastolic Pressure",
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter diastolic pressure',
            'min': 50,
            'max': 120
        })
    )
    existing_conditions = forms.ChoiceField(
        choices=[
            ('Diabetes', 'Diabetes'),
            ('Hypertension', 'Hypertension'),
            ('High cholesterol', 'High cholesterol'),
            ('Asthma', 'Asthma'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    family_history = forms.ChoiceField(
        choices=[
            ('Yes', 'Yes'),
            ('No', 'No'),
        ],
        label="Family History of Heart Disease",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    smoking_status = forms.ChoiceField(
        choices=[
            ('Never', 'Never'),
            ('Former', 'Former'),
            ('Current', 'Current'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    lab_status = forms.ChoiceField(
        choices=[
            ('High Blood Sugar', 'High Blood Sugar'),
            ('High cholesterol', 'High cholesterol'),
            ('Low Iron', 'Low Iron'),
            ('Normal Test Results', 'Normal Test Results'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    symptom = forms.ChoiceField(
        choices=[
            ('chest pain', 'Chest Pain'),
            ('dizziness', 'Dizziness'),
            ('fatigue', 'Fatigue'),
            ('nausea', 'Nausea'),
            ('palpitations', 'Palpitations'),
            ('shortness of breath', 'Shortness of Breath'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
