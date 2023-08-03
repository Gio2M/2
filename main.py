from fastapi import FastAPI
import pandas as pd
#from pydantic import BaseModel
#from typing import Optional


# Ruta al archivo JSON
file_path = '../PI MLOps - STEAM/steam_games.json'

# Leer el archivo JSON línea por línea y cargar los datos en una lista
data_list = []
with open(file_path, 'r') as f:
    for line in f:
        data_list.append(eval(line.strip()))

# Crear DataFrame a partir de la lista de diccionarios
df = pd.DataFrame(data_list)


# Función para obtener juegos por año
def juegos_por_año(df, año):

    # Convertir el año a entero
    #año = int(año)

    # Filtrar el DataFrame para obtener solo los juegos del año proporcionado
    juegos_del_año = df[df['release_date'].str.startswith((año)) & pd.notna(df['release_date'])]

    # Validar si se encontraron juegos para el año dado
    if juegos_del_año.empty:
        return f"No se encontraron juegos para el año {año}"

    # Obtener la lista de nombres de juegos y ordenarla alfabéticamente
    lista_juegos = sorted(juegos_del_año['app_name'].tolist())

    # Devolver la lista de juegos ordenada alfabéticamente
    return lista_juegos

app = FastAPI()

# Endpoint para obtener juegos por año
@app.get("/juegos/{Anio}")
def juegos(Anio: str):
    return juegos_por_año(df, Anio)















# app = FastAPI()

# class Libro(BaseModel):
#      titulo: str
#      autor: str
#      paginas: int
#      editorial: Optional [str]


# @app.get("/")
# def index():
#     return {"Mensaje" : "Mi Primera API"}

# @app.get("/Libros/{Id}")
# def mostrar_libro(Id: int):
#     return {"data" : Id}

# @app.post("/Libros")
# def insertar_libro(Libro: Libro):
#     return {"mensaje" : f"Libro {Libro.titulo} insertado"}