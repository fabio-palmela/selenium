import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
# Get: Acessa a página
browser.get('https://google.com')

# Maximize Window: Máximiza a tela
browser.maximize_window();

# Refresh: Atualiza Browser
time.sleep(1)

browser.find_elements(By.XPATH, "//*[contains(a, 'login')]")
# //*[contains(a, 'login')])
# browser.find_element_by_id(" ?? ").click()
#browser.find_elements_by_xpath("//*[contains(a, 'login')]")
# //*[contains(a, 'login')]

time.sleep(2)
