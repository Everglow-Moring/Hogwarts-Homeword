from selenium.webdriver.common.by import By
from practice05.page.base_page import BasePage


class DepartmentMemberList(BasePage):
    _location_get_department_member_list = (By.CSS_SELECTOR, ".jstree-default")

    def get_department_member_list(self):
        department_list = self.finds(*self._location_get_department_member_list)
        # print(department_member_list)
        department_name_list = []
        for i in department_list:
            # print(i.text)
            department_name_list.append(i.text)
        # department_name_list = [i.text for i in department_member_list]
        return department_name_list
