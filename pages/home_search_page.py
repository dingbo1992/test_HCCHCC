from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomeSearch(BaseAction):

    home_search_id = By.ID, 'com.bailun.huichacha:id/tv_search'  # 首页-搜索
    search_box_id = By.ID, 'com.bailun.huichacha:id/et_search'  # 搜索框
    search_text_xpath = By.XPATH, '//*[contains(@text, "富拓")]'  # 搜索历史记录
    delete_id = By.XPATH, 'com.bailun.huichacha:id/iv_delete'  # 删除历史记录按钮
    result_keyword_text = By.ID, 'com.bailun.huichacha:id/tv_dealer'
    result_site_text = By.ID, 'com.bailun.huichacha:id/tv_dealer'

    para = ['外汇', '富拓', 'https://www.invest.com', '600475']

    def search_in(self):
        self.click(self.home_search_id)
        self.click(self.search_box_id)

    def search_enter(self):
        self.set_input_ways(self.xiaomi_id)
        self.click(self.search_box_id)
        self.driver.press_keycode(66)

    def search_by_keyword(self):
        self.search_in()
        text = 'FXTM富拓'
        self.input_text(self.search_box_id, text=text)
        self.search_enter()
        expect_message = 'FXTM富拓'
        message = self.select_from_elements(self.result_keyword_text, 1, index=0).text
        print(message)
        if message == expect_message:
            return '搜索成功'
        else:
            return '搜索失败'

    # 通过网址搜索
    def search_by_site(self):
        self.search_in()
        text = 'https://www.invest.com'
        self.input_text(self.search_box_id, text=text)
        self.search_enter()
        message = self.select_from_elements(self.result_site_text, index=0).text
        expect_message = 'Invest.com'
        print(message)
        if message == expect_message:
            return '搜索成功'
        else:
            return '搜索失败'

    # 通过监管号搜索
    def search_by_supervise(self):
        self.search_in()
        text = '600475'
        self.input_text(self.search_box_id, text=text)
        self.search_enter()
        expect_message = 'FXTM富拓'
        message = self.select_from_elements(self.result_keyword_text, 1, index=0).text
        print(message)
        if message == expect_message:
            return '搜索成功'
        else:
            return '搜索失败'


if __name__ == '__main__':
    home_search = HomeSearch()
    home_search.search_by_supervise()


