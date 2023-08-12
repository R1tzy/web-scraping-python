import requests
from bs4 import BeautifulSoup

def get_url(url):
    #tratamento de erro para verificar se tem algum erro no momento de obter a url
    try:
        html = requests.get(url)
    except requests.exceptions.RequestException as e:
        return None
    #tratamento de erro para verificar se tem a tag fornecida
    try:
        bs = BeautifulSoup(html.content, 'html.parser') #transforma o conteúdo do request para formato do bs4
        title = bs.h1 #pega o título
    except AttributeError as e:
        return None
    return title

#caso entre em algum except retorna none 
title = get_url('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print("Título não encontrado")
else:
    print(title)