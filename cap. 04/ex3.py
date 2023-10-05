import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote


class Content:
    """Classe-base comum para todos os artigos/páginas"""
    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """Uma função flexível de exibição controla a saída"""
        print(f'Novo artigo encontrado para o tópico: {self.topic}')
        print("Title: " + "\n".join(self.title))
        print("Body:\n"+"\n".join(self.body))
        print(f'URL: {self.url}\n{"-"*50}')


class Website:
    """Contém informações sobre a estrutura do site"""
    def __init__(self, name, url, searchUrl, resultListing,
                 resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:

    def getPage(self, url):
        try:
            if url.startswith("//"):  # verifica se a url tá codificada
                decode_url = unquote(url)

                start_index = decode_url.find("u=") + 2
                end_index = decode_url.find("&syn=")
                page_url = decode_url[start_index:end_index]
                req = requests.get(page_url)
            else:
                req = requests.get(url)
            req.encoding = 'utf-8'  # Deixa no formato utf-8
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            # tira os espaços em branco
            childtext = [child.text.strip() for child in childObj]
            return childtext
        return ''

    def search(self, topic, site):
        """
        Pesquisa um dado site em busca de um dado tópico e registra
        todas as páginas encontradas
        """
        bs = self.getPage(site.searchUrl + topic)
        searchResult = bs.select(site.resultListing)
        for result in searchResult:
            url = result.select(site.resultUrl)[0].get('href')
            if url.startswith("//"):  # verifica se a url tá codificada
                decode_url = unquote(url)
                start_index = decode_url.find("u=") + 2
                end_index = decode_url.find("&syn=")
                url = decode_url[start_index:end_index]
            # Verifica se uma url é relativa ou absoluta
            if (site.absoluteUrl):
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print("Algo estava errado com a página ou url. Pulando!")
                return
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(topic, url, title, body)
                content.print()


crawler = Crawler()

siteData = [
    [
        'G1', 'https://g1.globo.com/', 'https://g1.globo.com/busca/?q=',
        'li.widget--info', "div.widget--info__text-container > a",
        True, 'h1.content-head__title', 'article[itemprop="articleBody"] p'
    ],
    [
        "Folha de São Paulo", 'https://www.folha.uol.com.br/',
        "https://search.folha.uol.com.br/?q=", "ol.c-search>li",
        'div.c-headline__content a', True, 'h1.c-content-head__title',
        'div.c-news__body p'
    ]
]

sites = []
for row in siteData:
    sites.append(Website(
        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
    ))

topics = ['python', 'ciência de dados']
for topic in topics:
    print(f"Obter informação sobre: {topic}")
    for targetSite in sites:
        crawler.search(topic, targetSite)
