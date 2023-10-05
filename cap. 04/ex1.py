import requests
from bs4 import BeautifulSoup


"""
    Exemplo de uma classe Content (que representa o conteúdo de um site,
    por exemplo, um artigo de notícia) e duas funções de coleta de dados
    que aceitam um objeto BeautifulSoup e devolvem uma instância de Content:
"""


class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body


def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.content, 'html.parser')


"""
    usa  list comprehension
    body = '\n'.join(
        [line.text for line in lines]
    )
    trocando em miúdos, isso é o mesmo que o de cima
    line = []
    for f in lines:
        line.append(f.text)
    body = '\n'.join(line)
"""


def scrapeG1(url):  # pega outro site
    bs = getPage(url)
    title = bs.find('div', {'class': 'mc-article-header'}).find('h1').text
    lines = bs.find("article", {'itemprop': 'articleBody'}).find_all('p')
    # [:-1] é para não pegar o último p, que tem a legenda de uma foto
    body = '\n\n'.join([line.text for line in lines[:-1]])
    return Content(url, title, body)


def scrapeBookings(url):
    bs = getPage(url)
    title = bs.find("h1").text
    lines = bs.find(id='content').find_all('div', {'class': 'wysiwyg-block'})
    paragraphs = [line.find_all('p') for line in lines]
    paragraphs_text = []
    for paragraph_list in paragraphs:
        for paragraph in paragraph_list:
            paragraphs_text.append(paragraph.text)
    body = '\n\n'.join(paragraphs_text)
    return Content(url, title, body)


url = 'https://www.brookings.edu/articles/'
'delivering-inclusive-urban-access-3-uncomfortable-truths/'

content = scrapeBookings(url)
print(f'Title: {content.title}')
print(f'URL: {content.url}\n')
print(f'{content.body}\n\n')

url = 'https://g1.globo.com/mundo/noticia/2023/08/24/trump-foto-georgia.ghtml'

content = scrapeG1(url)
print(f'Title: {content.title}')
print(f'URL: {content.url}')
print(f'{content.body}\n')
