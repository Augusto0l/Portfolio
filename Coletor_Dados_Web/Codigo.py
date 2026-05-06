import requests
from bs4 import BeautifulSoup

url = "https://g1.globo.com/"
resposta = requests.get(url)

soup = BeautifulSoup(resposta.text, "html.parser")

noticias = soup.find_all("a", class_="feed-post-link")

for i, noticia in enumerate(noticias, start=1):
    print(f"{i}. {noticia.text.strip()}")
