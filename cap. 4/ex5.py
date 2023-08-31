# import requests
# from bs4 import BeautifulSoup

"""
    Esse código são exemplos de como rastrear diferentes tipos de
    páginas em um site de maneira eficiente usando classes e herança
    (programação orientada a objeto)

    Tipos de Identificação de Página ao fazer web crawling:
    1 - Pelo URL: O formato do URL pode indicar o tipo de conteúdo
    da página, como postagens de blog, páginas de produtos, etc.

    2 - Pela presença/ausência de campos: Determinados campos na página,
    como data, autor, preço, imagem principal, etc., podem indicar o tipo
    da página.

    3 - Pela presença de tags específicas: As tags HTML presentes na
    página podem indicar seu tipo, mesmo que essas informações não
    sejam coletadas.

    4 - Através de diferentes estruturas de página: Se o conteúdo das
    páginas varia significativamente em termos de estrutura, criar objetos
    diferentes para cada tipo de página pode ser apropriado.
"""


class Website:
    """Classe-base comum para todos os artigos/páginas"""
    def __init__(self, pageType, name, url, searchUrl, resultListing,
                 resultUrl, absoluteUrl, titleTag, bodyTag):
        self.pageType = pageType
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag


class Webpage:
    """Classe-base comum para todos os artigos/páginas"""
    def __init__(self, name, url, titleTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag


class Product(Website):
    """Contém informações para coletar dados de uma página de produto"""
    def __init__(self, name, url, titleTag, productNumber, price):
        Website.__init__(self, name, url, titleTag)
        self.productNumber = productNumber
        self.price = price


class Article(Website):
    """Contém informações para coletar dados de uma página de artigo"""
    def __init__(self, name, url, titleTag, bodyTag, dateTag):
        Website.__init__(self, name, url, titleTag)
        self.bodyTag = bodyTag
        self.dateTag = dateTag
