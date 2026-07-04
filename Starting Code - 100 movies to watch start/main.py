import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_list = response.text

soup = BeautifulSoup(movies_list,'html.parser')
movies = soup.find_all(class_='landscape')[::-1]
with open('movies.txt','w') as file:
    for movie in movies:
        file.write(f"{movie.get('title')}\n")