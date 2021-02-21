from selenium.webdriver.common.by import By
from practice05.page.base_page import BasePage


class ContactPage(BasePage):
    _location_get_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_contact_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _location_contact_goto_add_department = (By.CSS_SELECTOR, ".js_add_sub_party")

    def contact_goto_add_member(self):
        """        添加成员页面-填写信息        """
        from practice05.page.add_member_page import AddMemberPage

        # 添加显示等待,保证按钮可点击,element_to_be_clickable()的参数是元组 WebDriverWait(self.driver, 10).until(
        # expected_conditions.element_to_be_clickable(self._location_contact_goto_add_member)) 使用封装的显示等待方法
        self.wait_click_available(self._location_contact_goto_add_member)
        self.find(self._location_contact_goto_add_member).click()
        return AddMemberPage(self.driver)

    def get_member_list(self):
        """        获取成员列表，用来做断言        """
        # member_list 获取到的数据是WebElement对象而不是我们想要的结构化数据
        # member_list = self.driver.find_elements(*self._location_get_member_list)
        # 优化
        member_list = self.finds(*self._location_get_member_list)
        print(self.finds(*self._location_get_member_list))
        # 优化：列表推导式
        # member_name_list = [i.text for i in member_list]

        # 一般形式
        member_name_list = []
        for i in member_list:
            print(i.text)
            member_name_list.append(i.text)

        print(member_name_list)
        return member_name_list

    def contact_goto_add_department(self):
        from practice05.page.add_department_page import AddDepartment

        self.wait_click_available(self._location_contact_goto_add_department)
        self.find(self._location_contact_goto_add_department).click()
        return AddDepartment(self.driver)
