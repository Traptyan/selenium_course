from selenium.webdriver.common.by import By


class FindElement:

    def __init__(self, context):
        self.context = context

    def css(self, selector):
        return self.context.find_element(By.CSS_SELECTOR, selector)

    def id(self, selector):
        return self.context.find_element(By.ID, selector)
