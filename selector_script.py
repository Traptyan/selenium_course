from selenium import webdriver

from findby import FindElement

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
a = FindElement(browser)

button = FindElement.id(a, "submit_button")
button.click()

# закрываем браузер после всех манипуляций
browser.quit()
