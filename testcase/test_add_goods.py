import pytest
import time
import allure
from api.goods import add_goods


# 标记  通过执行python -m smoke 只执行@pytest.mark.smoke的用例
@pytest.mark.smoke
@allure.feature("测试添加商品接口")
class TestAddGoods(object):
    @allure.title("添加成功的用例")
    def test_add_goods_success(self, login_fixtrue, base_url):
        """输入正确的商品名称和商品code，添加成功"""
        goodscode = "sp_" + str(int(time.time()))
        r = add_goods(s=login_fixtrue,
                      base_url=base_url,
                      goodsname="《selenium 入门到精通12》",
                      goodscode=goodscode,
                      merchantid=12
                      )
        time.sleep(1.2)
        assert r.json()['code'] == 0
        assert r.json()['msg'] == 'success!'

    @allure.story("参数化登录")
    @pytest.mark.parametrize('goodsname, expect, title',
                             [
                                 ["", {"code": 3003, "msg": "参数不合法"}, '输入空商品名，添加失败'],
                                 ["中文", {"code": 0, "msg": "success!"}, '输入中文商品名，添加成功'],
                                 ["@#$", {"code": 0, "msg": "success!"}, '输入特殊符号商品名，添加成功'],
                                 ["11111111111111111111111111111111", {"code": 3003, "msg": "参数不合法"}, '商品名称超过30个字符，添加失败'],
                             ])
    def test_add_goods_fial(self, login_fixtrue, base_url, goodsname, expect, title):
        """添加失败的用例"""
        allure.dynamic.title(title)  # 动态读取title
        goodscode = "sp_" + str(int(time.time()))
        time.sleep(2)
        r = add_goods(s=login_fixtrue,
                      base_url=base_url,
                      goodsname=goodsname,
                      goodscode=goodscode,
                      merchantid=12
                      )
        print(r.json())
        assert r.json()['code'] == expect['code']
        assert r.json()['msg'] == expect['msg']
