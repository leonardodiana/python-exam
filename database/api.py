from fastapi import FastAPI
import sqlite3
from database.db import *
import numpy as np





app = FastAPI()


@app.get("/wine")
def read_all_wine_endpoint():
    return read_all_wines()