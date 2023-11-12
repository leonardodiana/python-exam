from pydantic import BaseModel
from fastapi import FastAPI
from pypmml import Model
import pandas as pd

model =Model.fromFile("modello/wine-model.pmml")


class WineTest(BaseModel):
    color: int
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


app = FastAPI()


@app.post("/testWine")
def test_wine(wine: WineTest):
    data = [
        [
            wine.color,
            wine.fixed_acidity,
            wine.volatile_acidity,
            wine.citric_acid,
            wine.residual_sugar,
            wine.chlorides,
            wine.free_sulfur_dioxide,
            wine.density,
            wine.pH,
            wine.sulphates,
            wine.alcohol,
        ]
    ]
    data=pd.DataFrame(data).values
    pred = model.predict(data)[0][1]
    print(pred)
    prediction = ""
    if(pred > 0.5):
        prediction = f"Il vino inserito è di ottima qualità, superiore o uguale a 7 con probabilità del {pred}"
    else:
        prediction = f"Il vino inserito è di pessima qualità, inferiore a 7 con probabilità del {pred}"

    return {**wine.model_dump(), "Prediction": prediction}

    # if (result==0):
    #     return{"Il vino inserito è ottimo, ha una qualità pari a 7 o superiore!"}
    # else:
    #     return{"Il vino è di scarsa qualità"}
