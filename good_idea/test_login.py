import allure


class TestLogin:

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step(title="登录步骤")
    def test_login(self):
        allure.attach("输入用户名", "详细描述")
        print("hh")
        assert 1

    @allure.step(title="输入")
    def test_login2(self):
        print("oo")
        assert 1