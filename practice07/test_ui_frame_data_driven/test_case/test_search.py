from practice07.test_ui_frame_data_driven.page.app import App


class TestSearch:
    def setup(self):
        self.app = App()
        self.app.start()

    def test_search(self):
        self.app.goto_main().goto_market().goto_search().search()
