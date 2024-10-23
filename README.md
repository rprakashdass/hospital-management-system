# Health Management System!

## Project Overview

This Health Management System is developed as part of the Infosys Springboard Internship on Artificial Intelligence. The aim of this project is to provide an efficient platform for both patients and healthcare providers (doctors) to manage health records, consultations, and predictions related to health conditions.

## Features

- **User Registration**: 
  - Role-based registration for patients and doctors.
  - Secure user authentication with email verification.

- **Role Management**: 
  - Different dashboards for patients and doctors based on their roles.
  - Automatic role assignment during user registration.

- **Health Record Management**: 
  - Patients can manage their personal health information and medical history.
  - Doctors can access and update patient records as needed.

- **Health Prediction Tools**: 
  - Integration of AI algorithms to provide health predictions based on user input and historical data.

- **Document Management**: 
  - Secure storage and retrieval of health-related documents.
  
- **User-Friendly Interface**: 
  - Responsive design using Bootstrap for easy navigation on both desktop and mobile devices.

## Technologies Used

- **Backend**: Django Framework
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite
- **Version Control**: Git for source code management

## File Structure
![image](https://github.com/user-attachments/assets/e7d8d25b-5c4a-43dd-b9bd-cbfd2952e45a)


## Pages
### Home
![image](https://github.com/user-attachments/assets/d1a1849e-e0e5-4d02-b113-dbf14bfe2765)

### Login
![image](https://github.com/user-attachments/assets/403d2ee2-5cb3-4755-be8f-4c5434a0d864)



## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rprakashdass/hospital-management-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd health-management-system
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Run database migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
7. Access the application at `http://127.0.0.1:8000/`.

## Acknowledgements

- Thanks to Infosys Springboard for the opportunity to work on this project and enhance my skills in AI and software development.
