from dash import dcc
from dash import html
import plotly.express as px

def gr_barras(data_frame, eje_x, eje_y):
    fig = px.bar(data_frame, x=eje_x, y=eje_y, color=eje_x)
    return dcc.Graph(
        figure=fig
    )

def gr_barras_agr(data_frame, eje_x, eje_y):
    fig = px.bar(data_frame, x=eje_x, y=eje_y, barmode='group')
    return dcc.Graph(
        figure=fig
    )

def gr_puntos(data_frame, eje_x, eje_y, colores):
    fig = px.scatter(data_frame, x=eje_x, y=eje_y, color=colores)
    return dcc.Graph(
        figure=fig
    )

def gr_lineas(data_frame, eje_x, eje_y, colores):
    fig = px.line(data_frame, x=eje_x, y=eje_y, color=colores)
    return dcc.Graph(
        figure=fig
    )

def tabla(data_frame, max_rows=50):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in data_frame.columns])
        , className='table-dark'),
        html.Tbody([
            html.Tr([
                html.Td(data_frame.iloc[i][col]) for col in data_frame.columns
            ]) for i in range(min(len(data_frame), max_rows))
        ])
    ], className='table')
