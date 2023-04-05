import math
import time

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By


def findCSS(selector):
    return browser.find_element(By.CSS_SELECTOR, selector)


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    start_btn = findCSS(".btn")
    start_btn.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # --------------------------------------------------------

    x_element = findCSS("#input_value")
    x = x_element.text

    answer = math.log(abs(12 * math.sin(int(x))))

    output = browser.find_element(By.CSS_SELECTOR, "#answer")
    output.send_keys(str(answer))

    button = findCSS(".btn")
    button.click()

    result_element = browser.switch_to.alert
    result = result_element.text

    pyperclip.copy(result.split(': ')[-1])

finally:
    time.sleep(10)
    browser.quit()
