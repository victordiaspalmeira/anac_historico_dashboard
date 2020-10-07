from app import app
from dash.dependencies import Input, Output
from parsed_data import anac_df
from datetime import datetime as dt
import plotly.express as px
import re
import pandas as pd

def slice_data(df, empname, origin, destination, start, end):
    plot_df = df
    if empname == []:
        empname = None
    if origin == []:
        origin = None
    if destination == []:
        destination = None
    if(empname != None):
        plot_df = plot_df[plot_df['Sigla da Empresa'].isin(empname)]
    if(origin != None):
        plot_df = plot_df[plot_df['Aeroporto Origem'].isin(origin)]
    if(destination != None):
        plot_df = plot_df[plot_df['Aeroporto Destino'].isin(destination)]

    return plot_df

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
    plot_df = slice_data(anac_df, empname, origin, destination, start, end)
    plot_df.index = pd.to_datetime(plot_df['Partida Real'])
    plot_df = plot_df.loc[str(start):str(end)]
    print(empname, origin, destination, start, end)
    if plot_df.empty:
        print("Não há dados.")
        return px.scatter(title="Partida e Chegada de Voo")    
    return px.scatter(plot_df, y=plot_df['Chegada Real'], labels={"index": "Partida Real"}, color='Sigla da Empresa', title='Partida e Chegada de Voo')

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
    plot_df = slice_data(anac_df, empname, origin, destination, start, end)
    plot_df.index = pd.to_datetime(plot_df['Partida Real'])
    plot_df = plot_df[plot_df['Situação do Voo'].isin(['Realizado'])]
    plot_df = plot_df.loc[str(start):str(end)]
    duracao_series = (plot_df['Chegada Real'] -
                      plot_df['Partida Real']).div(pd.Timedelta('1H'))

    print(empname, origin, destination, start, end)
    if plot_df.empty:
        print("Não há dados.")
        return px.scatter(title="Duração de Voo")
    return px.scatter(plot_df, y=duracao_series, labels={"index": "Partida Real", "y": "Duração (horas)"}, color='Sigla da Empresa', title='Duração de Voo')

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
    plot_df = slice_data(anac_df, empname, origin, destination, start, end)
    
    plot_df.index = pd.to_datetime(plot_df['Partida Real'])
    plot_df = plot_df.loc[str(start):str(end)]

    print(empname, origin, destination, start, end)
    if plot_df.empty:
        print("Não há dados.")
        return px.scatter(title="Situação do Voo")
    return px.histogram(plot_df, color='Situação do Voo', x='Sigla da Empresa', barmode='group', title="Situação do Voo")


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
    plot_df = slice_data(anac_df, empname, origin, destination, start, end)
    plot_df.index = pd.to_datetime(plot_df['Partida Real'])
    
    plot_df = plot_df.loc[str(start):str(end)]

    print(empname, origin, destination, start, end)
    if plot_df.empty:
        print("Não há dados.")
        return px.scatter(title="Aeroporto Origem vs Aeroporto Destino")
    return px.scatter(plot_df, x='Aeroporto Origem', y='Aeroporto Destino', color='Sigla da Empresa', title="Aeroporto Origem vs Aeroporto Destino")

@app.callback(
    Output('flight-type-plot', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('origem-select', 'value')],
    [Input('destino-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_flight_type(empname, origin, destination, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    plot_df = slice_data(anac_df, empname, origin, destination, start, end)
    
    plot_df.index = pd.to_datetime(plot_df['Partida Real'])
    plot_df = plot_df.loc[str(start):str(end)]

    print(empname, origin, destination, start, end)
    if plot_df.empty:
        print("Não há dados.")
        return px.scatter(title="Tipo de Linha")
    return px.histogram(plot_df, color='Tipo de linha', x='Sigla da Empresa', barmode='group', title="Tipo de Linha")

@app.callback(
    Output('flight-depart-delay-plot', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('origem-select', 'value')],
    [Input('destino-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_flight_depart_delay(empname, origin, destination, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    plot_df = slice_data(anac_df, empname, origin, destination, start, end)
    
    plot_df.index = pd.to_datetime(plot_df['Partida Real'])
    plot_df = plot_df[plot_df['Situação do Voo'].isin(['Realizado'])]
    plot_df = plot_df.loc[str(start):str(end)]
    #atraso_series = (plot_df['Partida Real'] -
    #    plot_df['Partida Prevista']).div(pd.Timedelta('1minute'))
    atraso_series = ((pd.to_datetime(plot_df['Partida Real']) - pd.to_datetime(plot_df['Partida Prevista'])).dt.total_seconds() / 60)
    print(atraso_series)
    print(empname, origin, destination, start, end)
    if plot_df.empty:
        print("Não há dados.")
        return px.scatter(title="Atrasos na decolagem")
    return px.scatter(plot_df, y=atraso_series.where(atraso_series > 0), labels={"index": "Partida Real", "y": "Atraso (minutos)"}, color='Sigla da Empresa', title='Atrasos na decolagem')


@app.callback(
    Output('flight-arrival-delay-plot', 'figure'),
    [Input('empresa-select', 'value')],
    [Input('origem-select', 'value')],
    [Input('destino-select', 'value')],
    [Input('periodo', 'start_date'),
     Input('periodo', 'end_date')]
)
def update_graph_flight_arrival_delay(empname, origin, destination, start_date, end_date):
    start = dt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    end = dt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    plot_df = slice_data(anac_df, empname, origin, destination, start, end)

    plot_df.index = pd.to_datetime(plot_df['Partida Real'])
    plot_df = plot_df[plot_df['Situação do Voo'].isin(['Realizado'])]
    plot_df = plot_df.loc[str(start):str(end)]
    #atraso_series = (plot_df['Partida Real'] -
    #    plot_df['Partida Prevista']).div(pd.Timedelta('1minute'))
    atraso_series = ((pd.to_datetime(plot_df['Chegada Real']) - pd.to_datetime(plot_df['Chegada Prevista'])).dt.total_seconds() / 60)
    print(atraso_series)
    print(empname, origin, destination, start, end)
    if plot_df.empty:
        print("Não há dados.")
        return px.scatter(title="Atrasos na decolagem")
    return px.scatter(plot_df, y=atraso_series.where(atraso_series > 0), labels={"index": "Partida Real", "y": "Atraso (minutos)"}, color='Sigla da Empresa', title='Atrasos na aterrissagem')