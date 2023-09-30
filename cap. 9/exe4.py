from nltk import word_tokenize, sent_tokenize, pos_tag

"""
Nesse exemplo estamos usando a biblioteca 
NLTK (Natural Language Toolkit) para realizar 
tokenização de palavras e frases, bem como a 
marcação POS (part-of-speech) para identificar 
e extrair palavras específicas com determinadas 
classes gramaticais em um texto
"""


# Divide o texto em sentenças
sentences = sent_tokenize('Google is one of the best companies in the world.'\
' I constantly google myself to see what I\'m up to.')

nouns = ['NN', 'NNS', 'NNP', 'NNPS']
# NN = Substantivo, singular ou incontável
# NNS = Substantivo, plural
# NNP = Substantivo próprio, singular
# NNPS =  Substantivo próprio, plural

for sentence in sentences:
    if 'google' in sentence.lower():
        taggedWords = pos_tag(word_tokenize(sentence))
        for word in taggedWords:
            if word[0].lower() == 'google' and word[1] in nouns:
                print(sentence)


"""
Identifica frases que contenham a 
palavra 'google' como um substantivo 
nas classes gramaticais especificadas 
em nouns. É um exemplo de como a NLTK 
pode ser usada para análise linguística 
em texto.
"""