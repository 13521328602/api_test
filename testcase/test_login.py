import requests
import pytest
import allure
from api.login_api import login


@allure.feature("登录的接口")
@pytest.mark.smoke
class TestLogin(object):

    @allure.title("登录成功得用例")
    def test_login_success(self, base_url):
        """登陆成功的用例"""
        s = requests.Session()
        r = login(s, base_url, "test1", "123456")
        assert r.json()['code'] == 0
        assert r.json()['msg'] == 'login success!'
        assert len(r.json()['token']) == 40

    @allure.story("登录参数化")
    @pytest.mark.parametrize('user, powd, title',
                             [
                                 ["test888", "123456", "未注册的用户，登录失败"],
                                 ["testxx123zxz", "123456", "未注册用户，登陆失败"],
                                 ["", "", "空的账号和密码，登录失败"],
                                 ["test10", "", "空的密码，登陆失败"],
                             ]
                             )
    def test_login_fail(self, base_url, user, powd, title):
        """登陆失败的用例"""
        allure.dynamic.title(title)
        s = requests.Session()
        r = login(s, base_url=base_url, user=user, pwd=powd)
        print(r.json())
        assert r.json()['code'] == 3003
        assert r.json()['msg'] == '账号或密码不正确'
        assert len(r.json()['token']) == 0
