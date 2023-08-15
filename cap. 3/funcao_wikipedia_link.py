import requests
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now()) # usa o horário da máquina para deixar a aleatoriedade mais difícil
#função getLinks que recebe um link e retornar todos os href da tag <a> presente nessa url
def getLinks(articleUrl):
    try:     
        url = requests.get('https://pt.wikipedia.org/{}'.format(articleUrl))
    except requests.exceptions.RequestException as e: #tratamento de exceção caso ele não ache a url
          return e
    try:
        bs = BeautifulSoup(url.content, 'html.parser')
        return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    except AttributeError as e: # tratamento de exceção caso ele não encontre o elemento
        return e


link = getLinks('/wiki/Kevin_Bacon') #usado na inicialização da primeira url e armazena os links dessa url

while len(link) > 0: #verifica a quantidade de liks > 0
    newArticle = link[random.randint(0, len(link)-1)].attrs['href'] #variável que armazena um link escolhido aleatoriamente dentre os que foram armazenados na variável link
    print(newArticle) #imprime esse link
    getLinks(newArticle) #chama a função novamente

#acessa uma url e pega todos os links no formato definido da tag <a>
#escolhe uma url aleatória desse links e chama a função novamente
#fica executando isso até não ter mais links ou atér finalizar o script
