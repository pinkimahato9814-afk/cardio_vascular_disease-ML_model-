from fastapi import FastAPI # class
from app.models import load_model_scaler # function
from app.schema import Cardio # class
import pandas as pd
 
app= FastAPI() #  object instance of fastapi
model, scaler = load_model_scaler()

# request methosd
#----------------------------------
# post(create/insert),put(update by using primary key or unique key),get(read/retrive),delete(remove)


@app.get('/')
def home():
    return 'welcome to cardiovascular disease prediction systems'


@app.post('/predict-cardio')
def cardiovascular_prediction(data:Cardio):
    input_data = pd.DataFrame([
        data.model_dump() # from schema to 2d list and model_dump=>jason-> convertn
    ])
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    prediction_value = int(prediction[0])

    return {
        "prediction_status": prediction_value,
        "status": "likely to be healthy" if prediction_value == 0 else "likely to be unhealthy"
    }

    #input_scaler  =scaler.transform(input_data)
    #prediction = model.predict(input_scaler[[0]])   

    # return {
    #     "prediction_status" : int(prediction),
    #     "status":"likely to be healthy" if prediction == 0 else "likely to be unhealthy"
    # }



