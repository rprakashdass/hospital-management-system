from django.shortcuts import render
from django.http import JsonResponse
from .forms import SymptomsForm
import pandas as pd
import joblib
import os
from .models import Enquiry

def home(request):
    return render(request, "model_home.html")

def load_models():
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        model = joblib.load(os.path.join(BASE_DIR, 'pickle_files', 'knn_model.pkl'))
        label_encoder = joblib.load(os.path.join(BASE_DIR, 'pickle_files', 'label_encoder.pkl'))
        return model, label_encoder
    except Exception as e:
        print(f"Error loading models: {e}")
        return None, None

def predict_disease(request):
    model, label_encoder = load_models()
    
    if not model:
        return JsonResponse({'error': 'Model loading failed'}, status=500)
    
    if request.method == 'POST':
        form = SymptomsForm(request.POST)
        if form.is_valid():
            # Get cleaned data from the form
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            temperature = form.cleaned_data['temperature']
            heart_rate = form.cleaned_data['heart_rate']
            cholestrol = form.cleaned_data['cholestrol']
            blood_sugar = form.cleaned_data['blood_sugar']
            systolic = form.cleaned_data['systolic']
            diastolic = form.cleaned_data['diastolic']
            existing_conditions = form.cleaned_data['existing_conditions']
            family_history = form.cleaned_data['family_history']
            smoking_status = form.cleaned_data['smoking_status']
            lab_status = form.cleaned_data['lab_status']
            symptoms = form.cleaned_data['symptom']
            
            # Build input data for prediction
            categorical_columns = [
                'Symptoms_chest pain', 'Symptoms_dizziness', 'Symptoms_fatigue', 
                'Symptoms_nausea', 'Symptoms_palpitations', 'Symptoms_shortness of breath',
                'Existing_Conditions_Asthma', 'Existing_Conditions_Diabetes', 
                'Existing_Conditions_High Cholesterol', 'Existing_Conditions_Hypertension', 
                'Existing_Conditions_Thyroid', 'Laboratory_Test_Results_High Blood Sugar', 
                'Laboratory_Test_Results_High Cholesterol', 'Laboratory_Test_Results_Low Iron', 
                'Laboratory_Test_Results_Normal', 'Smoking_Status_Current', 
                'Smoking_Status_Former', 'Smoking_Status_Never', 
                'Family_History_Heart_Disease_No', 'Family_History_Heart_Disease_Yes'
            ]
            
            input_data = {col: [False] for col in categorical_columns}

            # Fill categorical input data
            if 'chest pain' in symptoms:
                input_data['Symptoms_chest pain'] = [True]
            if 'dizziness' in symptoms:
                input_data['Symptoms_dizziness'] = [True]
            # Repeat for other symptoms, conditions, lab_status, and family history...

            # Add numerical data
            input_data['Height_cm'] = [height]
            input_data['Weight_kg'] = [weight]
            input_data['Temperature_C'] = [temperature]
            input_data['Heart_Rate'] = [heart_rate]
            input_data['Cholesterol_mg_dL'] = [cholestrol]
            input_data['Blood_Sugar_mg_dL'] = [blood_sugar]
            input_data['Systolic_BP'] = [systolic]
            input_data['Diastolic_BP'] = [diastolic]

            # Convert to DataFrame
            input_df = pd.DataFrame(input_data)

            # Ensure all model columns are present
            model_columns = [
                'Height_cm', 'Weight_kg', 'Temperature_C', 'Heart_Rate', 'Cholesterol_mg_dL', 
                'Blood_Sugar_mg_dL', 'Symptoms_chest pain', 'Symptoms_dizziness', 'Symptoms_fatigue', 
                'Symptoms_nausea', 'Symptoms_palpitations', 'Symptoms_shortness of breath',
                'Existing_Conditions_Asthma', 'Existing_Conditions_Diabetes', 
                'Existing_Conditions_High Cholesterol', 'Existing_Conditions_Hypertension', 
                'Existing_Conditions_Thyroid', 'Laboratory_Test_Results_High Blood Sugar', 
                'Laboratory_Test_Results_High Cholesterol', 'Laboratory_Test_Results_Low Iron', 
                'Laboratory_Test_Results_Normal', 'Smoking_Status_Current', 
                'Smoking_Status_Former', 'Smoking_Status_Never', 
                'Family_History_Heart_Disease_No', 'Family_History_Heart_Disease_Yes', 
                'Systolic_BP', 'Diastolic_BP'
            ]
            for col in model_columns:
                if col not in input_df.columns:
                    input_df[col] = 0
            
            input_df = input_df[model_columns]

            # Predict disease
            prediction = model.predict(input_df)
            disease_name = label_encoder.inverse_transform(prediction)[0]

            # Save the enquiry with the prediction
            enquiry = Enquiry(
                user=request.user,  # Link to logged-in user
                height=height,
                weight=weight,
                temperature=temperature,
                heart_rate=heart_rate,
                cholestrol=cholestrol,
                blood_sugar=blood_sugar,
                systolic=systolic,
                diastolic=diastolic,
                existing_conditions=existing_conditions,
                family_history=family_history,
                smoking_status=smoking_status,
                lab_status=lab_status,
                symptom=symptoms,
                prediction=disease_name
            )
            enquiry.save()

            return render(request, 'predict.html', {'prediction': disease_name})

        return JsonResponse({'error': 'Invalid form input'}, status=400)

    form = SymptomsForm()
    return render(request, 'predict.html', {'form': form, 'prediction': None})





# from django.shortcuts import render
# from django.http import JsonResponse
# from .forms import SymptomsForm
# import pandas as pd
# import joblib
# import os
# from .models import Enquiry

# def home(request):
#     return render(request, "model_home.html")


# def load_models():
#     try:
#         BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#         model = joblib.load(os.path.join(BASE_DIR, 'pickle_files', 'knn_model.pkl'))
#         # scaler = joblib.load(os.path.join(BASE_DIR, 'pickle_files', 'scaler.pkl'))
#         # one_hot_encoder = joblib.load(os.path.join(BASE_DIR, 'pickle_files', 'encoder.pkl'))
#         label_encoder = joblib.load(os.path.join(BASE_DIR, 'pickle_files', 'label_encoder.pkl'))
#         return model, label_encoder
#         # return model, scaler, one_hot_encoder, label_encoder
#     except Exception as e:
#         print(f"Error loading models: {e}")
#         return None, None, None, None

# def predict_disease(request):

#     # model, scaler, one_hot_encoder, label_encoder = load_models()
#     model, label_encoder = load_models()
    
#     if not model:
#         return JsonResponse({'error': 'Model loading failed'}, status=500)
    
#     if request.method == 'POST':
#         form = SymptomsForm(request.POST)
#         if form.is_valid():
#             height = form.cleaned_data['height']
#             weight = form.cleaned_data['weight']
#             temperature = form.cleaned_data['temperature']
#             heart_rate = form.cleaned_data['heart_rate']
#             cholestrol = form.cleaned_data['cholestrol']
#             blood_sugar = form.cleaned_data['blood_sugar']
#             systolic = form.cleaned_data['systolic']
#             diastolic = form.cleaned_data['diastolic']
#             existing_conditions = form.cleaned_data['existing_conditions']
#             family_history = form.cleaned_data['family_history']
#             smoking_status = form.cleaned_data['smoking_status']
#             lab_status = form.cleaned_data['lab_status']
#             symptoms = form.cleaned_data['symptom']
            
#             categorical_columns = [
#                 'Symptoms_chest pain', 'Symptoms_dizziness', 'Symptoms_fatigue', 
#                 'Symptoms_nausea', 'Symptoms_palpitations', 'Symptoms_shortness of breath',
#                 'Existing_Conditions_Asthma', 'Existing_Conditions_Diabetes', 
#                 'Existing_Conditions_High Cholesterol', 'Existing_Conditions_Hypertension', 
#                 'Existing_Conditions_Thyroid', 'Laboratory_Test_Results_High Blood Sugar', 
#                 'Laboratory_Test_Results_High Cholesterol', 'Laboratory_Test_Results_Low Iron', 
#                 'Laboratory_Test_Results_Normal', 'Smoking_Status_Current', 
#                 'Smoking_Status_Former', 'Smoking_Status_Never', 
#                 'Family_History_Heart_Disease_No', 'Family_History_Heart_Disease_Yes'
#             ]
            
#             input_data = {col: [False] for col in categorical_columns}

#             if 'chest pain' in symptoms:
#                 input_data['Symptoms_chest pain'] = [True]
#             if 'dizziness' in symptoms:
#                 input_data['Symptoms_dizziness'] = [True]
#             if 'fatigue' in symptoms:
#                 input_data['Symptoms_fatigue'] = [True]
#             if 'nausea' in symptoms:
#                 input_data['Symptoms_nausea'] = [True]
#             if 'palpitations' in symptoms:
#                 input_data['Symptoms_palpitations'] = [True]
#             if 'shortness of breath' in symptoms:
#                 input_data['Symptoms_shortness of breath'] = [True]
            
#             if 'Asthma' in existing_conditions:
#                 input_data['Existing_Conditions_Asthma'] = [True]
#             if 'Diabetes' in existing_conditions:
#                 input_data['Existing_Conditions_Diabetes'] = [True]
#             if 'High Cholesterol' in existing_conditions:
#                 input_data['Existing_Conditions_High Cholesterol'] = [True]
#             if 'Hypertension' in existing_conditions:
#                 input_data['Existing_Conditions_Hypertension'] = [True]
#             if 'Thyroid' in existing_conditions:
#                 input_data['Existing_Conditions_Thyroid'] = [True]
            
#             if 'High Blood Sugar' in lab_status:
#                 input_data['Laboratory_Test_Results_High Blood Sugar'] = [True]
#             if 'High Cholesterol' in lab_status:
#                 input_data['Laboratory_Test_Results_High Cholesterol'] = [True]
#             if 'Low Iron' in lab_status:
#                 input_data['Laboratory_Test_Results_Low Iron'] = [True]
#             if 'Normal' in lab_status:
#                 input_data['Laboratory_Test_Results_Normal'] = [True]
            
#             if smoking_status == 'Current':
#                 input_data['Smoking_Status_Current'] = [True]
#             if smoking_status == 'Former':
#                 input_data['Smoking_Status_Former'] = [True]
#             if smoking_status == 'Never':
#                 input_data['Smoking_Status_Never'] = [True]
            
#             if family_history == 'Yes':
#                 input_data['Family_History_Heart_Disease_Yes'] = [True]
#             else:
#                 input_data['Family_History_Heart_Disease_No'] = [True]
            
#             input_data['Height_cm'] = [height]
#             input_data['Weight_kg'] = [weight]
#             input_data['Temperature_C'] = [temperature]
#             input_data['Heart_Rate'] = [heart_rate]
#             input_data['Cholesterol_mg_dL'] = [cholestrol]
#             input_data['Blood_Sugar_mg_dL'] = [blood_sugar]
#             input_data['Systolic_BP'] = [systolic]
#             input_data['Diastolic_BP'] = [diastolic]
            
#             # input data as a dataframe
#             input_df = pd.DataFrame(input_data)
            
#             # re-defining models
#             model_columns = [
#                 'Height_cm', 'Weight_kg', 'Temperature_C', 'Heart_Rate', 'Cholesterol_mg_dL', 
#                 'Blood_Sugar_mg_dL', 'Symptoms_chest pain', 'Symptoms_dizziness', 'Symptoms_fatigue', 
#                 'Symptoms_nausea', 'Symptoms_palpitations', 'Symptoms_shortness of breath',
#                 'Existing_Conditions_Asthma', 'Existing_Conditions_Diabetes', 
#                 'Existing_Conditions_High Cholesterol', 'Existing_Conditions_Hypertension', 
#                 'Existing_Conditions_Thyroid', 'Laboratory_Test_Results_High Blood Sugar', 
#                 'Laboratory_Test_Results_High Cholesterol', 'Laboratory_Test_Results_Low Iron', 
#                 'Laboratory_Test_Results_Normal', 'Smoking_Status_Current', 
#                 'Smoking_Status_Former', 'Smoking_Status_Never', 
#                 'Family_History_Heart_Disease_No', 'Family_History_Heart_Disease_Yes', 
#                 'Systolic_BP', 'Diastolic_BP'
#             ]
            
#             for col in model_columns:
#                 if col not in input_df.columns:
#                     input_df[col] = 0  # missing columns handled
            
#             input_df = input_df[model_columns]

#             prediction = model.predict(input_df)
            
#             # Getting disease name using label encoding 
#             disease_name = label_encoder.inverse_transform(prediction)

#             # Save the enquiry with the prediction
#             enquiry = form.save(commit=False)
#             enquiry.user = request.user  # Link to the logged-in user
#             enquiry.prediction = disease_name[0]  # Save the predicted disease
#             enquiry.save()
            
#             # displaying the prediction
#             return render(request, 'predict.html', {'prediction': disease_name[0]})
        
#         else:
#             return JsonResponse({'error': 'Invalid form input'}, status=400)

#     else:
#         form = SymptomsForm()
#         return render(request, 'predict.html', {'form': form, 'prediction': None})