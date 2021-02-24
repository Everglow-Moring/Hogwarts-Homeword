import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 将所有实例化放在base类里
    def __init__(self,base_driver=None):
        # 注解：不是赋值操作，无任何意义。用作id的类型提示
        base_driver: WebDriver
        # 避免driver多次实例化，在测试过程中打开多个页面
        if base_driver is None:
            # 复用浏览器，但此处不适用。因为添加成员失败，会一直停留在新增页面，无法参数化多次执行用例
            my_options = webdriver.ChromeOptions()
            my_options.debugger_address = "127.0.0.1:8080"
            # cmd 命令：chrome --remote-debugging-port=8080
            self.driver = webdriver.Chrome(options=my_options)
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            self.__cookie_login()
        else:
            self.driver = base_driver

        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # 封装方法: 将使用cookie登录
    def __cookie_login(self):
        with open("cookie.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    # 封装找元素的方法find   对用于不用的技术栈，可以方便快速的修改代码，仅需修改底层的方法，而不需要修改page与testcase
    def find(self, by, value=None):
        if value is None:
            # 传元组,就进行解包元组传参
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=value)

    def find_and_click(self, *by):
        return self.find(*by).click()

    def find_and_send_keys(self, *by, text):
        return self.find(*by).send_keys(text)

    def finds(self, by, value=None):
        if value is None:
            # 传元组
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by=by, value=value)

    def wait_click_available(self, locator):
        """        按钮显示等待封装        """
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        """        退出二次封装        """
        self.driver.quit()
