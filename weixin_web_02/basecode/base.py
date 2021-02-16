import os
from selenium import webdriver


class Base:
    def setup(self):
        browser = os.getenv("browser")
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "headless":
            self.driver = webdriver.PhantomJS()
        else:
            option = webdriver.ChromeOptions()
            option.add_experimental_option("w3c", False)
            self.driver = webdriver.Chrome(options=option)

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()