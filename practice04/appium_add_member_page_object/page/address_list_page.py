from appium.webdriver.common.mobileby import MobileBy
from practice04.appium_add_member_page_object.page import BasePage
from practice04.appium_add_member_page_object.page.member_invite_menu_page import MemberInviteMenuPage


class AdressListPage(BasePage):
    """
    通讯录-PO
    """

    def click_add_member(self):
        """
        点击添加成员
        """
        print("点击添加成员")
        # self.scroll_find_and_click("添加成员")
        self.swip_find_and_click(MobileBy.XPATH, '//*[@text="添加成员"]')

        return MemberInviteMenuPage(self.driver)