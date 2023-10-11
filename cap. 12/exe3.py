import requests
from bs4 import BeautifulSoup
import json
import re
import random
from requests import HTTPError


def getLinks(articleUrl):
    html = requests.get('https://en.wikipedia.org' + articleUrl)
    bs = BeautifulSoup(html.content, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all(
        'a', href=re.compile('^(/wiki/)((?!:).)*$'))


def getHistoryIPs(pageUrl):
    """
    Este é o formato das páginas 
    de histórico de revisões:
    http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    """
    pageUrl = pageUrl.replace('/wiki/', '')
    history_url = (
            'https://en.wikipedia.org/w/index.php?'
            f'title={pageUrl}&action=history'
    )
    print(f'histórico de url é {history_url}')
    html = requests.get(history_url)
    bs = BeautifulSoup(html.content, 'html.parser')
    """
    Encontra apenas os links cuja 
    classe seja "mw-anonuserlink" e
    tenha endereços IP em vez de nomes 
    de usuário
    """
    ipAddresses = bs.find_all('a', {'class': 'mw-anonuserlink'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList


def getCountry(ipAddress):
    try:
        response = requests.get(f'https://ipinfo.io/{ipAddress}/json')
        responseJson = response.json()
        return responseJson['country']
    except HTTPError:
        return None


links = getLinks("/wiki/Python_(programming_language)")
print(links)

while len(links) > 0:
    for link in links:
        print("-"*20)
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIp in historyIPs:
            country = getCountry(historyIp)
            if country is not None:
                print(f"{historyIp} is from {country}")

    newlinks = links[random.randint(0, len(links-1))].attrs['href']
    links = getLinks(newlinks)

"""
Saída

history url is: http://en.wikipedia.org/w/index.php?title=Programming_
paradigm&action=history
68.183.108.13 is from US
86.155.0.186 is from GB
188.55.200.254 is from SA
"""