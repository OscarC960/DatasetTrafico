import pandas as pd

def separar_columnas(data_frame, columnas):
    data_frame = data_frame[columnas]
    return data_frame

def separar_filas(data_frame, columna, filas):
    data_frame = data_frame[data_frame[columna].isin(filas)]
    return data_frame