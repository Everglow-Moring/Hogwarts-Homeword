from time import sleep
import yaml
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from basecode.base import Base


class TestAddMember(Base):
    def test_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("cookie.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]').click()
        self.driver.find_element(By.XPATH, '//*[@class="ww_operationBar"]')
        self.driver.find_element(By.XPATH, '//*[@class="ww_operationBar"]/a').click()
        sleep(1)
        ast = self.driver.find_element(By.XPATH, '//*[@class="qui_btn ww_btn ww_btn_Blue js_btn_continue"]').text
        assert (ast == "保存并继续添加")
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("test04")
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_english_name"]').send_keys("测试人员04")
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys("test034")
        self.driver.execute_script('a = document.getElementsByName("gender"),a[0].removeAttribute("checked"),a[1].setAttribute("checked","checked")')
        # print(self.driver.find_element(By.XPATH, '//*[@class="ww_radio"]').get_attribute("value"))
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys("13800000004")

        action = TouchActions(self.driver)
        action.scroll(0, 1000).perform()

        self.driver.find_element(By.XPATH, '//*[@class="qui_btn ww_btn ww_btn_Blue js_btn_continue"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="username"]').text
        # 新增成功后，查看页面的输入框是否清空了
        assert (self.driver.find_element(By.XPATH, '//*[@id="username"]').text == "")
        sleep(3)





