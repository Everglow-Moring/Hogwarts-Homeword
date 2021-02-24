import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# 黑名单装饰器
from practice07.test_ui_frame_data_driven.page.black_handle import black_wrapper


class BasePage:
    """
    通用操作：操作driver相关的方法
    """
    FIND = "find"
    ACTION = "action"
    FIND_AND_CLICK = "find_and_click"
    SEND = "send"
    CONTENT = "content"

    # 添加driver的注解，声明driver的类型，以方便引出driver的方法和属性
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        # 参考：可封装一个黑名单类 : by， locator
        self.black_list = [(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/iv_close"]')]

    # 黑名单装饰器，加强
    @black_wrapper
    # 装饰器会把self, by, locator这三个参数一起传值，只需要在black_wrapper定义中使用
    def find(self, by, locator):
        # 获取截图
        self.driver.save_screenshot("tmp.png")
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        return self.find(by, locator).click()

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def send(self, by, locator, content):
        return self.find(by, locator).send_keys(content)

    def scroll_find(self, text):
        return self.driver.find_element(MobileBy.
                                        ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                             'scrollable(true).instance(0)).'
                                                             'scrollIntoView(new UiSelector().'
                                                             f'text("{text}").instance(0));')

    def scroll_find_and_click(self, text):
        return self.scroll_find(text).click()

    def find_and_send_keys(self, by, locator, text):
        return self.find(by, locator).send_keys(text)

    def wait_for(self, by, locator):
        def wait_ele_for(driver: WebDriver):
            elements = driver.find_elements(by, locator)
            return len(elements) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_for)

    # 使用selenium的appium的滚动方式 因为scroll_find这个方法不好记
    def swip_find(self, by, locator):
        # 每次查找元素都会触发隐式等待，10s的话滑动的得特别慢
        # 在滑动查找时将隐式等待时间改短一点，找到元素后再复原等待时间
        self.driver.implicitly_wait(1)
        # 找到满足条件的所有元素
        elements = self.driver.find_elements(by, locator)
        # 不停的滑动，直到找到满足条件的元素为止
        while len(elements) == 0:
            # 滑动
            self.driver.swipe(0, 600, 0, 400)
            elements = self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)
        return elements[0]

    def swip_find_and_click(self, by, locator):
        return self.swip_find(by, locator).click()

    # todo: base page 已经无限膨胀了
    def load(self, yaml_path):
        with open(yaml_path, "r", encoding="utf-8") as f:
            # data_yaml 是 字典dict
            data_yaml = yaml.load(f)
            # step 的结构：find, action
            for step in data_yaml:
                # todo: 关键字可变问题
                xpath_expression = step.get(self.FIND)
                action = step.get(self.ACTION)
                # todo: 函数调用
                if action == self.FIND_AND_CLICK:
                    self.find_and_click(By.XPATH, xpath_expression)
                elif action == self.SEND:
                    content = step.get(self.CONTENT)
                    self.send(By.XPATH, xpath_expression, content)

    def screen_shot(self, picture_path):
        self.driver.save_screenshot(picture_path)
