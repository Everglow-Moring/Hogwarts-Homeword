from selenium.webdriver.common.by import By
from practice06.test_ui_frame.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        self.find_and_send_keys(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', "alibaba")
        return True
