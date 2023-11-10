from fastapi import FastAPI
from database.db import *
from database.crud import *
import numpy as np




#creo app
app = FastAPI()

#api POST che richiama funzione presente nel file crud.py
#permette di creare un nuovo record da inserire nel db

@app.post("/addWine")
def new_wine(wine:Wine):
    newWine=create_wine(wine)
    return{"id":newWine, **wine.model_dump()}

#api GET che richiama funzione presente nel file crud.py
#restituisce tutti i vini presenti nel db

@app.get("/wine")
def read_all_wine_endpoint():
    return read_all_wines()

#api GET che richiama funzione presente nel file crud.py
#restituisce tutti i vini di un determinato colore presenti nel db

@app.get("/wine/{color}")
def read_wines_by_color_endpoint(color:str):
    return read_wines_by_color(color)

#api GET che richiama funzione presente nel file crud.py
#restituisce la qualità media dei vini presenti nel db

@app.get("/quality")
def read_mean_quality_endpoint():
    return read_mean_quality()

#api GET che richiama funzione presente nel file crud.py
#restituisce la qualità media dei vini presenti nel db.
#in questo caso è possibile scegliere anche il colore dei vini

@app.get("/quality/{color}")
def mean_quality_by_color_endpoint(color:str):
    return read_mean_quality_by_color(color)

#api GET che richiama funzione presente nel file crud.py
#restituisce tutti i vini al di sopra di un determinato grado alcolico che viene passato come parametro.

@app.get("/alcohol/{vol}")
def read_wine_by_alcohol_vol_endpoint(vol:float):
    return read_wine_by_alchohol_vol(vol)

#api GET che richiama funzione presente nel file crud.py
#restituisce la qualità media dei vini al di sopra di un determinato grado alcolico che viene passato come parametro.

@app.get("/alcohol/{vol}/mean")
def read_mean_quality_by_alcohol_vol_endpoint(vol:float):
    return read_mean_quality_by_alcohol_vol(vol)

#api DELETE che richiama funzione presente nel file crud.py
#permette di cancellare un record individuandolo attraverso l'id che viene passato come parametro

@app.delete("/deleteWine/{id}")
def delete_wine_by_id_endpoint(id:int):
    delete_wine_by_id(id)
    return{"message": "Dato con eliminato con successo"}
    