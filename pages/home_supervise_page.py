from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomeSupervise(BaseAction):

    supervise_id = By.ID, 'com.bailun.huichacha:id/tv_title'  # 首页-监管机构
    supervise_list_id = By.ID, 'com.bailun.huichacha:id/rl_item'  # 监管列表

    def supervise_in(self):

        self.select_from_elements(self.supervise_id, index=0).click()

    def supervise_list_in(self, index):
        self.supervise_in()


if __name__ == '__main__':

    HomeSupervise().supervise_in()
