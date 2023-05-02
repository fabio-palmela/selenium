import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
# Get: Acessa a página
browser.get('https://demo.applitools.com/')

username = browser.find_element(By.ID, 'username')
check = browser.find_element(By.XPATH, "//*[@type='checkbox']")

print(username.is_displayed())
assert username.is_displayed()
 
print(username.is_enabled())
assert username.is_enabled()
 
time.sleep(1)

#check.click()
time.sleep(1)

print(check.is_selected())
assert not check.is_selected(), 'errou'