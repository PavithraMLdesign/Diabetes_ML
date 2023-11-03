import json
import requests

url = 'http://127.0.0.1:8000/diabetes_prediction'

input_data_for_model = {
    'pregnancies' : 1,
    'glucose' : 85,
    'bloodpressure' : 66, 
    'skinthickness' : 29,
    'insulin' : 0,
    'bmi' : 26.6,
    'diabetespedigreefunction' : 0.351,
    'age' : 31
}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data = input_json)

print(response.text)