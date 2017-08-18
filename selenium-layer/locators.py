from selenium.webdriver.common.by import By

class HomePageLocators(object):
    Search_editbox = (By.CLASS_NAME,'_2nOJuPvch8NVWZz5MwAZLD')
    AutoSuggest_SearchResults = (By.CLASS_NAME,'')
    AutoSuggest_PopularCities = (By.XPATH,'//*[@id="content"]/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div//button')
    Search_button = (By.CLASS_NAME,'_2t3YQsLhI2BWf222ZLLqFH')


class ListingPageLocators(object):
    Property_card = (By.CLASS_NAME,'_2fLrUNqRp_HSnpqqRjeoUp')


class DetailsPageLocators(object):
    Next_page_button = (By.CLASS_NAME,'_34T6us-YHgUxHnTsR2nPE6')
    Ask_the_host_button = (By.XPATH,"//button[@class='_2_fqhwTSVDeIV6EDPtLLwF ripplebutton btn btn-default']")
    Popup_send_message_button = (By.CLASS_NAME,"_1YDtDMwTsdZnQJ-Z114bLZ")
    Popup_continue_browsing_button = (By.CLASS_NAME,'errorModalButton')

    Popup_name_editbox = (By.NAME,'name')
    Popup_email_editbox = (By.NAME, 'email')
    Popup_phone_editbox = (By.NAME, 'phone')
    Popup_message_editbox = (By.NAME, 'message')

class BookingReviewPageLocators(object):

    Name_editbox = (By.NAME, '')
    Email_editbox = (By.NAME, '')
    Phone_editbox = (By.NAME, '')
    Message_editbox = (By.NAME, '')

    Submit_button = (By.CLASS_NAME,'')

class ThankyouPageLocators(object):

    text = (By.CLASS_NAME,'')


