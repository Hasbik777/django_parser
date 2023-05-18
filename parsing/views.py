import requests
from bs4 import BeautifulSoup
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AnimeSerializer
from .models import Anime


class AnimeView(APIView):
    def post(self, request):
        url = 'https://anilibria.tv/release/tengoku-daimakyou.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', {'class': 'release-title'}).text.strip()
        description = soup.find('p', {'class': 'detail-description'}).text
        image_url = soup.find('img', {'class': 'detail_torrent_pic'}).get('src')

        anime = Anime(title=title, description=description, image_url=image_url)
        anime.save()

        serializer = AnimeSerializer(anime)
        return Response(serializer.data)
