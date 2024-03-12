# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:04:06 2024

@author: Dell
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    aloow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


class model_input(BaseModel):
    
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
    
    
diabetes_model = pickle.load(open('trained_model.sav','rb'))

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.jason
    input_dictionary = jason.loads(input_data)
    
    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insul = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    
    input_list = [preg,glu,bp,skin,insul,bmi,dpf,age]
    
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'you are not having diabetic'
    else:
        return 'you are having diabetic'
    
    
    
    
    