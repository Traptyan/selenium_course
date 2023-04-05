import os
import time

from selenium import webdriver

from findby import FindElement


def findcss(selector):
    return FindElement.css(a, selector)


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a = FindElement(browser)

    first_name = findcss("[name='firstname']")
    first_name.send_keys("Sanyara")

    last_name = findcss("[name='lastname']")
    last_name.send_keys("Sayonara")

    email = findcss("[name='email']")
    email.send_keys("Sanyara_Sayonara")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    file = findcss("#file")
    file.send_keys(file_path)

    submit = findcss(".btn")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()
