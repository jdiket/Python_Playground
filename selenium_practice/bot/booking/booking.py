from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import booking.constants as const

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=webdriver.Chrome(ChromeDriverManager().install())):
        self.driver_path = driver_path
        super(Booking, self).__init__()

    def land_first_page(self):
        self.get(const.BASE_URL)