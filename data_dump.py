import pandas as pd
import glob, os
import pickle as p
import datetime

def open_data(path):
    os.chdir(path)
    df_list = list()
    for file in glob.glob("*.csv"):
        df = pd.read_csv(file, encoding = "ISO-8859-1", sep=";|,|\t")
        #df_list.append(df)
        
        df_list.append(df)
       
    return df_list

if __name__ == "__main__":
    df_list = open_data('./data')
    cols = ['Sigla da Empresa', 'Número do Voo', 'Código Autorização (DI)', 'Tipo de linha', 'Aeroporto Origem', 'Aeroporto Destino', 
            'Partida Prevista', 'Partida Real', 'Chegada Prevista', 'Chegada Real', 'Situação do Voo', 'Justificativa']
    anac_df = pd.DataFrame(columns=cols)
    for df in df_list:
        df.reset_index()
        #print(df.columns, cols)
        df.columns = cols

        for col in df.columns:
            try:
                df[col] = df[col].apply(lambda x: x.replace('"', ''))
            except:
                pass
        #print(df.head())
        anac_df = anac_df.append(df, ignore_index = True)

    format = '%d/%m/%Y %H:%M'
    date_cols = ['Partida Prevista', 'Partida Real', 'Chegada Prevista', 'Chegada Real']
    for key in date_cols:
        anac_df[key] = pd.to_datetime(anac_df[key], format=format, errors='coerce')

    #print(anac_df)
    anac_df.to_csv('anac_historico.csv', encoding = "ISO-8859-1")
    p.dump(anac_df, open("data.p", "wb"))