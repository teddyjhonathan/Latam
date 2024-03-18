import ujson as json
from collections import Counter
from typing import List, Tuple
import re

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Se crea un Counter para contar la frecuencia de cada mención
    mention_counts = Counter()
    
    # Se abre el archivo json y se itera sobre cada tweet
    with open(file_path, 'r') as file:
        # Iterar línea por línea en el archivo
        for line in file:
            tweet = json.loads(line)
            content = tweet.get('content', '')
            # Se busca todas las menciones en el contenido y se actualiza el Counter
            mention_counts.update(re.findall(r'@(\w+)', content))
            
    # Obtener los top 10 usuarios más mencionados
    top_mentions = mention_counts.most_common(10)
    
    return top_mentions