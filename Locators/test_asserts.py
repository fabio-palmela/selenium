import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
# Get: Acessa a página
browser.get('https://www.saucedemo.com/')

lista_inputs = browser.find_elements(By.XPATH, "//*[@class='input_error form_input']")

assert len(lista_inputs) == 2, "Deu ruim"

time.sleep(1)

browser.quit()
