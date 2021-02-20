from appium.webdriver.common.mobileby import MobileBy
from practice04.page.address_list_page import AdressListPage
from practice04.page.base_page import BasePage


class MainPage(BasePage):
    """
    首页PO
    """

    def goto_contact(self):
        """
        企业微信首页进入 通讯录 “address_list_page"
        :return:
        """
        print("点击通讯录")
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/dqn" and @text="通讯录"]')

        return AdressListPage(self.driver)
