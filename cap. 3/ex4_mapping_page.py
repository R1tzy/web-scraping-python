import requests
from bs4 import BeautifulSoup
import re

#AVISO
#esse código é de exemplo básico, não funciona para algo complexo ou mais elaborado. É apenas um exemplo de mapeamento de uma página e além disso imprimindo alguns dados. Visto que no pensamento do autor não faz sentido fazer um mapeamento listando o site se não for para captura algum dado, ou fazer algo.

#Redirecionamento
# Os redirecionamentos permitem que um servidor web aponte um nome de domínio ou um URL para um conteúdo em um local diferente. 
# Redirecionamentos servidor, em que o URL é alterado antes de a página ser carregada.
# Redirecionamentos cliente, às vezes visto com uma mensagem do tipo “Você será redirecionado em 10 segundos”, em que a página é carregada antes do redirecionamento para a nova página.
# A biblioteca urllib com Python 3.x, trata os redirecionamentos automaticamente
# A biblioteca requests, precisa definir a flag allow_redirects como True para permitir redirecionamentos
# r = requests.get('http://github.com', allow_redirects=True)

pages = set()
def getUrl(url):
    global pages
    html = requests.get('http://en.wikipedia.org{}'.format(url))
    bs = BeautifulSoup(html.content, 'html.parser')
    try:
        print(bs.find('h1').get_text()) #pegar o texto do primeiro h1
        print(bs.find(id='mw-content-text').find_all('p')[0]) #primeira tag <p> que aparecer no mw-content-text
        print(bs.find(id='ca-edit').find('a').attrs['href'])#pegar o link de editar da página
    except AttributeError: #se não tiver algum dos itens de cima, vai dar erro
        print('Esta página está faltando alguma coisa! Continuando')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs: #verifica se o link tem o atributo href
            if link.attrs['href'] not in pages: #se o href do link não estiver dentro do pages
                #Encontramos uma nova página
                new_page = link.attrs['href']
                print('-'*20) # apenas para apresentação separada
                print(new_page) #imprime a nova página
                pages.add(new_page) #adiciona ao set pages
                getUrl(new_page) #chama a função recursivamente

getUrl('')