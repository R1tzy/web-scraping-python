import requests
from bs4 import BeautifulSoup
"""
Como o texto do site é em russo e francês, os navegadores 
tem problemas para ler essa codificação, então 
precisamos definir o formato de codificação quando 
formos obter esse texto
"""
textPage = requests.get('https://www.pythonscraping.com/'
                        'pages/warandpeace/chapter1-ru.txt')
textPage.encoding = "UTF-8"
print(textPage.text)


html = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language')
bs = BeautifulSoup(html.content, 'html.parser')
content = bs.find('div', {'id': 'mw-content-text'}).get_text()
#converte o texto extraído em uma sequência de bytes em UTF-8
content = bytes(content, 'UTF-8')
#decodifica sequência de bytes para uma string usando UTF-8
content = content.decode('UTF-8')
print(content)

"""
Procurar pela tag meta charset e usar a codificação 
recomendada por ela ao ler o conteúdo da página é 
uma atitude inteligente ao fazer web scraping.
"""