import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

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
    data_frame = data_frame[data_frame.PROVEEDOR.isin(["CLARO", "ETB", "UNE", "MOVISTAR", "EMCALI", "AVANTEL", "VIRGIN"])]
    Titulo = "Trafico de datos de internet durante la pandemia"
    error = False
except:
    Titulo = "No se encontro el Dataset"
    error = True

# Tratamiento de datos
if not error:
    # -------- VER TRAFICO DE DATOS SUMADO EN UN RANGO DE FECHAS --------
    # Definir un rango de fechas
    fecha_inicial = datetime(2020,5,20)
    fecha_final = datetime(2020,5,30)
    rango_fechas = [fecha_inicial + timedelta(days=d) for d in range((fecha_final - fecha_inicial).days + 1)] 
    rango_fechas = [f.strftime('%#d-%#m-%Y') for f in rango_fechas]

    # Separar y agurpar los datos para el grafico
    df_gr1 = separar_filas(data_frame, 'FECHA_DEL_DIA_DE_TRAFICO', rango_fechas) # separar filas en ese rango de fechas
    df_gr1 = separar_columnas(df_gr1, ['PROVEEDOR', 'TRAFICO_DATOS_INTERNACIONAL_GB']) # separar las columnas que necesito
    df_gr1 = df_gr1.groupby("PROVEEDOR").sum() # agrupar por proveedor y sumar el trafico
    df_gr1 = df_gr1.rename_axis('PROVEEDOR').reset_index()

    # Generar grafica de barras
    grafico = gr_barras(df_gr1, 'PROVEEDOR', 'TRAFICO_DATOS_INTERNACIONAL_GB')


    # -------- VER HORA PICO UN RANGO DE FECHAS --------
    # Separar los datos para el grafico
    df_gr2 = separar_filas(data_frame, 'FECHA_DEL_DIA_DE_TRAFICO', rango_fechas) # separar filas en ese rango de fechas
    df_gr2 = separar_columnas(df_gr2, ['PROVEEDOR', 'FECHA_DEL_DIA_DE_TRAFICO', 'HORA_PICO']) # separar las columnas que necesito
    df_gr2['HORA_PICO'] = pd.to_datetime(df_gr2['HORA_PICO'], format="%H:%M") # formatear la hora en formato datetime
    
    # Generar grafica de puntos
    grafico2 = gr_puntos(df_gr2, 'FECHA_DEL_DIA_DE_TRAFICO', 'HORA_PICO', 'PROVEEDOR')


    # -------- VER TRAFICOS DE DATOS AGRUPADOS EN UN RANGO DE FECHAS --------
    # Separar los datos para el grafico
    df_gr3 = separar_filas(data_frame, 'FECHA_DEL_DIA_DE_TRAFICO', rango_fechas) # separar filas en ese rango de fechas
    df_gr3 = separar_columnas(df_gr3, ['PROVEEDOR', 'FECHA_DEL_DIA_DE_TRAFICO', 'TRAFICO_DATOS_LOCAL_GB']) # separar las columnas que necesito
    
    # Generar grafica de puntos
    grafico3 = gr_lineas(df_gr3, 'FECHA_DEL_DIA_DE_TRAFICO', 'TRAFICO_DATOS_LOCAL_GB', 'PROVEEDOR')

    # Separar y agurpar los datos para el grafico 4
    df_gr4 = separar_filas(data_frame, 'FECHA_DEL_DIA_DE_TRAFICO', rango_fechas) # separar filas en ese rango de fechas
    df_gr4 = separar_columnas(df_gr4, ['PROVEEDOR', 'TRAFICO_DATOS_INTERNACIONAL_GB','TRAFICO_DATOS_NAP_COLOMBIA_GB','TRAFICO_DATOS_ACUERDOS_DE_TRANSITO_O_PEERING_DIRECTO_GB','TRAFICO_DATOS_LOCAL_GB','TRAFICO_DATOS_TOTAL_GB']) # separar las columnas que necesito
    df_gr4 = df_gr4.groupby("PROVEEDOR").sum() # agrupar por proveedor y sumar el trafico
    df_gr4 = df_gr4.rename_axis('PROVEEDOR').reset_index()

    # Generar grafica de barras agrupadas
    grafico4 = gr_barras_agr(df_gr4, 'PROVEEDOR', ['TRAFICO_DATOS_INTERNACIONAL_GB','TRAFICO_DATOS_NAP_COLOMBIA_GB','TRAFICO_DATOS_ACUERDOS_DE_TRANSITO_O_PEERING_DIRECTO_GB','TRAFICO_DATOS_LOCAL_GB'])

    #-------- VER TRAFICO DE DATOS TOTAL EN UN RANGO DE FECHAS --------
    #Separar los datos para el grafico
    df_gr5 = separar_filas(data_frame, 'FECHA_DEL_DIA_DE_TRAFICO', rango_fechas) # separar filas en ese rango de fechas
    df_gr5 = separar_columnas(df_gr5, ['PROVEEDOR', 'FECHA_DEL_DIA_DE_TRAFICO', 'TRAFICO_DATOS_ACUERDOS_DE_TRANSITO_O_PEERING_DIRECTO_GB']) # separar las columnas que necesito
    
    #Generar grafica de puntos para trafico de datos con acuerdos
    grafico5 = gr_lineas(df_gr5, 'FECHA_DEL_DIA_DE_TRAFICO', 'TRAFICO_DATOS_ACUERDOS_DE_TRANSITO_O_PEERING_DIRECTO_GB', 'PROVEEDOR')

    # -------- VER ENTRADAS DEL DATASET --------
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
layout = []
layout.extend([
    dcc.ConfirmDialog(
        id='error',
        message='No se pudo cargar el Dataset',
        displayed=error
    ), 
    html.H1(Titulo, className='m-5'),
])
if not error:
    layout.extend([
        html.Div([
            html.H3('Grafica de barras de trafico total en un rango de fechas por cada proveedor'),
            grafico,
            html.H3('Grafica de puntos de hora pico en un rango de fechas por cada proveedor'),
            grafico2,
            html.H3('Grafica de lineas de trafico local en un rango de fechas por cada proveedor'),
            grafico3,
            html.H3('Grafica de barras de trafico total en un rango de fechas por cada proveedor.'),
            grafico4,
            html.H3('Grafica de lineas de cantidad de GB de tráfico por modalidad/acuerdos peering por cada proveedor.'),
            grafico5,
            html.H3('Dataset con filtros de proveedor, rango de fechas y rango de trafico local:'),
            dataset
        ])
    ])

app.layout = html.Div(layout)


# Correr la aplicacion
if __name__ == '__main__':
    app.run_server(debug=True)