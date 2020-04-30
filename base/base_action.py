from time import sleep
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base import dir_config
from base.base_driver import init_driver
# from base import loger
import logging
import time


class BaseAction:
    meizu_id = 'com.meizu.flyme.input/com.meizu.input.MzInputService'  # 魅族输入法
    xiaomi_id = 'com.sohu.inputmethod.sogou/.SogouIME'  # 小米-搜狗输入法
    appium_id = 'io.appium.android.ime/.UnicodeIME'

    def __init__(self):
        self.driver = init_driver()

    def find_element(self, location, wait=10, frequency=1, model='model'):
        """基本定位元素
        x = lambda : True  =====》》
        def func(): return True
        so  :
        x = lambda : find_element(location[0], location[1])  =====>>
        def func(): return find_element(location[0], location[1])"""
        loc_way = location[0]  # By.ID/By.XPATH/By.CLASS
        loc_value = location[1]  # 定位值
        logging.info("开始查找元素：{0}={1}".format(loc_way, loc_value))
        try:
            if loc_way == By.XPATH:
                loc_value = self.make_xpath_with_feature(loc_value)  # 调用拼接方法，传参为实际的值
                # 如：loc = ["test,设,0", 'index,1,1', 'index,50']或loc = '//*[contains(@text, "设置")]'
            element = WebDriverWait(self.driver, wait, frequency).\
                until(lambda x: x.find_element(loc_way, loc_value))
            start = time.time()
            end = time.time()
            wait_times = end - start
            logging.info("等待元素可见：{0},起始时间：{1},等待时长：{2}S".format(location, start, wait_times))
        except:
            # 日志
            logging.exception("等待元素可见异常")
            # 截图
            self._save_screen_shot(model)
            raise

        return element

    def find_elements(self, location, wait=10, frequency=1):

        loc_way = location[0]
        loc_value = location[1]
        if loc_way == By.XPATH:
            loc_value = self.make_xpath_with_feature(loc_value)

        return WebDriverWait(self.driver, wait, frequency)\
            .until(lambda x: x.find_elements(loc_way, loc_value))

    def click(self, location, wait=10, frequency=1):
        """基本点击事件"""
        self.find_element(location, wait, frequency).click()

    def input_text(self, location, wait=10, frequency=1, text=11):
        """基本输入事件"""
        self.find_element(location, wait, frequency).send_keys(text)

    def swipe_phone_list(self, times, duration=1000):
        """上滑滑动列表
        :arg times ---->> 需要滑动的次数
        :arg duration ---->>每次的滑动速度"""
        phone_size = self.driver.get_window_size()
        start_x = phone_size['width'] * 0.5
        start_y = phone_size['width'] * 0.9
        end_x = phone_size['height'] * 0.5
        end_y = phone_size['height'] * 0.2
        for i in range(times):
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            sleep(2)
            i += 1

    def set_input_ways(self, input_way):
        self.driver.is_ime_active()
        self.driver.activate_ime_engine(input_way)

    def select_from_elements(self, location, num=1, index=-1):
        """
        :param location: 定位的列表元素
        :param num: 选择列表中的元素个数
        :param index: 选择列表中元素的索引
        :return:
        """
        elements = self.find_elements(location)
        if elements is not None:
            albums = random.sample(elements, num)
            if num == 1:
                if index == -1 or index < 0:
                    location = random.randint(0, len(elements) - 1)
                    return elements[location]
                else:
                    return elements[index]
            if num > 1:
                sel_elements = []
                for album in albums:
                    sel_elements.append(album)
                return sel_elements

    def _save_screen_shot(self, model_name="model"):
        # 根据功能和时间点生成截图
        # 文件格式 ：功能名称_年月日-时分秒.png
        file_path = dir_config.screenshot_dir + "/{0}_{1}.png".format(model_name, time.strftime("%Y-%m-%d-%H-%M-%S",
                                                                                                time.localtime()))
        # 截图文件存放在 Screenshot目录下
        # driver方法：self.driver.save_screenshot()
        self.driver.save_screenshot(file_path)
        logging.info("截图成功,路径为：{0}".format(file_path))

    def make_xpath_with_unit_feature(self, location):

        args = location.split(',')
        key_index = 0
        value_index = 1
        option_index = 2
        feature = ''
        if len(args) == 2:
            feature = 'contains(@' + args[key_index] + ", '" + args[value_index] + "')" + ' and '
        elif len(args) == 3:
            if args[option_index] == '1':
                feature = '@' + args[key_index] + " = '" + args[value_index] + "'" + ' and '
            elif args[option_index] == '0':
                feature = 'contains(@' + args[key_index] + ", '" + args[value_index] + "')" + ' and '
        return feature

    def make_xpath_with_feature(self, location):
        feature_start = '//*['
        feature_end = ']'
        feature = ''
        print(feature)
        if isinstance(location, str):
            if location.startswith('//'):
                return location
        else:
            for i in location:
                feature += self.make_xpath_with_unit_feature(i)
        feature = feature.rstrip(' and ')
        location = feature_start + feature + feature_end
        # print(location[1])
        return location

