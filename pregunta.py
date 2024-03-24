"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd

from datetime import datetime as dt


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.drop("Unnamed: 0", axis=1, inplace=True)

    df.duplicated().sum()

    df.drop_duplicates(inplace=True)

    df.dropna(axis=0, inplace=True)

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].str.lower()

    df.idea_negocio = df.idea_negocio.str.replace("[_-]", " ", regex=True)

    df.barrio = df.barrio.str.replace("[-]", " ", regex=True)
    df.barrio = df.barrio.str.replace("[ ]+", "_", regex=True)

    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)

    def format_date(str_date):
        try:
            return dt.strptime(str_date, "%d/%m/%Y")
        except ValueError:
            return dt.strptime(str_date, "%Y/%m/%d")

    df.fecha_de_beneficio = df.fecha_de_beneficio.apply(format_date)

    df.monto_del_credito = df.monto_del_credito.str.replace("[$, ]", "", regex=True)
    df.monto_del_credito = df.monto_del_credito.str.replace(".00", "", regex=False)
    df.monto_del_credito = df.monto_del_credito.astype(float)

    df.línea_credito = df.línea_credito.str.replace("[-_]", " ", regex=True)

    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    df.drop_duplicates(inplace=True)

    return df
