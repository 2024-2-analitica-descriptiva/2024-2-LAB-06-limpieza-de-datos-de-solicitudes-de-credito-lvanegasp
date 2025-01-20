"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """

    # 1. Leer datos
    df = pd.read_csv(
        "files/input/solicitudes_de_credito.csv",
        delimiter=";",
        encoding="utf-8",
        index_col=0,
    )

    # ------------------------------------------------------------
    # ------------------------------------------------------------
    # Quitar duplicados y filas con datos faltantes
    # df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    # df = df.dropna()

    # ------------------------------------------------------------
    # ------------------------------------------------------------
    # Estandarizar columnas

    # ------------------------------
    # Estandarizar columna sexo
    df["sexo"] = df["sexo"].str.lower()
    df["sexo"] = df["sexo"].str.strip()

    # ------------------------------
    # Estandarizar columna tipo_de_emprendimiento
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    # df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.replace(
    #    r"[_-]", " ", regex=True
    # )

    # df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.replace(
    #    r'["]', "", regex=True
    # )
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.strip()

    # ------------------------------
    # Estandarizar columna idea_negocio
    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.replace(r"[_-]", " ", regex=True)
    df["idea_negocio"] = df["idea_negocio"].str.replace(r'["]', "", regex=True)
    df["idea_negocio"] = df["idea_negocio"].str.strip()

    # ------------------------------
    # Estandarizar columna barrio
    df["barrio"] = df["barrio"].astype(str)
    df["barrio"] = df["barrio"].str.lower()
    df["barrio"] = df["barrio"].str.replace(r"[_-]", " ", regex=True)
    # df["barrio"] = df["barrio"].str.replace(r'["]', "", regex=True)
    df["barrio"] = df["barrio"].str.replace(r"no\.\s*(\d+)", r"no\1", regex=True)
    # df["barrio"] = df["barrio"].str.strip()

    # ------------------------------
    # Estandarizar columna barrio
    df["estrato"] = df["estrato"].astype(int)

    # ------------------------------
    # Estandarizar columna comuna_ciudadano
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    # ------------------------------
    # Estandarizar columna fecha_de_beneficio

    df["fecha_de_beneficio"] = pd.to_datetime(
        df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"
    ).fillna(
        pd.to_datetime(df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce")
    )

    # ------------------------------
    # Estandarizar columna monto_del_credito

    df["monto_del_credito"] = (
        df["monto_del_credito"].astype(str).str.replace("[^0-9.]", "", regex=True)
    )
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)
    # df["monto_del_credito"] = pd.to_numeric(df["monto_del_credito"], errors="coerce")

    # ------------------------------
    # Estandarizar columna línea_credito

    df["línea_credito"] = df["línea_credito"].str.lower()

    # df["línea_credito"] = df["línea_credito"].str.replace("soli-daria", "solidaria")
    # df["línea_credito"] = df["línea_credito"].str.replace("soli-diaria", "solidaria")
    df["línea_credito"] = df["línea_credito"].str.replace(r"[_-]", " ", regex=True)
    df["línea_credito"] = df["línea_credito"].str.strip()

    output_path = "files/output/solicitudes_de_credito.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # ------------------------------------------------------------
    # ------------------------------------------------------------
    # Quitar duplicados y filas con datos faltantes
    df.drop_duplicates(inplace=True)
    # df.dropna(inplace=True)

    # ------------------------------------------------------------
    # ------------------------------------------------------------
    # Guardar datos limpios
    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)

    # ------------------------------------------------------------
    # ------------------------------------------------------------
    # Verificaciones

    # print(df.info())
    # print(df.sexo.value_counts().to_list())
    # print(df.sexo)
    # print(df.sexo.unique())


if __name__ == "__main__":
    pregunta_01()
