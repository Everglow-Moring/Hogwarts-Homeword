from practice07.test_ui_frame_data_driven.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        self.load("../../test_ui_frame_data_driven/page/search.yaml")
        return True
