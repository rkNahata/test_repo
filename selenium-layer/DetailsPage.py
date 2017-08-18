from Utils import Utils

class DetailsPage:

    def __init__(self,driver):
        self.driver = driver

    def clickButton(self,btnName):
        if btnName == 'ask Host':
            return self.driver.find_element_by_xpath("//button[@class='_2_fqhwTSVDeIV6EDPtLLwF ripplebutton btn btn-default']")
        elif btnName == 'send Message':
            return self.driver.find_element_by_class_name("_1YDtDMwTsdZnQJ-Z114bLZ")
        elif btnName == 'continue Browsing':
            return self.driver.find_element_by_class_name('errorModalButton')
        else:
            return self.driver.find_element_by_xpath("//button[@class='_34T6us-YHgUxHnTsR2nPE6 callToActionButton callToActionButton2 hidden-xs btn btn-default']")

    def enterText(self,label):
        driver = self.driver
        actions = Utils(driver)
        if label == 'name':
            return actions.actions('name')
        elif label =='email':
            return actions.actions('email')
        elif label =='phone':
            return actions.actions('phone')
        else:
            return actions.actions('message')





