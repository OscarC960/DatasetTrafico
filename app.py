import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

from separar import *
from graficas import *


# JavaScript Externos (Bootstrap)
external_scripts = [
    {
        'src': 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js',
        'integrity': 'sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ',
        'crossorigin': 'anonymous'
    }
]

# CSS Externos (Bootstrap)
external_stylesheets = [
    {
        'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU',
        'crossorigin': 'anonymous'
    }
]

# Cargar dataset
try:
    data_frame = pd.read_csv('https://www.postdata.gov.co/sites/default/files/datasets/data/Monitoreo%20de%20Tr%C3%A1fico%20de%20Internet%20-%20Trafico%20Diario_131.csv', 
        sep=';', 
        decimal=',')
except:
    data_frame = pd.read_csv('Dataset_TD.csv', 
        sep=';', 
        decimal=',')
finally:
    data_frame = data_frame[data_frame.PROVEEDOR.isin(["CLARO", "ETB", "UNE", "MOVISTAR", "EMCALI", "AVANTEL", "VIRGIN"])]

# Definir un rango de fechas
fecha_inicial = datetime(2020,5,20)
fecha_final = datetime(2020,5,30)
rango_fechas = [fecha_inicial + timedelta(days=d) for d in range((fecha_final - fecha_inicial).days + 1)] 
rango_fechas = [f.strftime('%#d-%#m-%Y') for f in rango_fechas]

# Separar y agurpar los datos para el grafico
df_gr = separar_filas(data_frame, 'FECHA_DEL_DIA_DE_TRAFICO', rango_fechas) # separar filas en ese rango de fechas
df_gr = separar_columnas(df_gr, ['PROVEEDOR', 'TRAFICO_DATOS_INTERNACIONAL_GB']) # separar las columnas que necesito
df_gr = df_gr.groupby("PROVEEDOR").sum() # agrupar por proveedor y sumar el trafico
df_gr = df_gr.rename_axis('PROVEEDOR').reset_index()

# Genrar grafica de barras
grafico = gr_barras(df_gr, 'PROVEEDOR', 'TRAFICO_DATOS_INTERNACIONAL_GB')


# filtrar el dataset
df_tbl = separar_filas(data_frame, 'FECHA_DEL_DIA_DE_TRAFICO', rango_fechas) # filtar un rango de fechas
df_tbl = separar_filas(df_tbl, 'PROVEEDOR', ['MOVISTAR', 'ETB']) # filtrar unos proveedores
rango_trafico = [r for r in range(300000, 600000)] 
df_tbl = separar_filas(df_tbl, 'TRAFICO_DATOS_LOCAL_GB', rango_trafico) # filtrar un rango de trafico

# Generar tabla del dataset
dataset = tabla(df_tbl)


# Crear la aplicacion
app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)

# Layout de la aplicacion
app.layout = html.Div([
    html.Div([
        html.H3('Grafica de barras de trafico total en un rango de fechas por cada proveedor'),
        grafico,
        html.H3('Dataset con filtros de proveedor, rango de fechas y rango de trafico local:'),
        dataset
    ])
])


# Correr la aplicacion
if __name__ == '__main__':
    app.run_server(debug=True)
