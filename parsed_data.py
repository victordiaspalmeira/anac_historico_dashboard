import pickle as p
import pandas as pd

anac_df = p.load(open('data/data.p', "rb")) #carrega database
anac_df.index = pd.to_datetime(anac_df['Partida Prevista'])
anac_df['Partida Prevista'] = pd.to_datetime(anac_df['Partida Prevista'])
anac_df['Partida Real'] = pd.to_datetime(anac_df['Partida Real'])
anac_df['Chegada Prevista'] = pd.to_datetime(anac_df['Chegada Prevista'])
anac_df['Chegada Real'] = pd.to_datetime(anac_df['Chegada Real'])

grp_empresas = anac_df['Sigla da Empresa'].unique()
aero_origem = anac_df['Aeroporto Origem'].unique()
aero_destino = anac_df['Aeroporto Destino'].unique()
grp_empresas.sort()
aero_origem.sort()
aero_destino.sort()
