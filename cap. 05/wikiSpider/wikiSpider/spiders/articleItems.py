from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from wikiSpider.items import Article


class ArticleSpider(CrawlSpider):
    name = 'articleItems'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']

    rules = [
        Rule(LinkExtractor(
            allow='(/wiki/)((?!:).)*$'),
            callback='parse_items',
            follow=True
        ),
    ]

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css(
            'h1>span::text'
        ).get()
        article['text'] = response.xpath(
            '//div[@id="mw-content-text"]//text()'
        ).extract()
        lastUpdated = response.css(
            'li#footer-info-lastmod::text'
        ).extract_first()
        article['lastUpdated'] = lastUpdated.replace(
            'This page was last edited on ', '')
        return article


"""
 Formas de salvar a saída do scrapy

 scrapy runspider articleSpider.py -o articles.xml -t xml
 scrapy runspider articleSpider.py -o articles.json -t json
 scrapy runspider articleSpider.py -o articles.csv -t csv

"""
