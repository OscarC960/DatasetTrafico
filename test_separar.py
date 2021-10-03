from os import sep
import pandas as pd
from separar import *

data_frame = pd.read_csv('Dataset_TD.csv', 
        sep=';', 
        decimal=',')

def test_separar_columnas():
    columnas = ['PROVEEDOR', 'TRAFICO_DATOS_TOTAL_GB']
        
    col = list(separar_columnas(data_frame, columnas).columns.values)

    assert columnas == col

def test_separar_filas():
    columna = 'FECHA_DEL_DIA_DE_TRAFICO'
    filas = ['7-4-2020', '7-5-2020', '1-5-2020']

    fil = list(separar_filas(data_frame, columna, filas)[columna])

    for f in fil:
        if f not in filas:
            assert False

    assert True