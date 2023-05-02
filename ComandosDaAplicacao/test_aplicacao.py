import time
from selenium import webdriver

browser = webdriver.Chrome()
# Get: Acessa a página
browser.get('https://getbootstrap.com/')

# Imprimir Título
print(f"O título da página é {browser.title}")

# current_url
print(f"O url da página é {browser.current_url}")

# page_source
print(f"O código fonte da página é {browser.page_source}")