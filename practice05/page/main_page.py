from selenium.webdriver.common.by import By
from practice05.page.base_page import BasePage
from practice05.page.contact_page import ContactPage


class MainPage(BasePage):
    _location_add_member = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")
    _location_import_members = (By.CSS_SELECTOR, ".ww_indexImg_Import")

    def goto_contact(self):
        """            企业微信web首页跳转到通讯录页面         """
        self.find(by=By.ID, value="menu_contacts").click()
        return ContactPage(self.driver)

    def goto_add_member(self):
        """        企业微信web首页跳转到添加成员页面        """
        from practice05.page.add_member_page import AddMemberPage

        # self.driver.find_element(*self._location_add_member).click()
        self.find(self._location_add_member).click()
        return AddMemberPage(self.driver)

    def goto_import_members(self):
        """        企业微信web首页跳转到导入通讯录页面        """
        from practice05.page.import_members_page import ImportMembersPage

        self.find(self._location_import_members).click()
        return ImportMembersPage(self.driver)

    def back_main(self):
        self.find(By.ID, "menu_index").click()
        self.find(By.CSS_SELECTOR, 'a[node-type="cancel"]').click()