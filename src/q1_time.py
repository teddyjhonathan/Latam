import pandas as pd
from typing import List, Tuple
from datetime import date

def q1_time(file_path: str) -> List[Tuple[date, str]]:
    # Leer el archivo JSON directamente si el archivo Parquet no existe
    try:
        df = pd.read_parquet(file_path.replace('.json', '.parquet'))
    except FileNotFoundError:
        df = pd.read_json(file_path, lines=True)
        df['date'] = pd.to_datetime(df['date']).dt.date
        df['username'] = df['user'].apply(lambda x: x.get('username'))
        df.drop(columns=['user'], inplace=True)
        df.to_parquet(file_path.replace('.json', '.parquet'), index=False)

    # Contar el número de tweets por fecha y usuario
    date_user_counts = df.groupby(['date', 'username']).size().reset_index(name='count')

    # Encontrar las 10 fechas con más tweets
    top_dates = df['date'].value_counts().nlargest(10).index

    # Obtener el usuario con más tweets para cada una de las 10 fechas
    result = []
    for date_val in top_dates:
        top_user_df = date_user_counts[date_user_counts['date'] == date_val].nlargest(1, 'count')
        top_user = top_user_df['username'].iloc[0]
        result.append((date_val, top_user))

    return result