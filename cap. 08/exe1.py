import requests
from bs4 import BeautifulSoup
import re

"""
n-grama é uma sequência de n palavras usadas em 
um texto ou discurso. Ao fazer análise de idiomas 
é conveniente separar um texto procurando n-gramas 
comuns ou conjuntos recorrentes de palavras usadas
com frequência juntas.
"""

"""
A função getNgrams recebe uma string de entrada, 
separa essa string em uma sequência de palavras 
e acrescenta o n-grama (nesse caso, um bigrama) 
iniciado por cada palavra em um array.
"""
def getNGrams(content, n):
    content = content.split(' ')
    output = []
    for i in range(len(content) - n+1):
        output.append(content[i:i+n])
    return output

html = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BeautifulSoup(html.content, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
ngrams = getNGrams(content, 2)
print(ngrams)
print(f'2-grams count is: {str(len(ngrams))}')

"""
Esse código devolve alguns bigramas do texto 
que são  realmente interessantes e úteis:
['of', 'free'], ['free', 'and'], 
['and', 'open-source'], ['open-source','software']

Contudo, a função também devolve muito lixo:
['software\nOutline\nSPDX\n\n\n\n\n\n\n\n\nOperating']
"""