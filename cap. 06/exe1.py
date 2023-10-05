import requests
from bs4 import BeautifulSoup

# Faz o download do logo do site pythonscraping.com no diretório img
html = requests.get('http://www.pythonscraping.com')
bs = BeautifulSoup(html.content, 'html.parser')
imageLocation =  bs.find('img', {'alt':'python-logo'}).attrs['src']
img = requests.get(imageLocation)
with open('cap. 6/img/python-logo.png', 'wb') as f:
    f.write(img.content)