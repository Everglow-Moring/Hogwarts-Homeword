import requests
from requests import Session


class Base:
    def __init__(self):
        self.session = Session()
        self.corpid = "ww27109c7ff003e40c"
        self.corpsecret = "GdQqf6MCOIEoth3nFipa0P7i7x-KJI5DeUMdFTtlK6E"
        self.session.params["access_token"] = self.get_token().get("access_token")

    def get_token(self, corpid=None, corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret

        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        return r.json()
