import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.pythonscraping.com/pages/warandpeace.html')
bs =  BeautifulSoup(url.content, 'html.parser')
print(bs.find_all(lambda tag: len(tag.attrs) == 2))
# usando lambda para retornar tags que tenha dois atributos

# podemos usar lambda para encontrar o determinado texto na página
# print(bs.find_all(lambda tag: tag.text =='War and Peace'))
# Ou simplesmente fazer isso
# print(bs.find_all('', string='War and Peace'))

#usando lambda ele retornar [<h1>War and Peace</h1>] e com o beautifulsoup retorna só ['War and Peace']