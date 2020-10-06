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
    plot_df.index = pd.to_datetime(anac_df['Partida Real'])
    plot_df = plot_df.loc[str(start):str(end)]

    if(empname != None):
        plot_df = plot_df[plot_df['Sigla da Empresa'].isin(empname)]
    if(origin != None):
        plot_df = plot_df[plot_df['Aeroporto Origem'].isin(origin)]
    if(destination != None):
        plot_df = plot_df[plot_df['Aeroporto Destino'].isin(destination)]
    try:
        plot = px.scatter(plot_df, y=plot_df['Chegada Real'], labels={"index": "Partida Real"}, color='Sigla da Empresa', title='Partida e Chegada de Voo')
    except:
        print("---- ERROR ----")
        plot = None
        print(empname, origin, destination, start_date, end_date)
        print(plot_df)
    return plot


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
    plot_df.index = pd.to_datetime(anac_df['Partida Real'])
    plot_df = plot_df.loc[str(start):str(end)]

    if(empname != None and empname != []):
        plot_df = plot_df[plot_df['Sigla da Empresa'].isin(empname)]
    if(origin != None and origin != []):
        plot_df = plot_df[plot_df['Aeroporto Origem'].isin(origin)]
    if(destination != None and destination != []):
        plot_df = plot_df[plot_df['Aeroporto Destino'].isin(destination)]

    duracao_series = (plot_df['Chegada Real'] -
                      plot_df['Partida Real']).div(pd.Timedelta('1H'))
    try:
        plot = px.scatter(plot_df, y=duracao_series, labels={"index": "Partida Real", "y": "Duração em horas"}, color='Sigla da Empresa', title='Duração de Voo')
    except:
        print("---- ERROR ----")
        plot = None
        print(empname, origin, destination, start_date, end_date)
        print(plot_df)
    return plot


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
    plot_df.index = pd.to_datetime(anac_df['Partida Prevista'])
    plot_df = plot_df.loc[str(start):str(end)]
    if(empname != None and empname != []):
        plot_df = plot_df[plot_df['Sigla da Empresa'].isin(empname)]
    if(origin != None and origin != []):
        plot_df = plot_df[plot_df['Aeroporto Origem'].isin(origin)]
    if(destination != None and destination != []):
        plot_df = plot_df[plot_df['Aeroporto Destino'].isin(destination)]
    try:
        plot = px.histogram(plot_df, x='Situação do Voo', color='Sigla da Empresa', barmode='group', title="Situação do Voo")
    except:
        print("---- ERROR ----")
        plot = None
        print(empname, origin, destination, start_date, end_date)
        print(plot_df)
    return plot

@app.callback(
    Output('flight_airports_pair', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('origem-select', 'value')],
    [Input('destino-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_flight_airports_pair(empname, origin, destination, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    plot_df = anac_df
    plot_df.index = pd.to_datetime(anac_df['Partida Prevista'])
    plot_df = plot_df.loc[str(start):str(end)]
    if(empname != None and empname != []):
        plot_df = plot_df[plot_df['Sigla da Empresa'].isin(empname)]
    if(origin != None and origin != []):
        plot_df = plot_df[plot_df['Aeroporto Origem'].isin(origin)]
    if(destination != None and destination != []):
        plot_df = plot_df[plot_df['Aeroporto Destino'].isin(destination)]
    try:
        plot = px.scatter(plot_df, x='Aeroporto Origem', y='Aeroporto Destino', color='Sigla da Empresa', title="Aeroporto Origem vs Aeroporto Destino")
    except:
        print("---- ERROR ----")
        plot = None
        print(empname, origin, destination, start_date, end_date)
        print(plot_df)
    return plot