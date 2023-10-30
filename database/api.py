from fastapi import FastAPI
import sqlite3
from database.db import *
import numpy as np





app = FastAPI()


@app.get("/wine")
def read_all_wine_endpoint():
    return read_all_wines()

@app.get("/wine/{color}")
def read_wines_by_color_endpoint(color:str):
    return read_wines_by_color(color)

@app.get("/quality")
def read_mean_quality_endpoint():
    return read_mean_quality()


@app.get("/quality/{color}")
def mean_quality_by_color_endpoint(color:str):
    return read_mean_quality_by_color(color)

@app.get("/alcohol/{vol}")
def read_wine_by_alcohol_vol_endpoint(vol:float):
    return read_wine_by_alchohol_vol(vol)

@app.get("/alcohol/{vol}/mean")
def read_mean_quality_by_alcohol_vol_endpoint(vol:float):
    return read_mean_quality_by_alcohol_vol(vol)