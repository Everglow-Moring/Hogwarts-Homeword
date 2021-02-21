from appium import webdriver
from practice06.test_ui_frame.page.base_page import BasePage
from practice06.test_ui_frame.page.main_page import MainPage


class App(BasePage):
    """
    启动操作：初始化driver
    """

    # 为什么不用setup？
    # setup是pytest的，用于写测试用例的 def test_*（），避免混淆，所以在PO中需要用类的方式，
    def start(self):
        # 避免每次运行都初始化
        if self.driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['udid'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.xueqiu.android'
            desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
            desired_caps['noReset'] = 'True'
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            # 隐式等待
        else:
            # 如果有初始化，就复用以上的设置，启动App即可
            self.driver.launch_app()

        self.driver.implicitly_wait(5)

    def goto_main(self):
        # 只有driver才能点击，如果不传给MainPage，就无法操作
        return MainPage(self.driver)