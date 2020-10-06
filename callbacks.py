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
    [Input('origem-select', 'value')],
    [Input('destino-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_depart_arrival(empname, origin, destination, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    plot_df = anac_df
    plot_df = plot_df.loc[str(start):str(end)]

    if(empname != None):
        plot_df = plot_df[plot_df['Sigla da Empresa'].isin(empname)]
    else:
        print(empname)
    if(origin != None):
        plot_df = plot_df[plot_df['Aeroporto Origem'] == origin]
    if(destination != None):
        plot_df = plot_df[plot_df['Aeroporto Destino'] == destination]

    return px.scatter(plot_df, y=plot_df['Chegada Prevista'], labels={"index": "Partida Prevista"}, color='Sigla da Empresa')


@app.callback(
    Output('flight-duration-plot', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('origem-select', 'value')],
    [Input('destino-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_flight_duration(empname, origin, destination, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    plot_df = anac_df
    plot_df = plot_df.loc[str(start):str(end)]

    if(empname != None):
        plot_df = plot_df[plot_df['Sigla da Empresa'].isin(empname)]
    else:
        print(empname)
    if(origin != None):
        plot_df = plot_df[plot_df['Aeroporto Origem'] == origin]
    if(destination != None):
        plot_df = plot_df[plot_df['Aeroporto Destino'] == destination]

    duracao_series = (plot_df['Chegada Real'] -
                      plot_df['Partida Real']).div(pd.Timedelta('1H'))
    return px.scatter(plot_df, y=duracao_series, labels={"index": "Partida Prevista", "y": "Duração em horas"}, color='Sigla da Empresa')


@app.callback(
    Output('flight-status-plot', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('origem-select', 'value')],
    [Input('destino-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_flight_status(empname, origin, destination, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')

    plot_df = anac_df
    plot_df = plot_df.loc[str(start):str(end)]

    if(empname != None):
        plot_df = plot_df[plot_df['Sigla da Empresa'].isin(empname)]
    if(origin != None):
        plot_df = plot_df[plot_df['Aeroporto Origem'] == origin]
    if(destination != None):
        plot_df = plot_df[plot_df['Aeroporto Destino'] == destination]

    return px.histogram(x=plot_df['Situação do Voo'])
