import requests
from io import BytesIO
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams

"""
requests - solicitações HTTP e obter o conteúdo do PDF da web.
io.BytesIO - cria um objeto de bytes a partir do conteúdo binário do PDF.
pdfminer.high_level.extract_text - extrai texto do PDF.
pdfminer.layout.LAParams - configurar parâmetros para o processamento do PDF.
"""

def readPDF(pdfContent):
    # LAParams não está fazendo nada nesse caso
    laparams = LAParams()
    text = extract_text(BytesIO(pdfContent), laparams=laparams)
    return text

pdf_url = 'http://pythonscraping.com/pages/warandpeace/chapter1.pdf'
response = requests.get(pdf_url)

if response.status_code == 200:
    pdf_content = response.content
    outputString = readPDF(pdf_content)
    print(outputString)
else:
    print(f'Falha ao acessar a URL. Código de status: {response.status_code}')
