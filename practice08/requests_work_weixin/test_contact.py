import requests


def get_token():
    r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww27109c7ff003e40c&corpsecret"
                     "=GdQqf6MCOIEoth3nFipa0P7i7x-KJI5DeUMdFTtlK6E")

    token = r.json()["access_token"]
    return token


def test_get_member():
    get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=0220-11"
    r = requests.get(get_member_url)
    print(r.json())
    assert "0220-11" == r.json()["name"]


def test_update_member():
    update_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}"
    data = {
        "userid": "0220-11",
        "mobile": "15702200001",
        "name": "0220-11"
    }
    r = requests.post(url=update_member_url, json=data)
    print(r.json())


def test_create_member():
    create_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}"
    data = {
        "userid": "20210324-2",
        "name": "张三-2",
        "mobile": "+86 13800002222",
        "department": [1]
    }
    r = requests.post(url=create_member_url, json=data)
    print(r.json())


def test_delete_member():
    delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=20210324-2"
    r = requests.get(url=delete_member_url)
    print(r.json())
