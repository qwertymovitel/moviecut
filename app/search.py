import requests
from config import Config

def advanced_search(phrase, genre=None, year=None):
    api_key = Config.TMDB_API_KEY
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={phrase}"
    if year:
        url += f"&year={year}"
    if genre:
        url += f"&with_genres={genre}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('results', [])
    return []