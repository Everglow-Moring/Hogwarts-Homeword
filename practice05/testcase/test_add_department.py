import pytest
from practice05.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    # @pytest.mark.parametrize("department_name, expect_res", [("0221部门-06", "新建部门成功")])
    @pytest.mark.parametrize("department_name", ["0221部门-23"])
    def test_add_department(self, department_name):
        """
        添加部门的测试用例：
        1、跳转至添加部门页面
        2、填写部门名称
        3、断言：添加部门成功后窗口部门节点中是否有该部门
        """
        res = self.main.goto_contact().contact_goto_add_department().add_department(department_name).get_department_member_list()
        # res = self.main.goto_contact().contact_goto_add_department().add_department(department_name)
        assert department_name in res[-1]

    @pytest.mark.parametrize("department_name, expect_res", [("0221部门-01", "该部门已存在")])
    def test_add_department_fail(self, department_name, expect_res):
        """
        添加部门失败的测试用例
        :param department_name:部门名称
        """
        res = self.main.goto_contact().contact_goto_add_department().add_department_fail(department_name)
        assert expect_res in res

    def teardown(self):
        self.main.quit()
