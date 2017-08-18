from locators import HomePageLocators
from locators import ListingPageLocators
from locators import DetailsPageLocators
from locators import BookingReviewPageLocators
from Utils import Utils
from selenium import webdriver

class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def actions(self,object):
        action = webdriver.ActionChains(self.driver)
        text = self.driver.find_element(object)
        return action.move_to_element(text).click()

class HomePage(BasePage):

    def clickPopularCityFromAutosuggest(self):
        self.driver.find_element(*HomePageLocators.Search_editbox).click()
        city = self.driver.find_elements(*HomePageLocators.AutoSuggest_PopularCities)
        city[2].click()

    def clickSearchButton(self):
        self.driver.find_element(*HomePageLocators.Search_button).click()

    def enterSearchTextInDestination(self):
        self.driver


class ListingPage(BasePage):

    def clickPropertyCrad(self):
        cards = self.driver.find_elements(*ListingPageLocators.Property_card)
        cards[0].click()

class DetailsPage(BasePage):

    def enterText(self,label):
        if label == 'name':
            return self.driver.find_element(*DetailsPageLocators.Popup_name_editbox).send_keys('Test')
        elif label =='email':
            return self.driver.find_element(*DetailsPageLocators.Popup_email_editbox).send_keys('rightstaytestggn@gmail.com')
        elif label =='phone':
            return self.driver.find_element(*DetailsPageLocators.Popup_phone_editbox).send_keys('9090909090')
        elif label =='message':
            return self.driver.find_element(*DetailsPageLocators.Popup_message_editbox).send_keys('This request is automated')

    def clickButton(self,btnName):
        if btnName == 'ask Host':
            return self.driver.find_element(*DetailsPageLocators.Ask_the_host_button).click()
        elif btnName == 'send Message':
            return self.driver.find_element(*DetailsPageLocators.Popup_send_message_button).click()
        elif btnName == 'continue Browsing':
            return self.driver.find_element(*DetailsPageLocators.Popup_continue_browsing_button).click()
        else:
            return self.driver.find_element(*DetailsPageLocators.Next_page_button).click()




