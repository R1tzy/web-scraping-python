import csv

"""
Modificar um arquivo CSV ou até mesmo criar um 
totalmente do zero é muito fácil com a biblioteca 
Python csv:
"""
# Abre novo arquivo para gravação - apagará o arquivo se ele já existir
csvFile = open('cap. 6/teste.csv', 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('número', 'número +2', 'número * 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csvFile.close()

"""
Se teste.csv ainda não existir, Python criará
o arquivo (mas não o diretório) automaticamente. 
Se já existir, o arquivo teste.csv será sobrescrito 
com os novos dados.
"""