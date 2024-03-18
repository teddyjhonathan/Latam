import os
import pandas as pd
from collections import Counter
from typing import List, Tuple

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Se ajusta la ruta de lectura del archivo JSON a .parquet para futuras lecturas
    parquet_file = file_path.replace('.json', '.parquet')

    try:
        # Intentar leer el archivo Parquet si existe
        df = pd.read_parquet(parquet_file)
    except FileNotFoundError:
        try:
            # Intentar leer el archivo JSON y convertirlo a DataFrame
            df = pd.read_json(file_path, lines=True)
            # Procesar los datos y guardarlos como archivo Parquet
            df.to_parquet(parquet_file, index=False)
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")
            return []

    # Se extraen todas las menciones por cada tweet
    mentions_flat = []
    for mentions_list in df['content'].str.findall(r'@(\w+)').dropna():
        mentions_flat.extend(mentions_list)

    # Se cuenta la frecuencia de cada mención en la lista aplanada
    mention_counts = Counter(mentions_flat)

    # Obtener los top 10 usuarios más mencionados
    top_mentions = mention_counts.most_common(10)

    return top_mentions
