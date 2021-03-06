import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta, date
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

# ----- FUNCIONES GENERADORAS DE GRAFICOS -----

def gr_tr_total(rango_fechas, tipo_trafico):
    # Separar y agurpar los datos para el grafico
    df_gr = separar_filas(data_frame, 'FECHA_DEL_DIA_DE_TRAFICO', rango_fechas) # separar filas en ese rango de fechas
    df_gr = separar_columnas(df_gr, ['PROVEEDOR', tipo_trafico]) # separar las columnas que necesito
    df_gr = df_gr.groupby("PROVEEDOR").sum() # agrupar por proveedor y sumar el trafico
    df_gr = df_gr.rename_axis('PROVEEDOR').reset_index()

    # Generar grafica de barras
    return gr_barras(df_gr, 'PROVEEDOR', tipo_trafico)


def gr_hr_pico(rango_fechas):
    # Separar los datos para el grafico
    df_gr = separar_filas(data_frame, 'FECHA_DEL_DIA_DE_TRAFICO', rango_fechas) # separar filas en ese rango de fechas
    df_gr = separar_columnas(df_gr, ['PROVEEDOR', 'FECHA_DEL_DIA_DE_TRAFICO', 'HORA_PICO']) # separar las columnas que necesito
    df_gr['HORA_PICO'] = pd.to_datetime(df_gr['HORA_PICO']).dt.time # formatear la hora en formato datetime

    # Generar grafica de puntos
    return gr_puntos(df_gr, 'FECHA_DEL_DIA_DE_TRAFICO', 'HORA_PICO', 'PROVEEDOR')


def gr_tr_diario(rango_fechas, tipo_trafico):
    # Separar los datos para el grafico
    df_gr = separar_filas(data_frame, 'FECHA_DEL_DIA_DE_TRAFICO', rango_fechas) # separar filas en ese rango de fechas
    df_gr = separar_columnas(df_gr, ['PROVEEDOR', 'FECHA_DEL_DIA_DE_TRAFICO', tipo_trafico]) # separar las columnas que necesito

    # Generar grafica de puntos
    return gr_lineas(df_gr, 'FECHA_DEL_DIA_DE_TRAFICO', tipo_trafico, 'PROVEEDOR')


def gr_tr_detallado(rango_fechas):
    df_gr = separar_filas(data_frame, 'FECHA_DEL_DIA_DE_TRAFICO', rango_fechas) # separar filas en ese rango de fechas
    df_gr = separar_columnas(df_gr, ['PROVEEDOR', 'TRAFICO_DATOS_INTERNACIONAL_GB','TRAFICO_DATOS_NAP_COLOMBIA_GB','TRAFICO_DATOS_ACUERDOS_DE_TRANSITO_O_PEERING_DIRECTO_GB','TRAFICO_DATOS_LOCAL_GB','TRAFICO_DATOS_TOTAL_GB']) # separar las columnas que necesito
    df_gr = df_gr.groupby("PROVEEDOR").sum() # agrupar por proveedor y sumar el trafico
    df_gr = df_gr.rename_axis('PROVEEDOR').reset_index()

    # Generar grafica de barras agrupadas
    return gr_barras_agr(df_gr, 'PROVEEDOR', ['TRAFICO_DATOS_INTERNACIONAL_GB','TRAFICO_DATOS_NAP_COLOMBIA_GB','TRAFICO_DATOS_ACUERDOS_DE_TRANSITO_O_PEERING_DIRECTO_GB','TRAFICO_DATOS_LOCAL_GB'])


def tbl_dataset(rango_fechas):
    # filtrar el dataset
    df_tbl = separar_filas(data_frame, 'FECHA_DEL_DIA_DE_TRAFICO', rango_fechas) # filtar un rango de fechas

    # Generar tabla del dataset
    return tabla(df_tbl)


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
            dbc.NavLink("Tr??fico Total", href="/", active="exact", className="text-light"),
            dbc.NavLink("Hora Pico", href="/Hora-Pico", active="exact", className="text-light"),
            dbc.NavLink("Tr??fico Diario", href="/Trafico-Diario", active="exact", className="text-light"),
            dbc.NavLink("Tr??fico Detallado", href="/Trafico-Detallado", active="exact", className="text-light"),
            dbc.NavLink("Dataset", href="/Dataset", active="exact", className="text-light")
        ], vertical=True, pills=True),
], style=SIDEBAR_STYLE, className="text-white bg-dark")

# ----- CONTENIDO -----
filtro_fecha = dcc.DatePickerRange(
    id='input_fecha',
    min_date_allowed=date(2020, 3, 30),
    max_date_allowed=date(2021, 9, 21),
    initial_visible_month=date(2020, 5, 20),
    
    start_date=date(2020, 5, 20),
    end_date=date(2020, 5, 30)
)
filtro_tipo_tr = dcc.Dropdown(
    id="filtro",
    options=[
        {"label": 'Tr??fico Internacional', "value": 'TRAFICO_DATOS_INTERNACIONAL_GB'},
        {"label": 'Tr??fico NAP Colombia', "value": 'TRAFICO_DATOS_NAP_COLOMBIA_GB'},
        {"label": 'Tr??fico Peering', "value": 'TRAFICO_DATOS_ACUERDOS_DE_TRANSITO_O_PEERING_DIRECTO_GB'},
        {"label": 'Tr??fico Local', "value": 'TRAFICO_DATOS_LOCAL_GB'},
        {"label": 'Todo el Tr??fico', "value": 'TRAFICO_DATOS_TOTAL_GB'}],
    value="TRAFICO_DATOS_TOTAL_GB",
)
filtros = dbc.Row([
    dbc.Col(filtro_fecha),
    dbc.Col(filtro_tipo_tr)
],id='filtros')
content = html.Div([
    html.H2(id='titulo'),
    filtros,
    html.Div(id='grafico')
], id="page-content", style=CONTENT_STYLE)


# ----- CREACION DE LA APP -----
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# ----- CALLBACKS -----
@app.callback(
    Output("titulo", "children"), 
    Input("url", "pathname"))
def cambiar_titulo(pathname):
    if pathname == "/":
        return 'Trafico total en un rango de fechas'
    elif pathname == "/Hora-Pico":
        return 'Hora pico de cada dia en un rango de fechas'
    elif pathname == "/Trafico-Diario":
        return 'Trafico diario en un rango de fechas'
    elif pathname == "/Trafico-Detallado":
        return 'Todos los tipos de trafico en un rango de fechas'
    elif pathname == "/Dataset":
        return 'Registros del dataset'
    
    return html.Div('Error al cargar el sitio')

@app.callback( 
    Output('filtros', 'children'),
    Input("url", "pathname"))
def cambiar_filtros(pathname):
    if pathname == "/":
        filtro_tipo_tr.disabled = False
    elif pathname == "/Hora-Pico":
        filtro_tipo_tr.disabled = True
    elif pathname == "/Trafico-Diario":
        filtro_tipo_tr.disabled = False
    elif pathname == "/Trafico-Detallado":
        filtro_tipo_tr.disabled = True
    elif pathname == "/Dataset":
        filtro_tipo_tr.disabled = True
    
    return filtros.children

@app.callback(
    Output('grafico', 'children'),
    Input('input_fecha', 'start_date'),
    Input('input_fecha', 'end_date'),
    Input("url", "pathname"),
    Input('filtro', 'value'))
def cambiar_grafico(start_date, end_date, pathname, value):

    if start_date is not None:
        fecha_inicial = date.fromisoformat(start_date)
    if end_date is not None:
        fecha_final = date.fromisoformat(end_date)
    
    # crear el rango de fechas
    rango_fechas = [fecha_inicial + timedelta(days=d) for d in range((fecha_final - fecha_inicial).days + 1)] 
    rango_fechas = [f.strftime('%#d-%#m-%Y') for f in rango_fechas]

    if pathname == "/":
        return gr_tr_total(rango_fechas, value)
    elif pathname == "/Hora-Pico":
        return gr_hr_pico(rango_fechas)
    elif pathname == "/Trafico-Diario":
        return gr_tr_diario(rango_fechas, value)
    elif pathname == "/Trafico-Detallado":
        return gr_tr_detallado(rango_fechas)
    elif pathname == "/Dataset":
        return tbl_dataset(rango_fechas)
    
    return dbc.Jumbotron([
        html.H1("404: sitio no encontrado", className="text-danger"),
        html.Hr(),
        html.P(f"El sitio {pathname} no se fue encontrado..."),
    ])

# ----- CORRER APP -----
if __name__ == '__main__':
    app.run_server(debug=True)