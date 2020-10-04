import plotly.express as px
import pandas as pd

def duracao_voo_plot(df, start_time, end_time, emp):
    start = datetime.datetime.strptime(inicio, '%d/%m/%Y').date()
    end = datetime.datetime.strptime(fim, '%d/%m/%Y').date()
    plot_df = anac_df[anac_df['Sigla da Empresa'] == empname]
    plot_df = plot_df.loc[str(start):str(end)]

    duracao_series = (plot_df['Chegada Real'] - plot_df['Partida Real']).div(pd.Timedelta('1H'))
    return px.scatter(plot_df, x=plot_df.index, y=duracao_series, labels={"index": "Partida Prevista", "y": "Duração em horas"})

def situaçao_voo_plot(df, start_time, end_time, emp):
    start = datetime.datetime.strptime(inicio, '%d/%m/%Y').date()
    end = datetime.datetime.strptime(fim, '%d/%m/%Y').date()
    plot_df = anac_df[anac_df['Sigla da Empresa'] == empname]
    plot_df = plot_df.loc[str(start):str(end)]

    return px.bar(plot_df, x=plot_df.index, y=plot_df['Situação do Voo'])
