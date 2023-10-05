import requests
from bs4 import BeautifulSoup
import re


# Rastreando sites por meio de links
class Website:
    def __init__(self, name, url, targetPattern, absoluteUrl,
                 titletag, bodyTag):
        self.name = name
        self.url = url
        self.targetPattern = targetPattern
        self.absoluteUrl = absoluteUrl
        self.titleTag = titletag
        self.bodyTag = bodyTag


class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print(f"URL: {self.url}")
        print(f"Title: {self.title}")
        print(f"Body:\n{self.body}\n{'-' * 50}")


class Crawler:
    def __init__(self, site):
        self.site = site
        self.visited = []

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        selectedElms = pageObj.select(selector)
        if selectedElms is not None and len(selectedElms) > 0:
            return "\n".join([elem.text for elem in selectedElms])
        return ''

    def parse(self, url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, self.site.titleTag)
            body = self.safeGet(bs, self.site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()

    def crawl(self):
        """
        Obtém páginas da página inicial do site
        """
        bs = self.getPage(self.site.url)
        targetPages = bs.find_all('a', href=re.compile(
            self.site.targetPattern))
        for targetPage in targetPages:
            targetPage = targetPage.attrs['href']
            if targetPage not in self.visited:
                self.visited.append(targetPage)
                if not self.site.absoluteUrl:
                    targetPage = "{}{}".format(self.site.url, targetPage)
                    self.parse(targetPage)


reuters = Website(
    'Reuters', 'https://www.reuters.com', '^(/world/)', False,
    'h1', 'div.article-body__content__17Yit p')
crawler = Crawler(reuters)
crawler.crawl()
