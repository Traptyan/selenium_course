import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:

    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_number_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    first_number = first_number_element.text

    second_number_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    second_number = second_number_element.text

    answer = int(first_number) + int(second_number)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(answer))

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
