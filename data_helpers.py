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
