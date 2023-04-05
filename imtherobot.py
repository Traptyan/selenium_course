import math
import time

from selenium import webdriver

from findby import FindElement


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a = FindElement(browser)

    x_element = FindElement.css(a, "#input_value")
    x = x_element.text

    answer = calc(x)

    answer_field = FindElement.css(a, "#answer")
    answer_field.send_keys(answer)

    checkbox = FindElement.css(a, "#robotCheckbox")
    checkbox.click()

    radiobutton = FindElement.css(a, "#robotsRule")
    radiobutton.click()

    submit = FindElement.css(a, ".btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
