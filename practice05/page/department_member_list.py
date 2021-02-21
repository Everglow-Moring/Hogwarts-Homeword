from selenium.webdriver.common.by import By
from practice05.page.base_page import BasePage


class DepartmentMemberList(BasePage):
    _location_get_department_member_list = (By.CSS_SELECTOR, ".jstree-default")
    _location_department_members = (By.ID, "js_tips")

    def get_department_member_list(self):
        self.wait_click_available(self._location_department_members)
        department_list = self.finds(*self._location_get_department_member_list)
        department_name_list = []
        for i in department_list:
            department_name_list.append(i.text)
        department_name1 = [x.split("\n") for x in department_name_list]
        department_name = [aa.split() for aa in department_name1[0]]
        return department_name
