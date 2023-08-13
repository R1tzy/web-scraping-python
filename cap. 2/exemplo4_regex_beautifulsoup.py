import requests
from bs4 import BeautifulSoup
import re

#Quero fazer o web scraping das imagens de um site, mas não posso simplesmente usar a tag <img>. Podemos usar o regex para diferenciar as imagens que queremos daquelas que não queremos
#o padrão do site é <img src="../img/gifts/img3.jpg">

url = requests.get('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(url.content, 'html.parser')
# imagens = bs.find_all('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
# for image in imagens:
#     print(image['src'])

# imagens = bs.img.attrs['src'] #posso fazer isso, mas é meio inútil e volta apenas o primeiro achado
#fazendo isso pegamos todas as imagens com esse formato ../img/gifts/img{valor}.jpg