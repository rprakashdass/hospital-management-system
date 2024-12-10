# Patient Health Enquiry System

This project is designed to collect patient data for diagnostic predictions. It allows users to input key medical parameters to assess health risks or predict possible diseases using pre-trained models.

## Features
- Collects detailed health-related inputs from patients.
- Provides disease predictions based on the input data.
- Stores data in an organized and structured manner for further analysis.

## Form Labels

Below are the fields available in the form, designed to capture essential patient health parameters:

| **Form Label**           | **Description**                           |
|---------------------------|-------------------------------------------|
| **Height_cm**             | Patient's height in centimeters.         |
| **Weight_kg**             | Patient's weight in kilograms.           |
| **Temperature_C**         | Patient's body temperature in Celsius.   |
| **Heart_Rate**            | Patient's heart rate in beats per minute (bpm). |
| **Cholesterol_mg_dL**     | Cholesterol level in milligrams per deciliter. |
| **Blood_Sugar_mg_dL**     | Blood sugar level in milligrams per deciliter. |
| **Systolic_BP**           | Systolic blood pressure (mmHg).          |
| **Diastolic_BP**          | Diastolic blood pressure (mmHg).         |

### Example Input Data Mapping
The input fields are mapped in the backend as follows:

```python
input_data['Height_cm'] = [height]
input_data['Weight_kg'] = [weight]
input_data['Temperature_C'] = [temperature]
input_data['Heart_Rate'] = [heart_rate]
input_data['Cholesterol_mg_dL'] = [cholestrol]
input_data['Blood_Sugar_mg_dL'] = [blood_sugar]
input_data['Systolic_BP'] = [systolic]
input_data['Diastolic_BP'] = [diastolic]
```

## How to Use
1. Fill in the form with accurate values for all the above fields.
2. Submit the form to process the data and receive predictions.
3. View predictions and access your previous enquiries on the dashboard.


| **Field**               | **Example 1** | **Example 2** |
|--------------------------|---------------|---------------|
| **Height (cm)**          | 174.0         | 162.0         |
| **Weight (kg)**          | 59.0          | 70.0          |
| **Temperature (°C)**     | 36.6          | 37.5          |
| **Heart Rate (bpm)**     | 63            | 72            |
| **Cholesterol (mg/dL)**  | 198.0         | 220.0         |
| **Blood Sugar (mg/dL)**  | 79.0          | 110.0         |
| **Systolic BP (mmHg)**   | 120.0         | 140.0         |
| **Diastolic BP (mmHg)**  | 80.0          | 90.0          |
| **Existing Conditions**  | Diabetes      | Hypertension  |
| **Family History**       | Yes           | No            |
| **Smoking Status**       | Never         | Former        |
| **Lab Status**           | High Cholesterol | Normal    |
| **Symptoms**             | Chest Pain    | Fatigue       |


## Example Output
  Output 1: Coronary Artery Disease
  Output 2: Hypertension
