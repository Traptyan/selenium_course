import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def scroll(element):
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    answer = math.log(abs(12 * math.sin(int(x))))

    output = browser.find_element(By.CSS_SELECTOR, "#answer")
    output.send_keys(str(answer))

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    scroll(checkbox)
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    scroll(radiobutton)
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    scroll(button)
    button.click()


finally:
    time.sleep(10)
    browser.quit()
