from appium import webdriver


def init_driver():
    desired_caps = {
        # "automationName": "UiAutomator2",
        "platformName": "Android",
        "platformVersion": "10",
        "deviceName": "1",
        "appPackage": "com.bailun.huichacha",
        "appActivity": 'com.bailun.huichacha.ui.splash.SplashActivity',
        "noReset": True,
        "unicodeKeyboard": True,
        # "resetKeyBoard": True,
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    print(driver.page_source)
    return driver


# print("-------------")
# init_driver()
