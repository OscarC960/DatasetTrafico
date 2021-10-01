import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

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

Titulo = 'Dataset'

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


# Generar tabla del dataset
def generate_table(dataframe, max_rows=50):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns]),
            className='table-dark'),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ], className='table')


# Crear la aplicacion
app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)

# Layout de la aplicacion
app.layout = html.Div(children=[
    html.H1(Titulo),

    html.Div([
        html.H3('50 Columnas del dataset:'),
        generate_table(data_frame)
    ])
])


# Correr la aplicacion
if __name__ == '__main__':
    app.run_server(debug=True)
