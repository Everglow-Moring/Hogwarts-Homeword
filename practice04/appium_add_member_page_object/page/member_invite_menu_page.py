from appium.webdriver.common.mobileby import MobileBy
from practice04.appium_add_member_page_object.page import BasePage
from practice04.appium_add_member_page_object.page.contact_add_page import ContactAdd


class MemberInviteMenuPage(BasePage):
    """
    添加成员PO
    """

    def add_member_manual(self):
        """
        手动添加成员信息
        """
        print("点击手动添加成员信息")
        self.find_and_click(MobileBy.XPATH, '//*[@text="手动输入添加"]')

        return ContactAdd(self.driver)
