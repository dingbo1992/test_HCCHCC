import os


#项目顶层目录


base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

logs_dir = os.path.join(base_dir,"Logs")

caps_dir = os.path.join(base_dir,"caps_config")

htmlreports_dir = os.path.join(base_dir,"HtmlReports")

testcaces_dir = os.path.join(base_dir,"TestCases")

testdates_dir = os.path.join(base_dir,"TestDates")

screenshot_dir = os.path.join(base_dir,"ScreenShot")

# print(testcaces_dir)