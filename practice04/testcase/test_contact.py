from practice04.page.app import App


class TestContact:
    # 首页 -> 通讯录 -> 滑动点击"添加成员" -> 手动添加 -> 信息填写
    def test_add_member(self):
        app = App()
        # start函数需要主动调用
        app.start()
        # 通过PO中的return返回的PO类实现
        result = app.goto_main().goto_contact().click_add_member().add_member_manual().add_contact()
        assert result
