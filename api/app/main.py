from fastapi import FastAPI
from envs import env

app = FastAPI()

def preprocessing(features):
    feature_list = features.split(",")
    return [int(f) for f in feature_list]

def predict(feature_list):
    return sum(feature_list)

@app.get("/api/predict")
def read_main(data):
    features = preprocessing(data)
    return {
        "Prediction": predict(features),
        "Author": env("USER_NAME"),
    }