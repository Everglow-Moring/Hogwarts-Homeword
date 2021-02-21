from selenium.webdriver.common.by import By
from practice06.test_ui_frame.page.base_page import BasePage
from practice06.test_ui_frame.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]')
        self.find_and_click(By.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]')
        return MarketPage(self.driver)
