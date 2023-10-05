import requests
from bs4 import BeautifulSoup
import re
import string

"""
É claro que a pontuação em si tem sentido, 
e simplesmente a remover pode resultar na 
perda de algumas informações importantes. 
Portanto caso você queira descartar n-gramas 
que cruzem um ponto final, como nesse caso, 
é viável considerar apenas os ngramas criados 
dentro da sentença.
"""

"""
A função cleanSentence separa a sentença
em palavras, remove pontuações e espaços 
em branco, além de eliminar palavras com um 
único caractere que não sejam I e a.
"""
def cleanSentence(sentence):
    sentence = sentence.split(' ')
    """
    Para cada palavra na lista sentence, 
    vai ser removido tanto a pontuação 
    quanto os caracteres de espaço em branco 
    do início e do final da palavra.
    """
    sentence = [word.strip(string.punctuation+string.whitespace) 
                for word in sentence]
    sentence = [word for word in sentence if len(word) > 1 or 
                (word.lower() == 'a' or word.lower() == 'i')]
    return sentence

"""
A função cleanInput remove quebras de linha e 
citações, como antes, mas também separa o texto 
em “sentenças” com base na posição dos pontos 
finais seguidos de um espaço
"""
def cleanInput(content):
    content = re.sub('\n|[[\d+\]]',' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    sentences = content.split('. ')
    return [cleanSentence(sentence) for sentence in sentences]

"""
As linhas principais que criam os n-gramas 
foram passadas para getNgramsFromSentence, 
que é chamada em cada sentença por getNgrams. 
Isso garante que n-gramas que se estendam por 
várias sentenças não sejam criados
"""
def getNGramsFromSentence(content, n):
    output = []
    for i in range(len(content) - n+1):
        output.append(content[i:i+n])
    return output

"""
A função getNgrams recebe uma string de entrada, 
separa essa string em uma sequência de palavras 
e acrescenta o n-grama (nesse caso, um bigrama) 
iniciado por cada palavra em um array.
"""
def getNGrams(content, n):
    content = cleanInput(content)
    ngrams = []
    for sentence in content:
        ngrams.extend(getNGramsFromSentence(sentence, n))
    return ngrams


html = requests.get('https://en.wikipedia.org/'
                    'wiki/Python_(programming_language)')
bs = BeautifulSoup(html.content, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
ngrams = getNGrams(content, 2)
print(ngrams)
print(f'2-grams count is: {str(len(ngrams))}')

"""
Ao usar item.strip(string.punctuation+string.whitespace) 
em um laço que itera por todas as palavras do conteúdo, 
qualquer caractere de pontuação de qualquer lado da palavra
será removido, porém palavras com hífen

Isso resulta em bigramas muito mais limpos:
[['Python', 'Paradigm'], ['Paradigm', 'Object-oriented']...

"""