import yaml
from selenium import webdriver


# 复用浏览器
class TestGetCookie:
    def test_get_cookie(self):
        my_options = webdriver.ChromeOptions()
        my_options.debugger_address = "127.0.0.1:8080"
        self.driver = webdriver.Chrome(options=my_options)
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookie = self.driver.get_cookies()
        print(cookie)
        # 覆盖形式写入
        with open("cookie.yaml", "w", encoding="UTF-8") as f:
            # 把cookie写入yaml文件f：cookie.yaml
            yaml.dump(cookie, f)