from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


"""
Como alternativa do exe03.py, 
podemos escrever um laço semelhante 
que verifique o URL atual da página 
até que ele mude, ou até que corresponda 
a um URL específico que estamos procurando.
"""

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://pythonscraping.com/pages/javascript/redirectDemo1.html")
try:
    bodyElement = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (By.XPATH, '//body[contains(text(), '
            '"This is the page you are looking for!")]')
        )
    )
    print(bodyElement.text)
except:
    print('Elemento não encontrado')

"""
Nesse caso, estamos especificando 
um timeout de 15 segundos e um seletor 
XPath que procura o conteúdo do corpo 
da página para executar a mesma tarefa

Usamos uma expressão XPath para localizar 
o elemento <body> com o texto desejado

'//body' procura em qualquer lugar do 
documento HTML pela tag <body>.

[contains(text(), "This is the page you 
are looking for!")] verifica se o texto 
dentro de <body> contém "This is the page 
you are looking for!". Corrija as aspas 
simples finais para funcionar corretamente.
"""