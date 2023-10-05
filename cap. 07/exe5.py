from zipfile import ZipFile
from io import BytesIO
import requests
from bs4 import BeautifulSoup

# Baixa o arquivo DOCX da URL e obtém seu conteúdo binário
wordFile = requests.get('http://pythonscraping.com/pages/AWordDocument.docx').content
# Cria um objeto de fluxo de bytes (BytesIO) a partir dos dados binários do arquivo
wordFile = BytesIO(wordFile)
# Abre o arquivo DOCX como um arquivo ZIP usando ZipFile
document = ZipFile(wordFile)
# Lê o conteúdo do arquivo XML que armazena o conteúdo do documento do Word
xml_content = document.read('word/document.xml')
# # Decodifica o conteúdo binário em uma string UTF-8 e imprime
# print(xml_content.decode('UTF-8'))

wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'xml')
textStrings = wordObj.find_all('w:t')
for texElem in textStrings:
    style = texElem.parent.parent.find('w:pStyle')
    if style is not None and style['w:val'] == "Title":
        print(f"Title is {texElem.text}")
    print(texElem.text)