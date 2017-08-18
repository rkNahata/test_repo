from selenium import webdriver
class Utils:

    def __init__(self,driver):
        self.driver = driver

    def actions(self,elementpath):
        action = webdriver.ActionChains(self.driver)
        text = self.driver.find_element_by_name(elementpath)
        return action.move_to_element(text).click()


