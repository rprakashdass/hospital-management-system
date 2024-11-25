from django.shortcuts import render
from .forms import SymptomsForm
import joblib
import numpy as np

# Create your views here.model/templates/modelPages/index.html
def home(request):
    return render(request, "model_home.html")

# Load the model and preprocessing objects
model_data = joblib.load('model/model.pkl')
model = model_data['model']
scaler = model_data['scaler']

def predict_disease(request):
    prediction = None
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

            # Scale the input
            input_vector_scaled = scaler.transform([input_vector])

            # Make prediction
            pred_encoded = model.predict(input_vector_scaled)
            prediction = pred_encoded[0]
            print(input_vector_scaled)
            print(pred_encoded)
            print(prediction)
          # Get the numeric prediction

    else:
        form = SymptomsForm()

    return render(request, 'predict.html', {'form': form, 'prediction': prediction})
