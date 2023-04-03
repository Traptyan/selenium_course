from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def findCSS (selector):
    return browser.find_element(By.CSS_SELECTOR, selector)


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    first_name = findCSS("[name='firstname']")
    first_name.send_keys("Sanyara")
    
    last_name = findCSS("[name='lastname']")
    last_name.send_keys("Sayonara")
    
    email = findCSS("[name='email']")
    email.send_keys("Sanyara_Sayonara")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    
    file = findCSS("#file")
    file.send_keys(file_path)
    
    submit = findCSS(".btn")
    submit.click()
    
    
finally:
    time.sleep(10)
    browser.quit()