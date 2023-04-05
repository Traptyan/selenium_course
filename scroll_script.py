import math
import time

from selenium import webdriver

from findby import FindElement


def scroll(element):
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a = FindElement(browser)

    x_element = FindElement.css(a, "#input_value")
    x = x_element.text

    answer = math.log(abs(12 * math.sin(int(x))))

    output = FindElement.css(a, "#answer")
    output.send_keys(str(answer))

    checkbox = FindElement.css(a, "#robotCheckbox")
    scroll(checkbox)
    checkbox.click()

    radiobutton = FindElement.css(a, "#robotsRule")
    scroll(radiobutton)
    radiobutton.click()

    button = FindElement.css(a, ".btn")
    scroll(button)
    button.click()


finally:
    time.sleep(10)
    browser.quit()
