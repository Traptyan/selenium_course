from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    first_name_input.send_keys("Kolya")

    last_name_input = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    last_name_input.send_keys("Kolyaenko")

    email_input = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    email_input.send_keys("Kolya.Kolyaenko@kolyan.com")

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

    time.sleep(1)

    congrats = browser.find_element(By.TAG_NAME, "h1")
    congrats_text = congrats.text

    assert "Congratulations! You have successfully registered!" == congrats_text

finally:
    time.sleep(10)
    browser.quit()