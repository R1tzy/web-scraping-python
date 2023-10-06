from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get('https://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
print(driver.find_element(By.ID, 'content').text)
driver.close()

"""
Apesar de funcionar, essa solução é ineficiente

Os tempos de carga de página são inconsistentes 
e dependem da carga do servidor em qualquer 
instante específico; 

Embora a carga dessa página deva demorar pouco 
mais que dois segundos, estamos lhe concedendo
três segundos inteiros para garantir que ela seja 
totalmente carregada. Uma solução mais eficiente 
seria verificar repetidamente a existência de um 
elemento específico em uma página carregada por 
completo e retornar apenas quando esse elemento 
existir.

"""