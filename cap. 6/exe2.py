import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
from urllib.parse import urljoin, urlparse

"""
Downloads de arquivos internos, associados ao atributo
src de qualquer tag, da página inicial de pythonscraping.com
"""

downloadDirectory = 'img'
baseUrl = 'https://pythonscraping.com'


def getAbsoluteURL(baseUrl, source):
    # Verificar se a URL já é absoluta
    if source.startswith(('http://', 'https://')):
        return source

    # Tratar URLs relativas
    return urljoin(baseUrl, source)


def getDownloadPath(absoluteUrl, downloadDirectory):
    url_path = urlparse(absoluteUrl).path
    filename = os.path.basename(url_path)
    path = os.path.join(downloadDirectory, filename)
    directory =  os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path


html = requests.get('https://www.pythonscraping.com/')
bs = BeautifulSoup(html.content, 'html.parser')
# Pegando todos os src do site, menos de tag script
downloadList = bs.find_all(
    lambda tag: tag.has_attr('src') and tag.name != 'script'
)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, getDownloadPath(fileUrl, downloadDirectory))


"""
Esse programa foi escrito somente com finalidades ilustrativas;
ele jamais deverá ser empregado aleatoriamente, sem uma verificação
mais rígida dos nomes de arquivos, e deve ser executado apenas em
uma conta com permissões limitadas. Como sempre, fazer backup de seus
arquivos, não armazenar informações confidenciais em seu disco rígido
e usar um pouco de bom senso já ajuda bastante
"""
