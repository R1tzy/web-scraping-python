import requests
from bs4 import BeautifulSoup


html = requests.get('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.content, 'html.parser')

#Lidando com filhos e descendentes
#para encontrar somente os filhos, use .children
#para encontrar todos os descendentes use a .descendants
# for child in bs.find('table', {'id':'giftList'}).children:
#     print(child)

#Lidando com irmãos
#next_siblings chama somente os próximos (next) irmãos
# for sibilings in bs.find('table', {'id':'giftList'}).tr.next_siblings:
#     print(sibilings)
#também há o previous_siblings que retornar os irmãos anteriores

#Lidando com pais
#não é muito comum como filhos e irmãos, mas pode ser necessário
print(
    bs.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.text
)
#encontra a tag img com a src='../img/gifts/img1.jpg', veja o pai dessa tag que no caso é td, e pega o td irmão anterior no formato texto

