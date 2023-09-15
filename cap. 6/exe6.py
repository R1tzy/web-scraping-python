import requests
from bs4 import BeautifulSoup
import pymysql
import re
import random

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', 
                       port=3306, db='mysql', charset='utf8')

cur = conn.cursor()
cur.execute('USE scraping')


def store(title, content):
    cur.execute('INSERT INTO pages (title, content) VALUES '
                '("%s", "%s")', (title, content))
    cur.connection.commit()

def getLinks(articlesURl):
    html = requests.get('https://en.wikipedia.org/' + articlesURl)
    bs = BeautifulSoup(html.content, 'html.parser')
    title = bs.find('span', {'class':'mw-page-title-main'}).get_text()
    div_content = bs.find('div', {'class':'mw-body-content'}).find('div', {'class':'mw-parser-output'})
    contents = div_content.find_all('p')
    content = [content.get_text() for content in contents]
    store(title, content)
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = getLinks('/wiki/Kevin_Bacon')

try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()