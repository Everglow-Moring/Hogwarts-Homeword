import pytest
from practice05.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        """        添加成员的测试用例        """
        # 1、跳转至添加成员页面  2、添加成员  3、断言：添加完成后会自动跳转至通讯录
        res = self.main.goto_add_member().add_member().get_member_list()
        assert "秦孔明" in res

    #
    @pytest.mark.parametrize("acctid, phone, expect_res",
                             [("testid-5", "12100090204", '该帐号已被“测试0204-5”占有'),
                             ("testid-7", "15721527996", '该手机号已被“秦孔明”占有')])
    # part1: 重复的acctid 正确的手机号  断言
    # part2: 正确的acctid  重复的手机号  断言
    def test_add_member_fail(self, acctid, phone, expect_res):
        """
        添加成员失败的测试用例
        :param acctid:账号
        :param phone:手机
        """
        res = self.main.goto_add_member().add_member_fail(acctid, phone)
        assert expect_res in res

    def test_add_member_by_contact(self):
        """        通过通讯录页面添加成员        """
        # 1、跳转至通讯录页面  2、跳转至添加成员页面  3、断言
        res = self.main.goto_contact().contact_goto_add_member().add_member()
        print(res)
        assert "秦孔明" in res

    def teardown(self):
        # 添加成员时使用，关闭浏览器
        # self.main.quit()
        # 当参数化测试添加成员失败时，不可关闭窗口
        self.main.back_main()


