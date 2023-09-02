from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

"""
    Percorre todos os links no domínio wikipedia.org e pega o título, url,
    e o conteúdo.

    Um Rule pode receber seis argumentos, os principais são:

    link_extractor
    É o único argumento obrigatório: um objeto LinkExtractor.

    allow - permite todos os links que correspondam à expressão
    regular fornecida.

    deny - recusa todos os links que correspondam à expressão
    regular fornecida.

    callback
    É a função que deve ser usada para parse do conteúdo da página.

    cb_kwargs
    dicionário com os argumentos a serem passados para a função de
    callback. Esse dicionário é formatado como {arg_name1: arg_value1,
    arg_name2: arg_value2}, e pode ser uma ferramenta conveniente para
    reutilizar as mesmas funções de parsing em tarefas um pouco diferentes.

    follow
    Informa se você quer que os links encontrados nessa página sejam
    incluídos em um rastreamento futuro. O default é True, mas se uma função
    de callback for especificada, o default será False.

"""


class ArticlesSpider(CrawlSpider):
    name = "articles"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Benevolent_dictator_for_life"]
    rules = (
      Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)
    )

    def parse_items(self, response):
        url = response.url
        title = response.css('h1>span::text').get()
        text = response.xpath(
            '//div[@id="mw-content-text"]//text()'
        ).extract()
        lastUpdate = response.css(
            'li#footer-info-lastmod::text'
        ).extract_first()
        lastUpdate = lastUpdate.replace('This page was last edited on ', '')
        print(f"URL: {url}")
        print(f"Title: {title}")
        print(f"Text is:\n{text}")
        print(f"Last update: {lastUpdate}")
