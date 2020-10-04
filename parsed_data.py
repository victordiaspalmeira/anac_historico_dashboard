import pickle as p
import pandas as pd

anac_df = p.load(open('data/data.p', "rb")) #carrega database
anac_df.index = pd.to_datetime(anac_df['Partida Prevista'])
anac_df['Partida Prevista'] = pd.to_datetime(anac_df['Partida Prevista'])
anac_df['Partida Real'] = pd.to_datetime(anac_df['Partida Real'])
anac_df['Chegada Prevista'] = pd.to_datetime(anac_df['Chegada Prevista'])
anac_df['Chegada Real'] = pd.to_datetime(anac_df['Chegada Real'])
