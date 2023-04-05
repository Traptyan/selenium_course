import math
import time

from selenium import webdriver

from findby import FindElement


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    a = FindElement(browser)
    browser.get(link)

    treasure_element = FindElement.css(a, "#treasure")
    x = treasure_element.get_attribute("valuex")

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
