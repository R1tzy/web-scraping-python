import requests
from bs4 import BeautifulSoup
import re
import string
from collections import Counter

"""
Usando o código de n-grama 
do exe3.py, recursos para normalização
de dados podem ser acrescentados.

Um problema do código do exe3.py é que ele 
contém vários bigramas duplicados. Todo bigrama 
encontrado pelo código é adicionado à lista, sem 
que sua frequência seja registrada. 

Anotar a frequência desses bigramas, como também 
esses dados podem ser convenientes para colocar os 
efeitosdas mudanças nos algoritmos de limpeza e de 
normalização de dados em um gráfico. 
"""

def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace) 
                for word in sentence]
    sentence = [word for word in sentence if len(word) > 1 or 
                (word.lower() == 'a' or word.lower() == 'i')]
    return sentence


def cleanInput(content):
    content = re.sub('\n|[[\d+\]]',' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    sentences = content.split('. ')
    return [cleanSentence(sentence) for sentence in sentences]


def getNGramsFromSentence(content, n):
    output = []
    for i in range(len(content) - n+1):
        output.append(content[i:i+n])
    return output

"""
Um objeto Counter também tem uma
desvantagem: ele não é capaz de 
armazenar listas (não é possível ter 
hashes com listas), portanto é necessário 
fazer antes uma conversão para strings
usando um ' '.join(ngram) em uma list 
comprehension para cada n-grama.
"""
def getNGrams(content, n):
    content = cleanInput(content)
    ngrams = Counter()
    for sentence in content:
        newNgrams = [
            ' '.join(ngram) for ngram in 
            getNGramsFromSentence(sentence, 2)
        ]
        ngrams.update(newNgrams)
    return ngrams


html = requests.get('https://en.wikipedia.org/'
                    'wiki/Python_(programming_language)')
bs = BeautifulSoup(html.content, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
ngrams = getNGrams(content, 2)
print(ngrams)
print(f'2-grams count is: {str(len(ngrams))}')

