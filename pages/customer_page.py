from time import sleep
# from base.base_driver import init_driver
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class CustomerAction(BaseAction):

    customer_id = By.ID, "com.bailun.huichacha:id/rl_bottom_menu_customer"  # 客诉中心
    exposure_xpath = By.XPATH, "//*[contains(@text, '曝光')]"  # 曝光tab
    consult_xpath = By.XPATH, "//*[contains(@text, '咨询')]"  # 咨询tab
    complaint_xpath = By.XPATH, "//*[contains(@text, '投诉')]"  # 投诉tab
    search_id = By.ID, 'com.bailun.huichacha:id/iv_right_center'  # 搜索按钮
    search_box_id = By.ID, 'com.bailun.huichacha:id/et_search'  # 搜索框
    publish_id = By.ID, 'com.bailun.huichacha:id/iv_right'  # 发布按钮

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

    def search(self, keys=11):

        self.click(self.customer_id)  # 点击进入客诉
        sleep(3)
        self.click(self.exposure_xpath)  # 点击曝光
        sleep(3)
        self.click(self.complaint_xpath)  # 点击投诉
        sleep(3)
        self.click(self.search_id)  # 点击搜索
        # self.driver.activate_ime_engine('io.appium.android.ime/.UnicodeIME')
        # self.set_input_ways(self.appium_id)
        self.click(self.search_box_id)
        self.input_text(self.search_box_id, keys)
        sleep(5)
        # self.driver.activate_ime_engine('com.meizu.flyme.input/com.meizu.input.MzInputService')
        self.set_input_ways(self.xiaomi_id)
        self.click(self.search_box_id)
        sleep(2)
        self.driver.press_keycode(66)
        sleep(3)

    def swipe_exposure(self):
        self.click(self.customer_id)  # 点击进入客诉
        sleep(3)
        self.click(self.exposure_xpath)  # 点击曝光
        self.swipe_phone_list(10, 2000)


cs = CustomerAction()
cs.search()
