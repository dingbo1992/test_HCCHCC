from time import sleep
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class HomeScan(BaseAction):

    scan_id = By.ID, 'com.bailun.huichacha:id/iv_scan_popup_window'  # 首页-扫一扫
    scan_take_id = By.ID, 'com.bailun.huichacha:id/iv_camera_scan_take_photo'  # 识别按钮
    scan_album_id = By.ID, 'com.bailun.huichacha:id/v_camera_scan_title_bar_album'  # 相册按钮
    scan_help_id = By.ID, 'com.bailun.huichacha:id/v_camera_scan_title_bar_help'  # 帮助按钮
    scan_cancel_id = By.ID, 'com.bailun.huichacha:id/v_camera_scan_title_bar_cancel'  # 取消按钮
    # 相册页面
    scan_picture_id = By.ID, 'com.bailun.huichacha:id/iv_album_picture'  # 相册图片id
    scan_camera_id = By.ID, 'com.bailun.huichacha:id/iv_animation_icon'  # 相机按钮
    picture_cancel_id = By.ID, 'com.bailun.huichacha:id/tv_cancel'  # 相册页面取消按钮
    picture_back_id = By.ID, 'com.bailun.huichacha:id/iv_back'  # 相册页面返回按钮
    picture_confirm_id = By.ID, 'com.bailun.huichacha:id/iv_ucrop_confirm'  # 确定选择按钮
    meizu_camera_take_id = By.ID, 'com.meizu.media.camera:id/shutter_button'  # 相机拍摄按钮
    meizu_camera_done_id = By.ID, 'com.meizu.media.camera:id/done_button'  # 照片完成按钮
    meizu_camera_confirm_id = By.ID, 'com.bailun.huichacha:id/iv_ucrop_confirm'  # 相机拍摄确按钮
    result_text = By.ID, 'com.bailun.huichacha:id/tv_custom_toolbar_title'

    def __init__(self):
        super().__init__()
        self.expect_message = '智能识别结果'

    # 进入扫一扫
    def scan(self):
        self.click(self.scan_id)

    def scan_by_camera(self):
        self.scan()
        self.click(self.scan_take_id)
        message = self.find_element(self.result_text).text
        if message == self.expect_message:
            return '扫描成功'
        else:
            return '扫描失败'  # 获取扫描结果

    # 进入相册页面
    def album_in(self):
        self.scan()
        self.click(self.scan_album_id)

    # 通过相册识别
    def scan_by_album(self):
        self.album_in()
        self.select_from_elements(self.scan_picture_id, 1).click()
        self.click(self.picture_confirm_id)
        message = self.find_element(self.result_text).text
        if message == self.expect_message:
            return '扫描成功'
        else:
            return '扫描失败'  # 获取扫描结果

    # 通过相机拍摄识别
    def scan_by_album_camera(self):
        self.album_in()
        sleep(1)
        self.click(self.scan_camera_id)  # 点击相册相机
        sleep(1)
        self.click(self.meizu_camera_take_id)  # 点击拍摄
        sleep(1)
        self.click(self.meizu_camera_done_id)  # 点击完成拍摄
        sleep(1)
        self.click(self.meizu_camera_confirm_id)  # 点击确认选择
        message = self.find_element(self.result_text).text
        print(message)
        if message == self.expect_message:
            return '扫描成功'
        else:
            return '扫描失败'  # 获取扫描结果


if __name__ == '__main__':

    home_scan = HomeScan()
    home_scan.scan_by_album_camera()



