from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# 黑名单装饰器
from practice06.test_ui_frame.page.black_handle import black_wrapper


class BasePage:
    """
    通用操作：操作driver相关的方法
    """

    # 添加driver的注解，声明driver的类型，以方便引出driver的方法和属性
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        # 参考：可封装一个黑名单类 : by， locator
        self.black_list = [(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/iv_close"]')]

    # 黑名单装饰器，加强
    @black_wrapper
    # 装饰器会把self, by, locator这三个参数一起传值，只需要在black_wrapper定义中使用
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # 递归
    # 设计模式：代理模式、装饰器模式
    # 这样写，find会越来越臃肿，庞大
    """
    def find(self, by, locator):
        try:
            return self.driver.find_element(by, locator)
        # 捕获元素未找到的异常
        except Exception as e:
            # 遍历黑名单中的元素，并进行处理：点击
            for black in self.black_list:
                # python 解包
                elements = self.finds(*black)
                # 如果在黑名单中找到元素，则对黑名单中的元素进行操作。然后继续查找元素
                if len(elements) > 0:
                    # 对黑名单元素进行点击，可以扩展
                    elements[0].click()
                    return self.find(by, locator)
            raise e
    """

    def find_and_click(self, by, locator):
        return self.find(by, locator).click()

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

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

