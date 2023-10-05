import requests
from bs4 import BeautifulSoup
import re
import string
from collections import Counter

"""
vai usar o discurso do presidente americano 
William Henry Harrison como fonte de dados 
para encontrar um conjunto de bigramas e devolver
um objeto Counter
"""

def cleanSentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace)
                for word in sentence]
    sentence = [word for word in sentence if len(word) > 1 or 
                (word.lower() == 'a' or word.lower() == 'i')]
    return sentence


def cleanInput(content):
    content = re.sub('\n',' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    sentences = content.split('. ')
    return [cleanSentence(sentence) for sentence in sentences]


def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content) - n+1):
        output.append(content[i:i+n])
    return output

"""
Função usada para eliminar os bigramas 
com as palavras mais comuns
"""
def isCommon(ngram):
    commonWords = [
        'THE', 'BE', 'AND', 'OF', 'A', 'IN', 'TO', 'HAVE', 'IT', 'I',
        'THAT', 'FOR', 'YOU', 'HE', 'WITH', 'ON', 'DO', 'SAY', 'THIS', 'THEY',
        'IS', 'AN', 'AT', 'BUT', 'WE', 'HIS', 'FROM', 'THAT', 'NOT', 'BY',
        'SHE', 'OR', 'AS', 'WHAT', 'GO', 'THEIR', 'CAN', 'WHO', 'GET', 'IF',
        'WOULD', 'HER', 'ALL', 'MY', 'MAKE', 'ABOUT', 'KNOW', 'WILL', 'AS',
        'UP', 'ONE', 'TIME', 'HAS', 'BEEN', 'THERE', 'YEAR', 'SO', 'THINK',
        'WHEN', 'WHICH', 'THEM', 'SOME', 'ME', 'PEOPLE', 'TAKE', 'OUT', 'INTO',
        'JUST', 'SEE', 'HIM', 'YOUR', 'COME', 'COULD', 'NOW', 'THAN', 'LIKE',
        'OTHER', 'HOW', 'THEN', 'ITS', 'OUR', 'TWO', 'MORE', 'THESE', 'WANT',
        'WAY', 'LOOK', 'FIRST', 'ALSO', 'NEW', 'BECAUSE', 'DAY', 'MORE', 'USE',
        'NO', 'MAN', 'FIND', 'HERE', 'THING', 'GIVE', 'MANY', 'WELL'
    ]
    for word in ngram:
        if word is commonWords:
            return True
    return False


def getNgrams(content, n):
    content = cleanInput(content)
    ngrams = Counter()
    ngrams_list = []
    for sentence in content:
        newNgrams = [' '.join(ngram) for ngram 
                     in getNgramsFromSentence(sentence, n)]
        for ngram in newNgrams:
            if not isCommon(ngram.split()):
                ngrams_list.extend(newNgrams)
                ngrams.update(newNgrams)
    return ngrams

response = requests.get('https://pythonscraping.com/'
                        'files/inaugurationSpeech.txt')
content = response.text

ngrams = getNgrams(content, 2)
print(ngrams)

"""
Utilizando desse métodos (n-grams) e das palavras 
mais comuns, podemos inferir de forma objetiva um 
resumo dessa fonte de dados, de certo nível adequado 
para uma primeira análise
"""