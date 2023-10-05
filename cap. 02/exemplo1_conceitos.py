import requests
from bs4 import BeautifulSoup

html =  requests.get('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.content, 'html.parser')
# namelist = bs.find_all('span', {'class': 'green'}) # attributes aceita um dicionário Python 
# for name in namelist: #'span', {'class':{'green', 'red'}}
#     print(name.text) #ou get_text()

namelist = bs.find_all(string='the prince') #args string, procura pelo texto informado
print(len(namelist))
# test = bs.find(id='text') #argumento keyword

# resultado = [name.text for name in namelist]
# resultado = list(map(lambda x: x.replace('\n', ' '), resultado))
# print(*resultado)

#argumento recursive do bs4 é um booleano, por padrão é sempre true (analisa os filhos, dos filhos...)