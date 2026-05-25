
from pydantic import BaseModel
class Cardio(BaseModel):
        age :float
        gender:int 
        height:int
        weight:int
        ap_hi:int
        ap_lo:int
        cholesterol:int
        gluc:int
        smoke:int
        alco:int
        active:int


 # for running this file in anoconda promot
 # uvicorn app.main:app --reload       