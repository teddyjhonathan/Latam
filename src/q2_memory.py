import ujson as json
from collections import Counter
from typing import List, Tuple
import emoji

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Se crea un contador para contar la frecuencia de cada emoji
    emoji_counts = Counter()
    
    # Se abre el archivo JSON y se itera sobre cada línea
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Se convierte la línea en un diccionario
            tweet = json.loads(line)
            # Se extrae el contenido del tweet y se obtienen los emojis
            content = tweet.get('content', '')
            emojis_in_content = [entry['emoji'] for entry in emoji.emoji_list(content)]
            
            # Se actualiza el contador con los emojis encontrados en este tweet
            emoji_counts.update(emojis_in_content)

    # Se obtienen los top 10 emojis más utilizados
    top_emojis = emoji_counts.most_common(10)
    
    return top_emojis