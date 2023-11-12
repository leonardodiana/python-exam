import joblib
from pydantic import BaseModel
from fastapi import FastAPI
import json

model=joblib.load('modello/wine-model.pmml')

class WineTest(BaseModel):
    color:int
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float   
    density: float
    pH: float
    sulphates: float
    alcohol: float
    quality:int

app = FastAPI()

@app.post("/testWine")
def test_wine(wine:WineTest):
    data=[wine.color, wine.fixed_acidity, wine.volatile_acidity, wine.citric_acid, wine.residual_sugar, wine.chlorides,
        wine.free_sulfur_dioxide, wine.density, wine.pH, wine.sulphates, wine.alcohol, wine.quality]
    pred=model.predict([data])
    print(pred)
    return pred.tolist()

    # if (result==0):
    #     return{"Il vino inserito è ottimo, ha una qualità pari a 7 o superiore!"}
    # else:
    #     return{"Il vino è di scarsa qualità"}


