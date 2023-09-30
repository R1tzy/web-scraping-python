import pymysql

"""
Nesse exemplos vamos resolver de uma vez o 
problema dos Six Degrees of Wikipedia que 
aparece no cap. 3 e cap. 6

O Six Degrees original é um problema 
envolvendo grafo não direcionado, portanto 
o relacionamento é bidirecional (não tem “direção”).

Já o Six Degrees of Wikipedia visa percorrer de um link
para o outro, ou seja, de A -> B, mas não necessariamente
de B -> A. É o mesmo que encontrar uma cadeia de Markov e
é um problema de grafo direcionado

A maneira mais comun para encontrar os caminhos 
mais curtos em um grafo direcionado – e que 
usaremos nesse problema – é fazer uma busca
em largura (breadth-first search).
"""

# Estabelece uma conexão com o banco de dados MySQL
conn = pymysql.connect(
    host='127.0.0.1', user='root', passwd='LopeS#2604', 
    db='mysql', charset='utf8',
)

# Cria um cursor para executar consultas SQL
cur = conn.cursor()

# Seleciona o banco de dados "wikipedia"
cur.execute('USE wikipedia')

# Função para obter a URL de um artigo com base no seu ID
def getUrl(pageId):
    cur.execute('SELECT url FROM pages WHERE id = %s', (int(pageId)))
    return cur.fetchone()[0]


# Função para obter os links de saída de um artigo com base no seu ID
def getLinks(fromPageId):
    cur.execute('SELECT toPageId FROM links WHERE fromPageId = %s',
                (int(fromPageId)))
    if cur.rowcount == 0:
        return []
    return [x[0] for x in cur.fetchall()]

# Função de busca em largura (BFS) para encontrar o caminho mais curto
def searchBreadth(targetPageId, paths=[[1]]):
    newPaths = []
    for path in paths:
        links = getLinks(path[-1])
        for link in links:
            if link == targetPageId:
                return path + [link] # Encontramos o caminho, retornamos
            else:
                newPaths.append(path + [link]) # Adiciona novos caminhos
    return searchBreadth(targetPageId, newPaths) # Chama a função recursivamente

# Inicialização obtém os links do artigo de partida (ID 1) que é Kevin Bacon
nodes = getLinks(1) 
targetPageId = 39134
"""
Essa numeração do targetPageId se refere ao exe7.py 
do cap.6 basicamente o código do exe7.py faz uma 
varredura nos links de artigos da wikipedia, iniciando 
pelo artigo de Kevin Bancon e salva no banco de dados, 
ou seja, o ID de '/wiki/Eric_Idle' ficou salvo com 39134
""" 
pageIds = searchBreadth(targetPageId)
for pageId in pageIds:
    print(getUrl(pageId))

"""
Saída 
/wiki/Kevin_Bacon
/wiki/Main_Page
/wiki/Wikipedia
/wiki/Slashdot
/wiki/Mel_Brooks
/wiki/Eric_Idle
"""