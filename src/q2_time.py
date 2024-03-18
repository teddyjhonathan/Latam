import os
import pandas as pd
import emoji
from collections import Counter
from typing import List, Tuple

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # Se ajusta la ruta de lectura de archivo json a .parquet para futuras lecturas
    parquet_file = file_path.replace('.json', '.parquet')
    
    try:
        # Se intenta leer el archivo parquet
        df = pd.read_parquet(parquet_file)
    except FileNotFoundError:
        # Si el archivo parquet no existe, se lee el archivo json y se convierte a parquet
        df = pd.read_json(file_path, lines=True)
        df.to_parquet(parquet_file, index=False)
    
    # Se extraen todos los emojis de la columna 'content' y se cuenta su frecuencia
    all_emojis = []
    for content in df['content']:
        emojis_in_content = [entry['emoji'] for entry in emoji.emoji_list(content)]
        all_emojis.extend(emojis_in_content)
    # Se cuenta la frecuencia de cada emoji
    emoji_counts = Counter(all_emojis)

    # Se obtienen los top 10 emojis más utilizados
    top_emojis = emoji_counts.most_common(10)
    
    return top_emojis
