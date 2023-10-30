import sqlite3
import pandas as pd
import numpy as np
import json

#importo csv e creo due datframe in base al colore del vino
df_red=pd.read_csv('https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/wine_quality/winequality-red.csv', sep=';', encoding='latin1')
df_white=pd.read_csv('https://raw.githubusercontent.com/FabioGagliardiIts/datasets/main/wine_quality/winequality-white.csv', sep= ';', encoding='latin1')

#aggiungo in entrambi i dataframe una colonna per il colore del vino 
df_red.insert(0,'color','red')
df_white.insert(0,'color','white')

#Creo un unico dataframe con vino bianco e rosso. Ho fatto questa scelta per vedere se la qualità del vino può dipendere anche dal colore.
wine=[df_red,df_white]
df_wine=pd.concat(wine)
df_wine.insert(0, "id", range(0, 0+len(df_wine)))


#creo db
db = sqlite3.connect('database/sqlite3/db.sqlite')
cursor = db.cursor()
db.commit()

#creo una tabella a partire dal dataframe df_wine
df_wine.to_sql('wine', db, if_exists='replace', index=False)
db.commit()

#test del db(lo lascio commentato per non avere stampe nel terminale)
# query=cursor.execute('SELECT * FROM wine LIMIT 10')
# query=cursor.fetchall()
# print(query)

##########
#        #
#  CRUD  #
#        # 
##########


#funzione per collegarmi al db
def create_connection():
    connection = sqlite3.connect('database/sqlite3/db.sqlite')
    return connection

#READ
def read_all_wines():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM wine")
    result = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    connection.commit()
    connection.close()
    return result

def read_wines_by_color(color:str):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM wine WHERE color =?", (color,))
    result = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    connection.commit()
    connection.close()
    return result

def read_mean_quality():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT quality FROM wine")
    result = [cursor.fetchall()]
    connection.commit()
    connection.close()
    result=np.mean(result)
    return result

def read_mean_quality_by_color(color:str):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT quality FROM wine WHERE color =?", (color,))
    result = [cursor.fetchall()]
    connection.commit()
    connection.close()
    result=np.mean(result)
    return result

def read_wine_by_alchohol_vol(vol:float):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM wine WHERE  alcohol > ?", (vol,))
    result = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    connection.commit()
    connection.close()
    return result

def read_mean_quality_by_alcohol_vol(vol:float):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT quality FROM wine WHERE  alcohol > ?", (vol,))
    result = [cursor.fetchall()]
    connection.commit()
    connection.close()
    result=np.mean(result)
    return result

type=cursor.execute("SELECT * FROM wine where alcohol>12.3")
type=cursor.fetchall()
print(type)