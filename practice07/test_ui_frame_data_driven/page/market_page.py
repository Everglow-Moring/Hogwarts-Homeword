from practice07.test_ui_frame_data_driven.page.base_page import BasePage
from practice07.test_ui_frame_data_driven.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.load("../page/market.yaml")
        return SearchPage(self.driver)
