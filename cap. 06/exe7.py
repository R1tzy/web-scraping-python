import requests
from bs4 import BeautifulSoup
import re
import pymysql

# Conexão com o banco de dados
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='LopeS#2604', 
                       port=3306, db='mysql', charset='utf8')
# Criando o cursos
cur = conn.cursor()
# Acessando o database wikipedia
cur.execute("USE wikipedia")

# Inserir página se não existir
def insertPageIfNotExist(url):
    # selecionando tudo da tabela pages onde url(database) = url (parâmetro)
    cur.execute('SELECT * FROM pages WHERE url = %s', (url))
    """
    Rowcount propriedade usada para obter o número de 
    linhas afetadas pela última operação executada do 
    banco de dados, ou seja, se rowcount for igual a 0
    significa que não existe na tabela
    """
    if cur.rowcount == 0:
        # Insere na tabela pages a url
        cur.execute('INSERT INTO pages (url) VALUES (%s)', (url))
        # commit é usado para confirmar a operação
        conn.commit()
        # lastrowid recupera o id da última linha inserida nada tabela
        return cur.lastrowid
    else:
        """
        Fetchone recupera a próxima linha de um conjunto de resultados,
        nesse caso na posição 0
        """
        return cur.fetchone()[0]

# Carregar páginas
def loadPages():
    # seleciona tudo da tabela pages
    cur.execute("SELECT * FROM pages")
    """
    Usa list comprehension para armazenar na variável 
    pages(vetor) o resultado da posição 1 dentre todos os 
    resultados existentes na tabela
    """
    pages = [row[1] for row in cur.fetchall()]
    return pages

# Inserir link passando o ID de onde(atual), ID para onde(próxima)
def insertLink(fromPageId, toPageId):
    """
    Selecionando tudo da tabela links onde 
    fromPageId(database) = fromPageId(parâmetro) e 
    toPagaId(database) = toPageId(parâmetro)
    """
    cur.execute('SELECT * FROM links WHERE fromPageId = %s '
                'AND toPageId = %s', (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)',
                    (int(fromPageId), int(toPageId)))

        conn.commit()

# Pegando os links
def getLinks(pageUrl, recursionLevel, pages):
    # Verificar o nível de recursão antes de continuar
    if recursionLevel > 4:
        return
    
    # Verificar se a página já foi visitada antes
    if pageUrl in pages:
        return
    
    # Inserir a página no banco de dados
    pageId = insertPageIfNotExist(pageUrl)
    html =  requests.get(f'http://en.wikipedia.org{pageUrl}')
    bs = BeautifulSoup(html.content, 'html.parser')
    links = bs.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    links = [link.attrs['href'] for link in links]
    for link in links:
        insertLink(pageId, insertPageIfNotExist(link))
        # Adicionar a página à lista de páginas visitadas
        if link not in pages:
            # Encontramos uma nova página, acrescente-a e procure outros links
            pages.append(link)
            getLinks(link, recursionLevel+1, pages)

getLinks('/wiki/Kevin_Bacon', 0, loadPages())
cur.close()
conn.close()
