from api.register import user_register
import pytest
import random
import allure


@allure.feature("测试注册接口")
@pytest.mark.smoke  # 标记
class TestRegistr(object):

    @allure.title("注册成功的接口")
    def test_register_success(self, base_url):
        """未注册的账号和密码，注册成功"""
        user = "test_" + "".join(random.sample('abcddfsf123544', 5))
        r1 = user_register(base_url, user, "123456")
        print(r1.json())
        assert r1.json()['code'] == 0
        assert r1.json()['msg'] == 'register success!'

    @allure.title("注册失败的接口")
    def test_register_failures_1(self, base_url):
        """已注册的账号和密码，注册失败"""
        r2 = user_register(base_url, "testcva", "123456")
        print(r2.json())
        assert r2.json()['code'] == 2000
        assert '用户已被注册' in r2.json()['msg']

    @allure.title("注册失败的接口")
    def test_register_failures_2(self, base_url):
        """空账号和密码，注册失败"""
        r2 = user_register(base_url, "", "")
        assert r2.json()['code'] == 3003
        assert r2.json()['msg'] == '参数不合法'
