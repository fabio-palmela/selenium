import time
from selenium import webdriver

browser = webdriver.Chrome()
# Get: Acessa a página
browser.get('https://google.com')

# Maximize Window: Máximiza a tela
browser.maximize_window();

# Refresh: Atualiza Browser
time.sleep(1)
browser.refresh()


browser.get('https://getbootstrap.com/')

# Back: Voltar navegação 
browser.back()

# Forward: Avançar navegação
browser.forward()

# Close: Fecha tab ativa
browser.switch_to.new_window("tab")
#time.sleep(1)
#browser.close()



# Quit: Fecha todas abas
browser.switch_to.new_window("tab1")
browser.switch_to.new_window("tab3")
time.sleep(2)
browser.quit()


# browser.find_element_by_id(" ?? ").click()
#browser.find_elements_by_xpath("//*[contains(a, 'login')]")
# //*[contains(a, 'login')]

time.sleep(2)
