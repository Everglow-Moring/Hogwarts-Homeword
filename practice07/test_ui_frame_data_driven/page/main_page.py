from practice07.test_ui_frame_data_driven.page.base_page import BasePage
from practice07.test_ui_frame_data_driven.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        # 从yaml文件获取数据 在base page进行封装
        self.load("../page/main.yaml")
        return MarketPage(self.driver)
