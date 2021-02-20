from appium.webdriver.common.mobileby import MobileBy
from practice04.page.base_page import BasePage
from practice04.page.member_invite_menu_page import MemberInviteMenuPage


class AdressListPage(BasePage):
    """
    通讯录PO
    """

    def click_add_member(self):
        """
        :param self:
        :return:
        """
        print("点击添加成员")
        # self.scroll_find_and_click("添加成员")
        self.swip_find_and_click(MobileBy.XPATH, '//*[@text="添加成员"]')

        return MemberInviteMenuPage(self.driver)