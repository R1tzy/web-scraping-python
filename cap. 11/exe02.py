# Importa as bibliotecas necessárias do Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Configuração das opções do navegador Chrome, 
no modo "headless" (sem interface gráfica)
""" 
options = webdriver.ChromeOptions()
options.add_argument("--headless")

"""
Inicializa o driver do navegador Chrome 
com as opções configuradas
"""
driver = webdriver.Chrome(options=options)

# Abre a página web desejada
driver.get("https://pythonscraping.com/pages/javascript/ajaxDemo.html")

try:
    """
    Aguarda até que o elemento com o ID 
    'loadedButton' esteja presente na página
    """
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'loadedButton'))
    )
finally:
    """
    Após o elemento ser encontrado, imprime 
    o texto do elemento com o ID 'content'
    """
    print(driver.find_element(By.ID, 'content').text)

    # Fecha o navegador
    driver.close()

"""
Uma espera implícita esperar que um
determinado estado no DOM ocorra antes 
de prosseguir

Uma espera explícita define um tempo 
fixo, como no exemplo anterior, em que
a espera era de três segundos

Nesse caso foi definido uma espera implícita, 
o estado do DOM a ser detectado é definido por 
expected_condition (que usa uma convenção comum 
EC).
"""