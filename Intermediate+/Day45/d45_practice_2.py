import math

import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

articles = soup.find_all(name='a', class_="titlelink")
article_texts = []
article_links = []
article_upvotes = [int(score.getText().split()[0]) for score in   soup.find_all(name='span', class_="score")]

for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get('href'))


index = article_upvotes.index(max(article_upvotes))

print(article_texts[index])
print(article_links[index])