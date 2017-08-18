import unittest
from selenium import webdriver
import time
from HomePage import HomePage
from ListingPage import ListingPage
from DetailsPage import DetailsPage
import page

class HomePageSearch(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("/Users/mmt6198/Downloads/chromedriver")
        self.driver.get("https://homestays.makemytrip.com")



    def test_askTheHost(self):
        driver = self.driver
        driver.implicitly_wait(5)
        homepage = HomePage(driver)

        home_page = page.HomePage(driver)
        home_page.clickPopularCityFromAutosuggest()

        #get the search edit box
        #homepage.searchBoxEnterText().send_keys('raichur')
        #self.assertIn("RightStay by MakeMyTrip - Book Right Place to Stay for your Trip",driver.title)
        time.sleep(1)

        #click On Search
        home_page.clickSearchButton()
        time.sleep(3)

        listing_page = page.ListingPage(driver)
        listing_page.clickPropertyCrad()

        time.sleep(2)
        driver.switch_to.window(self.driver.window_handles[1])
        print driver.title

        details_page = page.DetailsPage(driver)

        details_page.clickButton('ask Host')
        details_page.enterText('name')
        details_page.enterText('email')
        details_page.enterText('phone')
        details_page.enterText('message')
        details_page.clickButton('send Message')

        time.sleep(4)
        details_page.clickButton('continue Browsing')

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
        unittest.main()

