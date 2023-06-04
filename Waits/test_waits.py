import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
# Get: Acessa a página
browser.get('https://www.saucedemo.com/')

username = browser.find_element(By.ID, 'user-name')
password = browser.find_element(By.ID, 'password')

username.send_keys('standard_user')
password.send_keys('secret_sauce')

time.sleep(3)
loginButton = browser.find_element(By.ID, 'login-button')

loginButton.send_keys(Keys.ENTER)

time.sleep(3)
browser.quit()
