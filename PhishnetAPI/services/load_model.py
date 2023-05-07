import os
import joblib

def load_model(model_name):
    model_path = "PhishnetAPI/data/"+model_name
    phish_model = open(model_name,'rb')
    model = joblib.load(phish_model)
    return model