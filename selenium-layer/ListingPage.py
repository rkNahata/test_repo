
class ListingPage:

    def __init__(self,driver):
        self.driver = driver

    def clickPropertyCard(self):
        button = self.driver.find_elements_by_class_name('_2fLrUNqRp_HSnpqqRjeoUp')
        return button[1]


