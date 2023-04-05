import math
import time

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from findby import FindElement

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    a = FindElement(browser)

    browser.get(link)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = FindElement.css(a, "#book")
    button.click()

    x_element = FindElement.css(a, "#input_value")
    x = x_element.text

    answer = math.log(abs(12 * math.sin(int(x))))

    output = FindElement.css(a, "#answer")
    output.send_keys(str(answer))

    button = FindElement.css(a, "#solve")
    button.click()

    result_element = browser.switch_to.alert
    result = result_element.text

    pyperclip.copy(result.split(': ')[-1])

finally:
    time.sleep(10)
    browser.quit()
