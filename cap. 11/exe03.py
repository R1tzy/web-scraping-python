from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException
import time

def waitForLoad(driver):
    elem = driver.find_element(By.TAG_NAME, "html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5) # equivale a 0.5 segundos; 0.5 * 20 = 10 segundos
        try:
            elem = driver.find_element(By.TAG_NAME, "html")
        except StaleElementReferenceException:
            return

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)
driver.close()

"""
Esse script verifica a página a 
cada meio segundo, com um timeout 
de 10 segundos, porém os tempos 
usados para verificação e timeout
podem ser ajustados com facilidade, 
para cima ou para baixo, conforme 
necessário.
"""