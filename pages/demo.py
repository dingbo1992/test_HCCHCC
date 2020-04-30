
from appium.webdriver.common.mobileby import MobileBy
import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class Comliaint(BaseAction):

    complaint_btn_id = By.ID, 'com.bailun.huichacha:id/rl_bottom_menu_customer'  # 首页-客诉
    complaint_id = By.ID, 'com.bailun.huichacha:id/iv_right'  # 右上角去投诉
    complaint_exposure_id = By.ID, 'com.bailun.huichacha:id/ll_add_exposure'  # 我要曝光
    # complaint_exposure_id = 'new UiSelector().text("我要曝光")'  # 我要曝光
    complaint_consult_id = By.ID, 'com.bailun.huichacha:id/ll_add_consultation'  # 我要咨询
    complaint_complain_id = By.ID, 'com.bailun.huichacha:id/ll_add_complaint'#我要投诉

    complaint_select_id = By.ID, 'com.bailun.huichacha:id/tv_select'  # 我要曝光-选择曝光的平台
    complaint_select_platform_xpath = By.XPATH, '//*[contains(@text, "AAATrade")]'
    complaint_inputtitle_id = By.ID, 'com.bailun.huichacha:id/submit_item_et_info'  # 我要曝光-输入标题
    complaint_inpputcontent_id = By.ID, 'com.bailun.huichacha:id/fxsact_et_submit_content'  # 我要曝光-输入内容
    complaint_addphont_id = By.ID, 'com.bailun.huichacha:id/iv_add'  # 我要曝光-添加图片
    complaint_inputname_id = By.ID, 'complaint_addphont_id'  # 我要曝光-名字
    complaint_select_class = By.ID, 'android.widget.TextView'   # 选择平台
    complaint_selectphoto_class = By.ID, 'com.bailun.huichacha:id/tv_select_order'  # 选择图片的id
    complaint_finish_id = By.ID, 'com.bailun.huichacha:id/tv_complete'  # 选择图片-完成

    input_name_xpath = By.XPATH, '//*[contains(@text,"填写您的名字")]'  # 输入姓名
    input_mb_xpath = By.XPATH, '//*[contains(@text,"您的手机号码")]'  # 输入手机号
    input_email_xpath = By.XPATH, '//*[contains(@text,"您的邮箱")]'  # 输入邮箱

    always_allow_xpath = 'new UiSelector().text("始终允许")'
    finish_xpath = 'new UiSelector().text("完成")'

    #  search_xpath = 'new UiSelector().text("搜索")'
    def click_complaint(self):
        # name = '点击首页的客诉'
        self.click(self.complaint_btn_id)
        time.sleep(5)

    def click_right_corner(self):
        self.click_complaint()
        # 点右上角
        # name = '右上角'
        self.click(self.complaint_id)
        return self

    def click_exposure(self):
        # name = '点击我要曝光'
        self.click_right_corner()
        time.sleep(2)
        self.click(self.complaint_exposure_id)
        return self

    def select_platform(self):
        # name = '选择平台'
        time.sleep(1)
        self.click(self.complaint_select_id)
        time.sleep(2)
        self.click(self.complaint_select_platform_xpath)
        return self

    def add_photo(self):
        name = '添加图片'
        time.sleep(1)
        self.swipe_phone_list(1)
        time.sleep(1)
        self.click(self.complaint_addphont_id)

        if self.get_page_source().find("始终允许") > 0:
            self.click(self.always_allow_xpath)
        time.sleep(1)
        # 选择第一张图片
        self.click(self.complaint_selectphoto_class)
        time.sleep(1)
        self.click_element(self.complaint_finish_id,model=name)
        time.sleep(1)
        return self
    def input_all_content(self,title,content,name2,moblie,email):
        #进入到我要曝光页面
        self.click_exposure()
        name = '输入我曝光的所有信息'
        #1.选择一个平台
        self.select_platform()
        #2.输入title
        self.wait_eleVisible(self.complaint_inputtitle_id,model=name)
        self.input_text(title,self.complaint_inputtitle_id,model=name)
        #3.输入内容
        time.sleep(1)
        self.wait_eleVisible(self.complaint_inpputcontent_id, model=name)
        self.input_text(content, self.complaint_inpputcontent_id, model=name)
        #4.选择照片 默认第一张
        self.add_photo()
        #5.输入名字
        self.wait_eleVisible(self.input_name_xpath,by=MobileBy.XPATH,model=name)
        self.input_text(name2,self.input_name_xpath,by=MobileBy.XPATH,model=name)
        #6.输入手机号
        self.wait_eleVisible(self.input_mb_xpath,by=MobileBy.XPATH,model=name)
        self.input_text(moblie,self.input_mb_xpath,by=MobileBy.XPATH,model=name)
        #7.输入邮箱
        self.wait_eleVisible(self.input_email_xpath,by=MobileBy.XPATH,model=name)
        self.input_text(email,self.input_email_xpath,by=MobileBy.XPATH,model=name)




if __name__ == '__main__':
    a = make_driver()
    b = Comliaint(a)
    # b.click_exposure().select_platform().add_photo()
    b.input_all_content('标题','内容','姓名','13277935978','583737406@qq.com')
