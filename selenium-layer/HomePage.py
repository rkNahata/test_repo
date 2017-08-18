from Utils import Utils

class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def searchBoxEnterText(self):
        searchbox = self.driver.find_element_by_class_name('_2nOJuPvch8NVWZz5MwAZLD')
        searchbox.clear()
        return searchbox

    def selectItemfromAutosuggest(self):
        autosuggest = self.driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div[2]/div//ul[1]//button')
        return autosuggest

    def clickSearchButton(self):
        submitbtn = self.driver.find_element_by_class_name("_2t3YQsLhI2BWf222ZLLqFH")
        return submitbtn

    def clickCheckIn(self):
        actions = Utils(self.driver)
        checkIn = actions.actions('//*[@id="content"]/div/div/div/div/div/div[2]//div[2]//input')
        return checkIn

    def clickCheckOut(self):
        actions = Utils(self.driver)
        checkOut = actions.actions('//*[@id="content"]/div/div/div/div/div/div[2]//div[3]//input')
        return checkOut

    def clickGuests(self):
        actions = Utils(self.driver)
        guests = actions.actions('//*[@id="content"]//div[2]//div[4]//input')
        return guests