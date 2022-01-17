from bs4 import BeautifulSoup
import requests

url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url).text

soup = BeautifulSoup(response, 'html.parser')
titles = [title.getText().split(') ') for title in soup.find_all(name="h3", class_="title")]

with open('top_100_movies.txt', 'a+') as file:
    titles.reverse()
    for movie in titles:
        text = f"{movie[0]}) {movie[-1]} \n"
        file.write(text)