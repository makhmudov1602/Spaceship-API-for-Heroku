#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 10:48:07 2025

@author: muhammadqodir
"""



from fastapi import FastAPI
import pickle
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods = ['*'],
    allow_headers=['*']
)


class model_input(BaseModel):
    HomePlanet: float
    CryoSleep:float
    Destination :float
    Age:float
    VIP:float
    RoomService:float
    FoodCourt:float
    ShoppingMall:float
    Spa:float
    VRDeck:float
    Deck:float
    CabinNum:float
    Side:float
    
    
spaceship_pred = pickle.load(open('spaceship_prediction.sav', 'rb'))

@app.post('/spaceship_pred')
def spaceship_prediction(input_parameters: model_input):
    # Convert pydantic model to dict directly
    input_data = input_parameters.dict()
    
    # Safely extract each value
    hp = input_data['HomePlanet']
    cs = input_data['CryoSleep']
    dest = input_data['Destination']
    age = input_data['Age']
    vip = input_data['VIP']
    rs = input_data['RoomService']
    fc = input_data['FoodCourt']
    shopma = input_data['ShoppingMall']
    spa = input_data['Spa']
    vrd = input_data['VRDeck']
    deck = input_data['Deck']
    canum = input_data['CabinNum']
    side = input_data['Side']
    
    input_list = [hp, cs, dest, age, vip, rs, fc, shopma, spa, vrd, deck, canum, side]
    
    prediction = spaceship_pred.predict([input_list])
    
    return {"Transported": bool(prediction[0])}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
