import scrapy


class ArticleSpider(scrapy.Spider):
    name = "article"

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/Python_%28programming_language%29',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python'
        ]
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        title = response.css('h1>span::text').extract_first()
        print(f"URL: {url}")
        print(f"Title: {title}")
