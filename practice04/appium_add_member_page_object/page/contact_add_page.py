from appium.webdriver.common.mobileby import MobileBy
from practice04.appium_add_member_page_object.page import BasePage


class ContactAdd(BasePage):
    """
    成员信息填写页面PO
    """

    def add_contact(self):
        """
        添加信息
        :return:
        """
        self.find_and_send_keys(MobileBy.XPATH, '//*[contains(@text, "姓名")]/..//*[@text="必填"]', "0220-11")
        self.find_and_click(MobileBy.XPATH, '//*[contains(@text, "性别")]/..//*[@text="男"]')
        self.wait_for(MobileBy.XPATH, '//*[@text="女"]')
        self.find_and_click(MobileBy.XPATH, '//*[@text="女"]')
        self.find_and_send_keys(MobileBy.XPATH, '//*[contains(@text, "手机")]/..//*[@text="手机号"]', "15702200001")
        self.find_and_click(MobileBy.XPATH, '//*[@text="保存"]')
        print("姓名、性别、手机号信息填写")
        return True
