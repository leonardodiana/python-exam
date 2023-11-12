from pydantic import BaseModel
from fastapi import FastAPI
from pypmml import Model
import pandas as pd
from sklearn.preprocessing import StandardScaler

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
    scaling=StandardScaler()
    scaled_data=scaling.fit_transform(data)
    pred = model.predict(scaled_data)
    print(pred)
    prediction = ""
    if(pred[0][1] > 0.5):
        prediction = f"Il vino inserito e' di ottima qualita', superiore o uguale a 7. P = {pred[0][1]}"
    else:
        prediction = f"Il vino inserito e' di pessima qualita', inferiore a 7. P = {pred[0][0]}"

    return {**wine.model_dump(), "Prediction": prediction}

   
