from selenium.webdriver.common.by import By
from practice05.page.base_page import BasePage
from practice05.page.department_member_list import DepartmentMemberList


class AddDepartment(BasePage):
    _locator_department_name = (By.CSS_SELECTOR, ".member_tag_dialog_inputDlg .ww_inputText")

    def add_department(self, department_name):
        self.find(*self._locator_department_name).send_keys(department_name)
        self.find_and_click(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]')

        return DepartmentMemberList(self.driver)

    def add_department_fail(self, department_name):
        self.find(self._locator_department_name).send_keys(department_name)
        self.find_and_click(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]')
        res = self.finds(By.ID, "js_tips")
        error_list = [i.text for i in res]
        return error_list



