import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.implicitly_wait(12)

browser.maximize_window()

browser.implicitly_wait(12)#Realiza verificações por x segundos até que o elemento seja encontrado.
# Get: Acessa a página
browser.get('https://chercher.tech/practice/practice-dropdowns-selenium-webdriver')
browser.maximize_window();


dropdownClientes = Select(browser.find_element(By.XPATH, "//*[@id='ui-id-1']/li"))



dropdownClientes = Select(browser.find_element(By.XPATH, "//select[@id='first']"))
dropdownClientes.select_by_visible_text('Google')

dropdownAnimals = Select(browser.find_element(By.XPATH, "//select[@id='animals']"))
dropdownAnimals.select_by_value("babycat")

time.sleep(1)

dropdownAnimals.select_by_index(3)

time.sleep(1)

dropdownFood = Select(browser.find_element(By.XPATH, "//select[@id='second']"))
dropdownFood.select_by_visible_text("Pizza")
time.sleep(1)
dropdownFood.select_by_visible_text("Bonda")
time.sleep(1)

# dropdownClientes.send_keys('05907569662')

# listaClientes = browser.find_elements(By.ID, "ui-id-1")

# qtdeClientes = len(listaClientes)
# print(qtdeClientes)

# pesquisarCliente = browser.find_element(By.ID, "botao-search")
# pesquisarCliente.click()



# browser.switch_to.new_window('Planilhamento')
# browser.get('https://srv-probat/planilhamento/dossie/modulo/detalhamento/05907569662')

# editarPlanilhamento = browser.find_element(By.XPATH, "//*[contains(@type, 'button') and contains(text(), 'Novo/Editar planilhamento')]")
# editarPlanilhamento.click()


time.sleep(3)
browser.quit()
