import requests
import csv
from io import StringIO

"""
A biblioteca csv de Python trabalha com arquivos locais, 
ou seja, é necessário ter os dados CSV armazenados em seu 
computador. Como esse nem sempre será o caso, ainda mais 
quando se trata de web scraping. 

Há várias maneiras de contornar essa situação:
• Faça download do arquivo localmente, de modo manual
• Escreva um script Python para fazer download do arquivo, 
leia-o e (opcionalmente) apague o arquivo após obter seus 
dados.
• Obtenha o arquivo da web na forma de uma string e encapsule
a string

As duas primeiras opções são viáveis, mas ocupar espaço no disco
quando seria fácil mantê-los em memória não é uma boa prática. 
A terceira opção é a mais indicada. 
"""

response = requests.get('http://pythonscraping.com/files/MontyPythonAlbums.csv')
data = response.text
data = data.encode('ascii', 'ignore').decode('ascii')
#contém o conteúdo do arquivo CSV  com caracteres não-ASCII ignorados

dataFile = StringIO(data)

# 1 Forma de fazer apresentação do csv e tirar o cabeçalho
# csvReader = csv.reader(dataFile)
# Use uma variável de controle para ignorar a primeira linha
# first_row = True
# for row in csvReader:
#     if first_row:
#         first_row = False
#         continue # Ignora a primeira linha
#     print(f'The album {row[0]} was released in {row[1]}')


# 2 Forma de fazer a apresentação do csv e tirar o cabeçalho
""" 
Ao transformar em um dicionário, ele elimina o cabeçalho que não 
tem dado nenhum
A desvantagem é que demora um pouco mais para criar,
processar e exibir esses objetos DictReader, em comparação 
com csvReader, porém a conveniência e a usabilidade compensam 
o overhead adicional. 

Overhead - sobrecarga ao servidor da web ou à rede em que está operando.
"""
dictReader = csv.DictReader(dataFile) 
for row in dictReader:
    print(f"The album {row['Name']} was release in {row['Year']}.")




