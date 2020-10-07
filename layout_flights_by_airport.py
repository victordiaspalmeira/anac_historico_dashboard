import pandas as pd
from datetime import datetime as dt
from app import app
from parsed_data import anac_df
from data_helpers import slice_data
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from parsed_data import anac_df, grp_empresas, aero_origem, aero_destino
import numpy as np
import re
import dash


layout_flights_by_origin_airport = html.Div([
    dcc.Graph('flights-by-origin-airpot-plot',  config={'displayModeBar': True})],
    style={"flex": "1"}
)


@app.callback(
    Output('flights-by-origin-airpot-plot', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('origem-select', 'value')],
    [Input('destino-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_flights_by_origin_airport(empname, origin, destination, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    plot_df = slice_data(anac_df, empname, origin, None, start, end)

    plot_df.index = pd.to_datetime(plot_df['Partida Real'])
    plot_df = plot_df.loc[str(start):str(end)]

    if plot_df.empty:
        print("Não há dados.")
        return px.scatter(title="Voos por Aeorporto (Origem)")
    return px.histogram(plot_df, color='Situação do Voo', x='Aeroporto Origem', barmode='group', title="Quantidade de Voos por Aeroporto (Origem)")


layout_flights_by_destination_airport = html.Div([
    dcc.Graph('flights-by-destination-airpot-plot',  config={'displayModeBar': True})],
    style={"flex": "1"}
)


@app.callback(
    Output('flights-by-destination-airpot-plot', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('origem-select', 'value')],
    [Input('destino-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_flights_by_destination_airport(empname, origin, destination, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    plot_df = slice_data(anac_df, empname, None, destination, start, end)

    plot_df.index = pd.to_datetime(plot_df['Partida Real'])
    plot_df = plot_df.loc[str(start):str(end)]

    if plot_df.empty:
        print("Não há dados.")
        return px.scatter(title="Voos por Aeorporto (Destino)")
    return px.histogram(plot_df, color='Situação do Voo', x='Aeroporto Destino', barmode='group', title="Quantidade de Voos por Aeroporto (Destino)")
