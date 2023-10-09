import pandas as pd

def cargar_datos(ruta):
    datos = pd.read_csv(ruta)
    return datos

