from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from wikiSpider.items import Article


class ArticleSpider(CrawlSpider):
    name = 'articlePipelines'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']

    rules = [
        Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'), follow=True, callback='parse_items')
    ]


    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css('h1>span::text').get()
        article['text'] = response.xpath('//div[@id="mw-content-text"]//text()').get()
        article['lastUpdated'] = response.css(
            'li#footer-info-lastmod::text'
        ).extract_first()
        return article
