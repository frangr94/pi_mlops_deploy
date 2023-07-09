# iniciar con comando terminal : uvicorn app:app --reload
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text,Optional
from datetime import datetime
import pandas as pd
import numpy as np

app = FastAPI()


df = pd.read_csv('datasets/data_api.csv')

df['prod_companies']=df.prod_companies.str.strip('''""''') # tuve que emparchar esto

@app.get('/')
def read_root():
    return {'0':'Bienvenido a movies REST API. Para obtener datos complete el URL o ingrese a /docs',
            '1':'/count_lang/en',
            '2':'/duracion_pelicula/Toy Story',
            '3':'/franquicia/Toy Story Collection',
            '4': '/count_pais/US',
            '5':'/productoras/Pixar Animation Studios',
            '6':'/directores/John Lasseter',
            '7':'/recomendacion/Toy Story'
            }


# devuelve la cantidad de peliculas producidas en x idioma
@app.get('/count_lang/{Idioma}')
def peliculas_idioma(Idioma: str):

    count=0
    for i in df.langs_unn:
        if Idioma in i:
            count+=1

    respuesta=[{'idioma':Idioma,'cantidad':count}]

    return respuesta

# devuelve duracion y año de una pelicula
@app.get('/duracion_pelicula/{Pelicula}')
def get_duracion(Pelicula: str):

    row=df.loc[df.original_title==Pelicula]
    #row = df[df['original_title'].str.contains(Pelicula)]
    nombre =row.original_title.values[0]
    año = row.release_year.values[0]
    duracion = row.runtime.values[0]

    # respuesta='La pelicula {} dura {} minutos y fue estrenada en {}'.format(nombre,duracion,año)

    respuesta=[{'title':str(nombre),'runtime':int(duracion),'released':int(año)}]

    
    return respuesta

# devuelve cantidad de peliculas, ganancias totales y promedio
@app.get('/franquicia/{Franquicia}')
def franquicia(Franquicia: str):

    rows=df.loc[df.collection_unn==Franquicia]
    cantidad_peliculas = len(rows)
    ganancia_total = rows['revenue'].sum()
    ganancia_promedio = ganancia_total/cantidad_peliculas

    
    respuesta=[{'franquicia':Franquicia,'producciones':cantidad_peliculas,'ganancia_total':ganancia_total,'ganancia_promedio':ganancia_promedio}]

    return respuesta

# devuelve la cantidad de peliculas producidas en un pais
@app.get('/count_pais/{Pais}')
def peliculas_pais( Pais: str ):
    count = 0
    for i in df.prod_countries_unn:
        if Pais in i:
            count+=1
    
    respuesta=[{'pais':Pais,'cantidad':count}]

    return respuesta

# devuelve el revenue total y cantidad de peliculas realizadas
@app.get('/productoras/{Productora}')
def productoras_exitosas( Productora: str ):
    rows = df.loc[df.prod_companies.str.contains(Productora)]
    cantidad_peliculas = len(rows)
    ingresos = rows['revenue'].sum()

    respuesta=[{'productora':Productora,'cantidad_peliculas':cantidad_peliculas,'ingresos':ingresos}]
    return respuesta

# devuelve el exito de un director, junto a una lista de peliculas con estadisticas
@app.get('/directores/{nombre_director}')

def get_director(nombre_director: str):
    rows = df.loc[df.directors.str.contains(nombre_director)]
    ingresos = np.average(rows['return'])
    values=['original_title','release_date','revenue','budget','return']
    peliculas=[]
    for index, row in rows.iterrows():
        v=row[values].to_dict()
        peliculas.append(v)

    resultado={'director':nombre_director,'ingresos':ingresos}
    return resultado,peliculas


# vecinos recomendacion
df_r = pd.read_csv('datasets/data_modelado_nn.csv')

# tomar titulos como indice
df_r.replace(np.nan,0,inplace=True)
df_r.genres_unn.replace(0,'none',inplace=True)
indexes = df_r.title

# voy a probar quedarme solo con tres columnas para ohe para no quedarme sin ram en Render
df_r.drop(columns=['title','langs_unn'],inplace=True)

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder()

numerical=['budget','popularity','revenue','runtime','vote_average']
categorical=['genres_unn','cast_unn','prod_companies','prod_countries_unn','directors']

# crear arrays para el modelo
data=[]
for i in df_r:
    if i in numerical:
        data.append(np.array(df_r[[i]]).reshape(-1,1))
    elif i in categorical:
        data.append(ohe.fit_transform(df_r[[i]]).toarray())
    else:
        continue

# stackear arrays
X = np.hstack(data)

from sklearn.neighbors import NearestNeighbors

@app.get('/recomendacion/{title}')
def recomendador(title: str):


    reccomender = NearestNeighbors(n_neighbors=6, algorithm='auto') # instanciar modelo

    reccomender.fit(X) # ajustar datos

    idx = indexes[indexes == title].index[0] # recuperar indice

    query_point = np.array([X[idx]]) # tomar datos del indice requerido

    distances,indices = reccomender.kneighbors(query_point) # unpack kneightbors, necesito distances porque devuelve dos valores

    resultado=[]
    for i in indices:
        if i != title:
            resultado.append(indexes[i]) # crear lista de resultados
            
    
    return resultado