import smtplib
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
import time

"""
Faz o web scraping do site https://isitchristmas.com/ para
verificar se é natal ou não, e envia um email caso seja natal.
Pode parecer bobo mas é um exemplo de como o web scraping pode
ser usado, por exemplo. Caso tenha algum produto que você queria
mas esteja fora de estoque, é possível criar um script para ser
executado periodicamente para verificar se tal produto está
disponível e se esiver envia um email avisando.
"""

def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'fox_raposa64@hotmail.com'
    msg['To'] =  'thiagolopesalmeida1230@gmail.com'

    s = smtplib.SMTP(host='localhost', port=1025)
    s.send_message(msg)
    s.quit()

html = requests.get('https://isitchristmas.com/')
bs = BeautifulSoup(html.text, 'html.parser')

while(bs.find('a', {'id':'answer'}).attrs['title'] == 'NÃO'):
    print('Ainda não é natal!!')
    time.sleep(3600)
    html = requests.get('https://isitchristmas.com/')
    bs = BeautifulSoup(html.text, 'html.parser')

sendMail('É natal!', 'De acordo com https://isitchristmas.com/, hoje é natal!')