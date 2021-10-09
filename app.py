import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

from separar import *
from graficas import *

# ----- CARGAR DATASET -----
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


# ----- ESTILOS -----
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
}
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# ----- SIDEBAR -----
sidebar = html.Div([
    html.H2("Trafico de Internet", className=""),
    html.Hr(),
    html.P(
        "A continuacion puede ver datos del trafico de internet durante la pandemia de distintos proveedores", className=""
    ),
    html.Hr(),
    dbc.Nav([
            dbc.NavLink("Tráfico Total", href="/", active="exact", className="text-light"),
            dbc.NavLink("Hora Pico", href="/Hora-Pico", active="exact", className="text-light"),
            dbc.NavLink("Tráfico Diario", href="/Trafico-Diario", active="exact", className="text-light"),
            dbc.NavLink("Tráfico Detallado", href="/Trafico-Detallado", active="exact", className="text-light"),
            dbc.NavLink("Dataset", href="/Dataset", active="exact", className="text-light")
        ], vertical=True, pills=True),
], style=SIDEBAR_STYLE, className="text-white bg-dark")

# ----- CONTENIDO -----
content = html.Div(id="page-content", style=CONTENT_STYLE)
mybtn = html.Button('botonXD', className='btn btn-primary')

# ----- CREACION DE LA APP -----
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# ----- CALLBACKS -----
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return grafico
    elif pathname == "/Hora-Pico":
        return grafico2
    elif pathname == "/Trafico-Diario":
        return grafico3
    elif pathname == "/Trafico-Detallado":
        return grafico4
    elif pathname == "/Dataset":
        return dataset
    
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

# ----- CORRER APP -----
if __name__ == '__main__':
    app.run_server(debug=True)