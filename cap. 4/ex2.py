import requests
from bs4 import BeautifulSoup


class Content:
    """
    Classe-base comum para todos os artigos/páginas
    """
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Uma função flexível de exibição que controla a saída
        """
        # Substituir múltiplos espaços por um único espaço
        # clean_body = ' '.join(self.body.split())
        print(f'URL: {self.url}')
        print(f'title: {self.title}')
        print(f'Body:\n{self.body}\n{"-"*50}')
        # Imprimir o corpo limpo e adicionar linha de separação


class Website:
    """
    Contém informações sobre a estrutura do site
    """
    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Crawler:

    def getPage(self, url):
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(response.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        """
        Função utilitária usada para obter uma string de conteúdo de um
        objeto BeautifulSoup e um seletor. Devolve uma string
        vazia caso nenhum objeto seja encontrado para o dado seletor
        """
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return "\n".join([elem.get_text() for elem in selectedElems])
        return ''

    def parse(self, site, url):
        """
        Extrai conteúdo de um dado URL de página
        """
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()


crawler = Crawler()

siteData = [
    ["O'reilly Media", "https://www.oreilly.com/",
     'h1', "div.content>span>div"],
    ["Reuters", 'https://www.reuters.com/', 'h1',
     "article.ArticlePage-article-body-1xN5M"],
    ['Brookings', 'https://www.brookings.edu/',
     "h1", "section#content>div>div"],
]

website = []

for row in siteData:
    website.append(Website(row[0], row[1], row[2], row[3]))

crawler.parse(website[0], 'https://www.oreilly.com/library/'
              'view/learning-python-5th/9781449355722/')
crawler.parse(website[1], 'https://www.reuters.com/article/'
              'us-usa-epa-pruitt-idUSKBN19W2D0')
crawler.parse(website[2], 'https://www.brookings.edu/articles/'
              'idea-to-retire-old-methods-of-policy-education/')
