from typing import List

from practice09.test_requests_po_session.base_page.base import Base


class Contact(Base):
    def create_member(self, userid: str, name: str, mobile: str, department: List[int], **kwargs):
        create_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        data.update(kwargs)
        r = self.session.post(url=create_member_url, json=data)
        return r.json()

    def update_member(self, userid: str, name: str, mobile: str, **kwargs):
        update_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": userid,
            "mobile": mobile,
            "name": name
        }
        data.update(kwargs)
        r = self.session.post(url=update_member_url, json=data)
        return r.json()

    def find_member(self, userid):
        params = {"userid": userid}
        get_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        r = self.session.get(get_member_url, params=params)
        return r.json()

    def delete_member(self, userid):
        params = {"userid": userid}
        get_member_url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        r = self.session.get(get_member_url, params=params)
        return r.json()
