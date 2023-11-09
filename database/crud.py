import sqlite3
import numpy as np
from database.model import *


##########
#        #
#  CRUD  #
#        # 
##########


#funzione per collegarmi al db
def create_connection():
    connection = sqlite3.connect('database/sqlite3/db.sqlite')
    return connection

#CREATE

def create_wine(wine:Wine):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO wine(id, color, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (wine.id, wine.color, wine.fixed_acidity, wine.volatile_acidity, wine.citric_acid, wine.residual_sugar, wine.chlorides, wine.free_sulfur_dioxide, wine.total_sulfur_dioxide, wine.density, wine.pH, wine.sulphates, wine.alcohol, wine.quality),
    )
    connection.commit()
    connection.close()

#READ
#restituisce tutti i vini presenti nel db
def read_all_wines():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM wine")
    result = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    connection.commit()
    connection.close()
    return result

#accetta come parametro una stringa che permette di filtrare i vini in base al colore
def read_wines_by_color(color:str):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM wine WHERE color =?", (color,))
    result = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    connection.commit()
    connection.close()
    return result

#restituisce la qualità media per tutti i vini
def read_mean_quality():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT quality FROM wine")
    result = [cursor.fetchall()]
    connection.commit()
    connection.close()
    result=np.mean(result)
    return result

#reestituisce la qualità media dei vini filtrati per colore
def read_mean_quality_by_color(color:str):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT quality FROM wine WHERE color =?", (color,))
    result = [cursor.fetchall()]
    connection.commit()
    connection.close()
    result=np.mean(result)
    return result

#restituisce tutti i vini al di sopra di un determinato grado alcolico
def read_wine_by_alchohol_vol(vol:float):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM wine WHERE  alcohol > ?", (vol,))
    result = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    connection.commit()
    connection.close()
    return result

#restituisce la qualità media di tutti i vini al di sopra di un determinato grado alcolico
def read_mean_quality_by_alcohol_vol(vol:float):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT quality FROM wine WHERE  alcohol > ?", (vol,))
    result = [cursor.fetchall()]
    connection.commit()
    connection.close()
    result=np.mean(result)
    return result

def delete_wine_by_id(id:int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM wine WHERE id =?", (id,))
    connection.commit()
    connection.close()