import pytest

from practice09.test_requests_po_session.base_page.contact import Contact


class TestContact:
    def setup_class(self):
        self.contact = Contact()
        self.userid = "20210327-1"
        self.name = "你好20210327-1"
        self.mobile = "1895703270001"

    @pytest.mark.parametrize("corpid, corpsecret, result",
                             [(None, None, 0), ("xxx", None, 40013), (None, "xxx", 40001)])
    def test_token(self, corpid, corpsecret, result):
        r = self.contact.get_token(corpid, corpsecret)
        print(r)
        assert result == r.get("errcode")

    def test_create_member(self):
        self.contact.create_member(userid=self.userid, name=self.name, mobile=self.mobile, department=[1],
                                   alias="0327-1的别名")
        try:
            find_result = self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(self.userid)
        assert find_result.get("errcode") == 0
        assert find_result["name"] == self.name

    def test_update_member(self):
        self.contact.create_member(userid=self.userid, name=self.name, mobile=self.mobile, department=[1],
                                   alias="0327-1的别名")
        self.contact.update_member(self.userid, self.name, "18903270002")
        try:
            find_result = self.contact.find_member(self.userid)
        finally:
            self.contact.delete_member(self.userid)
        assert find_result.get("errcode") == 0
        assert find_result["mobile"] == "18903270002"

    def test_delete_member(self):
        self.contact.create_member(userid=self.userid, name=self.name, mobile=self.mobile, department=[1],
                                   alias="find的别名")
        try:
            self.contact.find_member(self.userid)
        finally:
            r = self.contact.delete_member(self.userid)
        assert r.get("errcode") == 0

    def test_find_member(self):
        self.contact.create_member(userid=self.userid, name=self.name, mobile=self.mobile, department=[1],
                                   alias="find的别名")
        self.contact.find_member(self.userid)
        self.contact.delete_member(self.userid)

    @pytest.mark.parametrize("tmp", range(20))
    def test_defect_member(self, tmp):
        self.contact.find_member(self.userid)
