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




def spaceship_predoction(input_parameters:model_input):
    input_data= input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    
    hp = input_dictionary['HomePlanet']
    cs = input_dictionary['CryoSleep']
    dest = input_dictionary['Destination']
    age = input_parameters['Age']
    vip = input_parameters['VIP']
    rs = input_parameters['RoomService']
    fc = input_parameters['FoodCourt'] 
    shopma = input_parameters['ShoppingMall']
    spa = input_parameters['Spa']
    vrd = input_parameters['VRDeck']
    canum = input_parameters['CabinNum']
    side = input_parameters['Side']
    
    input_list = [hp, cs, dest, age, vip, rs, fc, shopma, spa,vrd, canum, side]
    
    prediction = spaceship_pred.predict([input_list])
    
    return {"Transported": bool(prediction[0])}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    