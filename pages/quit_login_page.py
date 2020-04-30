from selenium.webdriver.common.by import By
from time import sleep
from base.base_action import BaseAction


class LoginQuit(BaseAction):

    mine_id = By.ID, 'com.bailun.huichacha:id/rl_bottom_menu_my_page'  # 主页“我的”
    # mine_xpath = "//*[contains(@text, '我的')]"
    mine_set_id = By.ID, 'com.bailun.huichacha:id/cl_my_setting'  # 我的-设置
    mine_set_quit_xpath = By.XPATH, '//*[contains(@text, "退出登录")]'  # 我的-设置-退出登录
    mine_set_quit_sure_id = By.ID, 'com.bailun.huichacha:id/tv_positive'
    mine_set_quit_sure_xpath = By.XPATH, "//*[contains(@text, '确定')]"  # 我的-设置-退出-弹框确认
    mine_set_quit_dismiss_id = By.ID, 'com.bailun.huichacha:id/tv_negative'  # 取消退出
    mine_set_quit_dismiss_xpath = By.ID, "//*[contains(@text, '取消')]"
    mine_no_login_id = By.ID, 'com.bailun.huichacha:id/tv_tips'
    mine_no_login_xpath = By.XPATH, '//*[contains(@text, "“登录汇查查，体验更多功能”")]'

    def quit_login(self):

        self.click(self.mine_id)
        self.driver.swipe(484, 1485, 484, 800)
        self.click(self.mine_set_id)
        self.click(self.mine_set_quit_xpath)
        sleep(3)
        self.click(self.mine_set_quit_sure_id)
        # text = self.driver.find_element_by_xpath(self.mine_no_login_xpath).text
        # self.assertEqual(text, "“登录汇查查，体验更多功能”")


if __name__ == '__main__':

    a = LoginQuit()
    a.quit_login()
