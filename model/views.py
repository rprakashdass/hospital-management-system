from django.shortcuts import render
from .forms import SymptomsForm
import joblib
import numpy as np
import pandas as pd


def home(request):
    return render(request, "model_home.html")


model_data = joblib.load('model/model.pkl')
model = model_data['model']
scaler = model_data['scaler']
label_encoder = model_data['label_encoder']
features = model_data['features']

disease_labels = {}
disease_labels[0] = 'Unknown',
disease_labels[1] = 'Chest Pain',
disease_labels[2] = 'Dizziness',
disease_labels[3] = 'Fatigue',
disease_labels[4] = 'Nausea',
disease_labels[5] = 'Palpitations',
disease_labels[6] = 'Shortness of Breath',

print(disease_labels)

def predict_disease(request):
    prediction = None
    predicted_label = None
    if request.method == 'POST':
        form = SymptomsForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data

            # Prepare the input vector in the correct order
            input_vector = [
                user_input['height_cm'],
                user_input['weight_kg'],
                user_input['blood_pressure'],
                user_input['temperature_c'],
                user_input['heart_rate'],
                int(user_input['symptoms']),  # Already encoded
                int(user_input['existing_conditions']),  # Already encoded
                0,  # Laboratory_Test_Results placeholder (update if applicable)
                user_input['cholesterol_mg_dl'],
                user_input['blood_sugar_mg_dl'],
                int(user_input['family_history_heart_disease']),
                int(user_input['smoking_status'])
            ]

            # Convert input_vector to pandas DataFrame to match the model's expected input format
            input_df = pd.DataFrame([input_vector], columns=features)

            # Scale the input
            input_vector_scaled = scaler.transform(input_df)

            # Make prediction
            pred_encoded = model.predict(input_vector_scaled)
            prediction = pred_encoded[0]

            # Map the encoded prediction (numeric value) to the disease name
            predicted_label = disease_labels[prediction]

            # Print the results for debugging
            print("Input Vector (Scaled):", input_df)
            print("Encoded Prediction:", prediction)
            print("Predicted Label:", predicted_label)

    else:
        form = SymptomsForm()

    return render(request, 'predict.html', {'form': form, 'prediction': predicted_label})
