from selenium.webdriver.common.by import By
from practice06.test_ui_frame.page.base_page import BasePage
from practice06.test_ui_frame.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]')
        return SearchPage(self.driver)
