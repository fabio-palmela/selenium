import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.implicitly_wait(12)#Realiza verificações por x segundos até que o elemento seja encontrado.
# Get: Acessa a página
browser.get('https://srv-probat/plataforma_pj_credito/')
# browser.get('https://intranetnlb/plataforma_pj_credito/')
browser.maximize_window();




searchCliente = browser.find_element(By.ID, "search")
searchCliente.send_keys('05907569662')

#print(dropdownClientes)
dropdownClientes = browser.find_elements(By.XPATH, "//*[@id='ui-id-1']/li")[0]
dropdownClientes.click()
#dropdownClientes.select_by_visible_text('05907569662')
buttonPesquisar = browser.find_element(By.ID, "botao-search")
buttonPesquisar.click()




# searchCliente = browser.find_element(By.ID, "search")
# searchCliente.send_keys('05907569662')
# listaClientes = browser.find_elements(By.ID, "ui-id-1")
# qtdeClientes = len(listaClientes)
# print(qtdeClientes)
# assert qtdeClientes > 1, "Registro em duplicidade."
# assert qtdeClientes < 1, "Registro não encontrado."
# clienteResult = browser.find_element(By.ID, "ui-id-4")
# clienteResult.click()
# pesquisarCliente = browser.find_element(By.ID, "botao-search")
# pesquisarCliente.click()

# planilhamentoCliente = browser.find_element(By.PARTIAL_LINK_TEXT, "//*[@id='hrefPlanilhamento']")
# print(planilhamentoCliente)
# planilhamentoCliente.click()

browser.switch_to.new_window('Planilhamento')
# browser.get('https://srv-probat/planilhamento/dossie/modulo/detalhamento/05907569662')
browser.get('https://srv-probat/planilhamento/dossie/modulo/detalhamento/05907569662')

editarPlanilhamento = browser.find_element(By.XPATH, "//*[contains(@type, 'button') and contains(text(), 'Novo/Editar planilhamento')]")
editarPlanilhamento.click()


# myLink = browser.find_element(By.PARTIAL_LINK_TEXT, 'New Article')
#     myLink.click()

# time.sleep(1)
#//*[@id="search"]
# username = browser.find_element(By.ID, 'user-name')
# password = browser.find_element(By.ID, 'password')
# btn_button = browser.find_element(By.ID, 'login-button')

# username.send_keys('standard_user')
# password.send_keys('secret_sauce')

# btn_button.click()

# products_title = browser.find_element(By.XPATH, "//span[@class='title']")
# print(products_title.text)
# assert products_title.text == "Products"

# imagem = browser.find_element(By.XPATH, "(//img[@class='bm-icon'])[1]")
# print(imagem.get_attribute('alt'))

wait = WebDriverWait(browser, 5)

check_id = ['chk1', 'chk2', 'chk3']
for check in check_id:
    checkbox = f'//input[@id="{check}"]/ancestor::label'
    checkbox_label = wait.until(EC.visibility_of_element_located((By.XPATH, checkbox)))
    checkbox_label.click()
    data_balanco = f'//input[@id="{check}"]/ancestor::div/input'
    data_input = wait.until(EC.visibility_of_element_located((By.XPATH, data_balanco)))
    data_input.send_keys('2020')
    
btnGerarPlanilhamento = browser.find_element(By.ID, 'botao-confirmar-modal')
btnGerarPlanilhamento.click()

# Clicar no rótulo (o que selecionará o checkbox)

# Clicar no checkbox
# checkbox.click()

time.sleep(2)



# segBalanco = browser.find_element(By.XPATH, "//*[@id='chk2']")
# segBalanco.click()
# terBalanco = browser.find_element(By.XPATH, "//*[@id='chk3']")
# terBalanco.click()


time.sleep(3)
browser.quit()
