
import requests
from bs4 import BeautifulSoup
import re

#obtenha uma página arbitrária da Wikipédia e gere uma lista de links 
url = requests.get('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(url.content, 'html.parser')

for link in bs.find_all('a'): #percorre todos as tag <a> da páginas
    if 'href' in link.attrs: # verifica se a tag <a> tem o atributo href
        print(link.attrs['href']) #imprime o href das tag
    # também podemos fazer link.get('href') que pega os href da tag e não precisa do if  
    # no primeiro caso precisa do if porque nem toda tag <a> tem o atributo href, então sem isso temos o erro KeyError: 'href'

#Pegar apenas os links internos do wikipedia, ou seja, links de artigos da wikipedia
# todos os links de artigos tem essas características:
    # Estão na div com o id definido com bodyContent.
    # Os URLs não contêm dois-pontos.
    # Os URLs começam com /wiki/.

# encontre a div com o id:bodyContent, encontre todas as tag <a> com href nesse padrão /wiki/nome_pagina
# foi usando o re.compile para definir o padrão porque ele vai ser usado várias vezes
# ^ indica o início
# (/wiki/) grupo de captura que corresponde a sequência /wiki/
# ((?!:).)* outro grupo de captura, que contém um grupo de caputra (?!:) que indica que não deve haver ":"
# ?! indica a negação, não deve haver
# '.' indica qualquer caracter (exceto uma nova linha)
# * faz com que a combinaçã ((?!:).) repita 0 ou mais vezes
# $ indica o final
for link in bs.find('div', {'id':'bodyContent'}).find_all(
    'a', href=re.compile('^(/wiki/)((?!:).)*$')):
    print(link.get('href'))
# ou if 'href' in link.attrs:
    # print(link.attrs['href'])
