import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.get('https://the-internet.herokuapp.com/login')
    driver.maximize_window()
    
    driver.find_element(By.ID, 'username').send_keys('tomsmith')
    driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    time.sleep(3)
    driver.quit()