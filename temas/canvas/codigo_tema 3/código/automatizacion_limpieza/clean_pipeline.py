# clean_pipeline.py

import pandas as pd
import janitor
import numpy as np
import pandas_flavor as pf

@pf.register_dataframe_method
def limpiar_boletos_estructura(df):
    """
    PIPELINE STEP 1: Realiza la limpieza estructural genérica.
    Normaliza nombres, nulos no estándar, duplicados y fechas.
    """
    print("-> Ejecutando: limpiar_boletos_estructura")
    
    valores_nulos_no_estandar = ['Sin Dato', 'N/A', 'No Aplica']
    
    df_limpio = (
        df
        .clean_names()
        .replace(valores_nulos_no_estandar, np.nan)
        .drop_duplicates(subset='id_ticket', keep='first')
        #.convert_to_datetime('purchase_date', errors='coerce')
    )
    return df_limpio

@pf.register_dataframe_method
def aplicar_boletos_logica_negocio(df):
    """
    PIPELINE STEP 2: Aplica reglas de negocio específicas para boletos.
    Limpia precios y crea banderas de validación.
    """
    print("-> Ejecutando: aplicar_boletos_logica_negocio")
    
    # Limpiar y convertir la columna de precios
    df['price'] = df['price'].str.replace('MXN ', '', regex=False)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    # Crear una bandera para boletos que requieren revisión
    condicion_revision = (df['destination_state'] == 'Querétaro') & (df['price'] < 400.0)
    df['requiere_revision'] = np.where(condicion_revision, True, False)
    
    # Llenar valores nulos en columnas importantes
    df['seat_number'] = df['seat_number'].fillna(0).astype(int)
    
    return df
