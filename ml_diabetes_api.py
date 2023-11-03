from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class model_input(BaseModel):

    pregnancies : int
    glucose : int
    bloodpressure : int
    skinthickness : int
    insulin : int
    bmi : float
    diabetespedigreefunction : float
    age : int


# loading the saved model
diabetes_model = pickle.load(open('diabetes_svm_model.sav', 'rb'))


#Create the api
@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):

    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    preg = input_dictionary['pregnancies']
    glu = input_dictionary['glucose']
    bp = input_dictionary['bloodpressure']
    skin = input_dictionary['skinthickness']
    insulin = input_dictionary['insulin']
    bmi = input_dictionary['bmi']
    dpf = input_dictionary['diabetespedigreefunction']
    age = input_dictionary['age']

    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]

    prediction = diabetes_model.predict([input_list]) 

    if prediction[0] == 0:
        return 'The patient is Non-diabetic'
    else:
        return 'The patient is diabetic'
    