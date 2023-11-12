#importo librerie
from pydantic import BaseModel
from fastapi import FastAPI
from pypmml import Model
import pandas as pd
from sklearn.preprocessing import StandardScaler

#carico il modello di ml 
model =Model.fromFile("modello/wine-model.pmml")

#creo un classe per definire le proprietà dell'oggetto che riceverò come input del modello
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

#creo applicazione
app = FastAPI()

#creo post per dare l'input al modello di ml
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
    #trasformo l'input in un oggetto di tipo dataframe e poi estraggo i valori
    data=pd.DataFrame(data).values
    #normalizzazione dei dati in input (come avevo fatto per allenare il modello)
    scaling=StandardScaler()
    scaled_data=scaling.fit_transform(data)
    #prediction dell'input
    pred = model.predict(scaled_data)
    #output della
    prediction = ""
    if(pred[0][1] > 0.5):
        prediction = f"Il vino inserito e' di ottima qualita', superiore o uguale a 7. P = {pred[0][1]}"
    else:
        prediction = f"Il vino inserito e' di pessima qualita', inferiore a 7. P = {pred[0][0]}"

    return {**wine.model_dump(), "Prediction": prediction}

    #il modello restituisce una matrice
    #il primo valore [0][0] è la probabilità che il vino sia di qualità inferiore a 7
    #il secondo valore [0][1] è la probabilità che sia maggiore di 7
   
