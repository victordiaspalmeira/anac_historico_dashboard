from app import app
from dash.dependencies import Input, Output
from parsed_data import anac_df
from datetime import datetime as dt
import plotly.express as px
import re
import pandas as pd

@app.callback(
    Output('flight-depart-arrival-plot', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_depart_arrival(empname, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    
    plot_df = anac_df[anac_df['Sigla da Empresa'] == empname]
    plot_df = plot_df.loc[str(start):str(end)]
    return px.scatter(plot_df, y=plot_df['Chegada Prevista'], labels={"index": "Partida Prevista"})

@app.callback(
    Output('flight-duration-plot', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_flight_duration(empname, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    
    plot_df = anac_df[anac_df['Sigla da Empresa'] == empname]
    plot_df = plot_df.loc[str(start):str(end)]
    duracao_series = (plot_df['Chegada Real'] - plot_df['Partida Real']).div(pd.Timedelta('1H'))
    return px.scatter(plot_df, y=duracao_series, labels={"index": "Partida Prevista", "y": "Duração em horas"})

@app.callback(    
    Output('flight-status-plot', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_flight_status(empname, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    
    plot_df = anac_df[anac_df['Sigla da Empresa'] == empname]
    plot_df = plot_df.loc[str(start):str(end)]
    realizado = len(plot_df[plot_df['Situação do Voo'] == 'REALIZADO']) + len(plot_df[plot_df['Situação do Voo'] == 'Realizado'])
    cancelado = len(plot_df[plot_df['Situação do Voo'] == 'CANCELADO']) + len(plot_df[plot_df['Situação do Voo'] == 'Cancelado'])
    print(realizado, cancelado)
    return px.bar(plot_df, x=['Realizados', 'Cancelados'], y=[realizado, cancelado])    
