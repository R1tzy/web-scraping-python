import requests
from bs4 import BeautifulSoup
import re

# set é uma coleção não ordenada, imutável e não indexada. Nenhum membro duplicado.
pages = set() # define um conjunto vazio

def getLinks(url):
    global pages #variável global que referengica a pages fora da função
    html = requests.get('http://en.wikipedia.org{}'.format(url))
    bs = BeautifulSoup(html.content, 'html.parser')
    #procura por toda tag <a> com href que começa com /wiki/
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')): 
        if 'href' in link.attrs: #verifica se a tag tem href
            if link.attrs['href'] not in pages: #se o link href não estiver no conjunto pages
                #Encontramos uma nova página
                new_page = link.attrs['href'] #adiciona o link na variável new_page
                print(new_page) #imprime a nova página
                pages.add(new_page) #adiciona ao conjunto pages
                getLinks(new_page) #chama de forma recursiva a função novamente

getLinks('') #inicio da chamada da função, está vazio pois vai começa a busca em http://en.wikipedia.org

# AVISO IMPORTANTES
# Esse programa vai chegar a uma falha se rodar por muito tempo, pois o Python tem um limite default para recursão (o número de vezes que um programa pode chamar a si mesmo recursivamente) igual a 1.000. 
# Como a rede de links da Wikipédia é extremamente grande, o programa chegará no limite e será interrompido.
# A menos que você coloque um contador de recursão ou algo para impedir que isso aconteça.
# Para sites com menos de 1.000 links de profundidade, esse método funciona bem

# Exceções
# URL gerado dinamicamente, que depende do endereço da página atual para escrever o link, resulta em paths se repetindo infinitamente 
# Exemplo, /blogs/blogs.../blogs/blog-post.php.