
from datetime import datetime
from typing import List, Tuple
from collections import defaultdict
import ujson as json

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Diccionario para mantener el conteo de tweets por fecha
    date_counts = defaultdict(int)
    # Diccionario para mantener el usuario con más tweets por fecha
    top_users_by_date = {}
    
    with open(file_path, "r") as file:
        for line in file:
            tweet = json.loads(line)
            # Se extrae la fecha del tweet y se convierte a datetime.date
            tweet_date = datetime.strptime(tweet['date'].split("T")[0], '%Y-%m-%d').date()
            
            # Se actualiza el conteo de tweets para esa fecha
            date_counts[tweet_date] += 1
            
            # Se actualiza el usuario con más tweets para esa fecha
            if tweet_date not in top_users_by_date:
                top_users_by_date[tweet_date] = defaultdict(int)
            top_users_by_date[tweet_date][tweet['user']['username']] += 1
    
    # Se obtienen las top 10 fechas con más tweets
    top_dates = sorted(date_counts, key=date_counts.get, reverse=True)[:10]
    
    # Se obtiene el usuario con más tweets para cada fecha
    result = [(date, max(top_users_by_date[date], key=top_users_by_date[date].get)) for date in top_dates]
    
    return result