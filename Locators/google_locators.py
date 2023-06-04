from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestGoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.google.com/")
    
    def test_search(self):
        search_input = self.driver.find_element(By.NAME, "q")
        search_input.send_keys("python selenium")
        search_input.submit()
        assert "python selenium" in self.driver.title
        time.sleep(5) # pausa a execução por 5 segundos

    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
