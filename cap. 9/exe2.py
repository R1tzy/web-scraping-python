import requests
from random import randint

"""    
Nesse exemplo vamos usar novamente o 
discurso do William Henry Harrison e 
usaremos o modelo markov que vai
gerar cadeias de Markov arbitrariamente 
longas (com o tamanho da cadeia definida 
com 100) com base na estrutura do texto:
"""

# Função para calcular a soma dos valores em um dicionário
def wordListSum(wordlist):
    sum = 0
    for word, value in wordlist.items():
        sum += value
    return sum


# Função para recuperar uma palavra aleatória com base nas probabilidades
def retrieveRandomWord(wordlist):
    randIndex = randint(1, wordListSum(wordlist))
    for word, value in wordlist.items():
        randIndex -= value
        if randIndex <= 0:
            return word


# Função para construir um dicionário de palavras a partir do texto
def buildWordDict(text):
    # Remove a quebra de linhas e aspas
    text = text.replace('\n',' ')
    text = text.replace('"', '')
    
    """
    Garante que sinais de pontuação sejam 
    tratados como "palavras" próprias

    Adiciona espaços antes e depois do símbolo
    de pontuação e divide o texto
    """
    punctuation = [',','.',';',':']
    for symbol in punctuation:
        # Adiciona espaços antes e depois do símbolo de pontuação
        text = text.replace(symbol, ' {} '.format(symbol))
    # Divide o texto para remover os espaços adicionados
    words = text.split(' ')

    # Filtra palavras vazias
    words = [word for word in words if word != '']

    # Inicializa um dicionário de palavras
    wordDict = {}
    for i in range(1, len(words)):
        """
        Como estamos usando prev_word e current_word. 
        Isso representa um bigrama. Se fosse trigrama seria:

        prev_word1 = words[i-2]
        prev_word2 = words[i-1]
        current_word = words[i]
        """
        prev_word = words[i-1]
        current_word = words[i]
        if prev_word not in wordDict:
            # Cria um novo dicionário para essa palavra
            wordDict[prev_word] = {}
        if current_word not in wordDict[prev_word]:
            # Inicializa o valor como 1 na primeira ocorrência
            wordDict[prev_word][current_word] = 1
        else:
            # Incrementa o valor se a palavra já existe no dicionário
            wordDict[prev_word][current_word] += 1
    return wordDict

# Faz uma solicitação HTTP para obter o conteúdo do discurso
response = requests.get('https://pythonscraping.com/'
                        'files/inaugurationSpeech.txt')
content = response.text

# Constrói o dicionário de palavras com base no conteúdo do discurso
wordDict = buildWordDict(content)

# Gera uma cadeia de Markov de tamanho 100
length = 100
chain = ['I']
for i in range(0, length):
    # Recupera uma nova palavra aleatória com base na palavra anterior
    newWord = retrieveRandomWord(wordDict[chain[-1]])
    chain.append(newWord)

# Imprime a cadeia de Markov gerada
print(' '.join(chain))

"""
Como vai funcionar o código

1 - Inicialização:

2 - Cadeia Inicial: ['I']
    Primeira iteração:
    Palavra anterior: 'I'
    Palavras possíveis após 'I': ['have'], 'will'], 'dream']
    Palavra selecionada aleatoriamente: 'have'
    Cadeia atualizada: ['I', 'have']

3 - Segunda iteração:
    Palavra anterior: 'have'
    Palavras possíveis após 'have': ['a']
    Palavra selecionada aleatoriamente: 'a'
    Cadeia atualizada: ['I', 'have', 'a']

vai seguir assim por diante até dar o tamanho de 100 

Como a cadeia de Markov usa estatística e nós utilizamos 
o radiant, a saída vai  ser diferente a cada execução
"""

"""
As cadeias de Markov modelam a ligação
entre os sites, de uma página para a próxima. 
Nesse sentido, as cadeias de Markov compõem a 
base tanto para pensar sobre web crawling quanto 
para saber como seus web crawlers podem pensar.
"""