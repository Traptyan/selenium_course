import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from findby import FindElement

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = FindElement(browser)

    elements = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for element in elements:
        element.send_keys("AMOGUS")

    button = FindElement.css(a, "button.btn")
    button.click()


finally:
    time.sleep(30)
    browser.quit()
