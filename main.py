from fastapi import FastAPI
import pickle
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

class model_input(BaseModel):
    HomePlanet: float
    CryoSleep: float
    Destination: float
    Age: float
    VIP: float
    RoomService: float
    FoodCourt: float
    ShoppingMall: float
    Spa: float
    VRDeck: float
    Deck: float
    CabinNum: float
    Side: float

spaceship_pred = pickle.load(open('spaceship_prediction.sav', 'rb'))

@app.post('/spaceship_pred')
def spaceship_prediction(input_parameters: model_input):
    data = input_parameters.dict()

    input_list = np.array([[
        float(data['HomePlanet']), float(data['CryoSleep']), float(data['Destination']),
        float(data['Age']), float(data['VIP']), float(data['RoomService']),
        float(data['FoodCourt']), float(data['ShoppingMall']), float(data['Spa']),
        float(data['VRDeck']), float(data['Deck']), float(data['CabinNum']), float(data['Side'])
    ]], dtype=np.float32)

    prediction = spaceship_pred.predict(input_list)
    return {"Transported": bool(prediction[0])}
