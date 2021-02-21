from time import sleep
from selenium.webdriver.common.by import By
from practice05.page.base_page import BasePage
from practice05.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    # _location_username ：在变量前加 下划线 _ ，是让变量私有化即只能在该类中使用
    _location_username = (By.ID, "username")
    _location_account_id = (By.ID, "memberAdd_acctid")
    _location_phone = (By.ID, "memberAdd_phone")

    def add_member(self):
        """        添加成员操作        """

        # 不要暴露页面内部的元素给外部
        # _location_username的类型是元组，find_element需要2个参数
        # 在前面加*即可，*self._location_username   解元组：把元组内的元素拆分为不用的参数传入
        self.driver.find_element(*self._location_username).send_keys("测试0204-5")
        self.driver.find_element(*self._location_account_id).send_keys("testid-5")
        self.driver.find_element(*self._location_phone).send_keys("12100050204")

        # 滑动屏幕
        self.driver.execute_script("document.documentElement.scrollTop=1000")

        # ".s_btn_save"这里的 . 代表的是css-class中的内容
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()

        return ContactPage(self.driver)

    def add_member_fail(self, acctid, phone):
        # self.driver.find_element(*self._location_username).send_keys("测试0131-8")
        # self.driver.find_element(*self._location_account_id).send_keys("testid-8")
        # self.driver.find_element(*self._location_phone).send_keys("13101310008")
        # 优化
        self.find(self._location_username).send_keys("测试0204-5")
        self.find(self._location_account_id).send_keys(acctid)
        self.find(self._location_phone).send_keys(phone)

        self.driver.execute_script("document.documentElement.scrollTop=1000")
        # self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        # 优化
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        sleep(1)  # 等待过度，不然断言的时候报错，因为操作太快，或获取到error_massage

        # id_message = self.driver.find_element(By.CSS_SELECTOR, ".member_edit_item_right.ww_inputWithTips_WithErr "
        #                                                        ".ww_inputWithTips_tips").text
        # phone_message = self.driver.find_element(By.CSS_SELECTOR, ".member_edit_item_right.ww_inputWithTips_WithErr "
        #                                                           ".ww_inputWithTips_tips").text
        # error_message 优化
        res = self.finds(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        print(res)
        error_list = [i.text for i in res]
        print(error_list)
        return error_list
