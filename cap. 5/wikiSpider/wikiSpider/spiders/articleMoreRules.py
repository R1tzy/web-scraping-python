from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


"""
    Identificando todas as páginas de artigos e sinalizando
    as páginas que não o são
"""


class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = [
        'https://en.wikipedia.org/wiki/Benevolent_dictator_for_life',
    ]

    rules = (
        Rule(
            LinkExtractor(allow='(/wiki/)((?!:).)*$'), callback='parse_item',
            follow=True, cb_kwargs={'is_article': True}
        ),
        Rule(
            LinkExtractor(allow='.*'), callback='parse_item',
            cb_kwargs={'is_article': False}
        )
    )

    def parse_item(self, response, is_article):
        print(response.url)
        title = response.css('h1>span::text').get()
        if is_article:
            # Extrair os parágrafos do artigo
            url = response.url
            text = response.xpath(
                '//div[@id="mw-content-text"]//text()'
            ).extract()
            lastUpdated = response.css(
                'li#footer-info-lastmod::text'
            ).extract_first()
            lastUpdated = lastUpdated.replace(
                'This page was last edited on ', ''
            )
            print('URL: {} '.format(url))
            print('Title: {} '.format(title))
            print('Text: {}'.format(text))
        else:
            print('Não é um artigo: ', title)
