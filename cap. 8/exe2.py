import requests
from bs4 import BeautifulSoup
import re

"""
Essa nova função n-grama usa expressões 
regulares para remover caracteres de escape 
(\n) e filtragem para remover quaisquer 
caracteres Unicode
"""
def getNGrams(content, n):
    content = re.sub('\n|[[d+\]]',' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    content = content.split(' ')
    content = [word for word in content if word != '']
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

html = requests.get('https://en.wikipedia.org/'
                    'wiki/Python_(programming_language)')
bs = BeautifulSoup(html.content, 'html.parser')
content = bs.find(
    'div', {'id':'mw-content-text'}
).get_text()
ngrams = getNGrams(content, 2)
print(ngrams)
print(f'2-grams count is: {str(len(ngrams))}')

"""
Esse código substitui todas as instâncias 
do caractere de quebra de linha por um espaço, 
remove citações como [123] e elimina todas as 
strings vazias, resultantes de vários espaços 
em branco sequenciais. Em seguida, os caracteres 
de escape são eliminados ao codificar o conteúdo 
com UTF-8.

Esses passos melhoram bastante o resultado da função, 
mas alguns problemas persistem:
['years', 'ago('], ['ago(', '-'], ['-', '-'], 
['-', ')'], [')', 'Stable']
"""