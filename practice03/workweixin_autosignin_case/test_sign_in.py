from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestAutoSignIn:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = 'True'
        # 设置页面等待空闲状态的时间
        desired_caps["setting[waitForIdleTimeout]"] = 0
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 隐式等待
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_auto_sign_in(self):
        self.driver.find_element(By.XPATH, '//*[@text="工作台"]').click()
        # 滚动查找元素
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("打卡")'
                                                        '.instance(0));').click()
        self.driver.find_element(By.ID, "com.tencent.wework:id/ghc").click()
        # self.driver.find_element(By.ID, "com.tencent.wework:id/alq").click()
        # 包含文本信息查找元素
        self.driver.find_element(By.XPATH, '//*[contains(@text,"次外出")]').click()
        # x = driver
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
        assert "外出打卡成功" in self.driver.page_source
