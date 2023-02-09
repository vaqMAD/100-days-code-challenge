import requests
import credentials
from date import Today

API_KEY = credentials.NEWS_API
API_ENDPOINT = "https://newsapi.org/v2/everything?"

today = Today()

PARAMS = {
    'q': 'Tesla',
    'searchIn' : 'title',
    'from': today.date,
    'sortBy': 'popularity',
    'language': 'en',
    'pageSize': '10',
    'apiKey': API_KEY,
}


class News():

    def __init__(self):
        self.data = self._get_data_from_api()

        self.all_articles = self.data['articles']
        self.articles_range = self.all_articles[:3]

    def _get_data_from_api(self) -> dict:
        response = requests.get(url=API_ENDPOINT, params=PARAMS)
        response.raise_for_status()
        return response.json()


class OneArticle():

    def __init__(self, article: dict):
        self.title = article['title']
        self.description = article['description']
        self.url = article['url']
