# Cardiovascular Disease Prediction System

A Machine Learning based **Cardiovascular Disease Prediction System** built using **FastAPI**, **Streamlit**, and **Logistic Regression**.

This project predicts whether a person is likely to be healthy or unhealthy based on health-related input features such as age, gender, height, weight, blood pressure, cholesterol, glucose level, smoking habit, alcohol consumption, and physical activity.

---

## Project Description

This project contains two main parts:

1. **FastAPI Backend**
   - Handles API requests.
   - Loads the trained machine learning model.
   - Receives user health data.
   - Returns prediction result in JSON format.

2. **Streamlit Frontend**
   - Provides a simple user interface.
   - Takes input from users.
   - Sends the input data to the FastAPI backend.
   - Displays the prediction result.

---

## Technologies Used

- Python
- FastAPI
- Streamlit
- Pandas
- Scikit-learn
- Joblib
- Pydantic
- Uvicorn
- Requests

---

## Machine Learning Model

The project uses a trained **Logistic Regression** model for cardiovascular disease prediction.

The saved model files are:

```text
models/model.pkl
models/scaler.pkl