import requests
from config import Config

def search_movie_phrases(phrase):
    api_key = Config.TMDB_API_KEY
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={phrase}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('results', [])
        return [{
            "movie": movie['title'],
            "phrase": phrase,
            "timestamp": "00:01:30"  # Mock timestamp
        } for movie in results[:5]]  # Limit to 5 results
    return []