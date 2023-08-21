import requests
from bs4 import BeautifulSoup
import re
import datetime
import random
from urllib.parse import urlparse


#mapeando links internos e externos

page = set()

#Obtém uma lista de todos os links internos encontrados em uma página
def getInternalLink(bs, includeUrl):
    internalsLink = []
    #Encontra todos os links que começam com "/"
    for link in bs.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')):
        #busca href que começa com / ou corresponde a zero ou mais caracteres de qualquer tipo e concatenado ao includeUrl
        if link.get('href') is not None: #se o href do link não for vazio
            if link.get('href') is not internalsLink: #se o href não estiver no internalsLink
                if (link.attrs['href'].startswith('/')): 
                    #se o href começa com /, armazena no internalsLink a url e o href
                    internalsLink.append(includeUrl + link.attrs['href'])
                else: #se não armazena apenas o href no internalsLink
                    internalsLink.append(link.get('href'))
    return internalsLink

#Obtém a lista de todos os links externos da página
def getExternalLinks(bs, excludeUrl):
    externalLink = []
    ##Encontra todos os links que começam com "http" e que não contenham o URL atual
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        #href inicia com http ou www e exclui a variável excludeUrl
        if link.attrs['href'] is not None:
            if link.attrs['href'] is not externalLink:
                externalLink.append(link.attrs['href'])
    return externalLink

#Obtém um link externo aleatório da página 
def getRandomExternalLink(startingPage):
    html = requests.get(startingPage)
    bs = BeautifulSoup(html.content, 'html.parser')
    externalLink = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLink) == 0:
        print('Não há links externos, procure no site por um')
        domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
        internalLink = getInternalLink(bs, domain)
        return getRandomExternalLink(internalLink[random.randint(0, len(internalLink)-1)])
    else:
        return externalLink[random.randint(0, len(externalLink)-1)]

def followExternalOnly(stratingSite):
    externalLink = getRandomExternalLink(stratingSite)
    print('O link externo aleatório é {}'.format(externalLink))
    followExternalOnly(externalLink)

followExternalOnly('http://oreilly.com')

# Se o objetivo é rastrear um site todo em busca de links externos e tomar nota de cada um deles, a seguinte função pode ser acrescentada:

# allExtLinks = set() #links externos
# allIntLinks = set() #links internos

# def getAllExternalLinks(siteUrl):
#     html = requests.get(siteUrl)
#     bs = BeautifulSoup(html.content, 'html.parser')
#     domain = '{}://{}'.format(urlparse(siteUrl).scheme, urlparse(siteUrl).netloc)
#     internalLinks = getInternalLink(bs, domain)
#     externalLinks = getExternalLinks(bs, domain)

#     for link in externalLinks:
#         if link not in allExtLinks:
#             allExtLinks.add(link)
#             print(link)

#     for link in internalLinks:
#         if link not in allIntLinks:
#             allIntLinks.add(link)
#             getAllExternalLinks(link)

# allIntLinks.add('http://oreilly.com')
# getAllExternalLinks('http://oreilly.com')




