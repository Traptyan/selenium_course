from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pyperclip

	
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
	
    browser.get(link)
	
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    
    answer = math.log(abs(12*math.sin(int(x))))
    
    output = browser.find_element(By.CSS_SELECTOR, "#answer")
    output.send_keys(str(answer))
    
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()    
    
    result_element = browser.switch_to.alert
    result = result_element.text
    
    pyperclip.copy(result.split(': ')[-1])
    
finally:
    time.sleep(10)
    browser.quit()