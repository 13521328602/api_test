"""
工作流：登录(前置操作)-添加商品-查询商品-修改商品-查询
"""
import time
import allure
import pytest
from api.goods import add_goods, update_goods


@pytest.mark.smoke
@allure.feature("商品添加修改查询流程")
class TestGoodWorkfolw(object):

    @allure.title("商品流程测试")
    def test_goods_workflow(self, login_fixtrue, base_url):
        with allure.step("添加商品"):
            goodscode = "sp_" + str(int(time.time()))
            r = add_goods(s=login_fixtrue, base_url=base_url, goodsname="《selenium 入门到精通12》", goodscode=goodscode, merchantid=12)

        with allure.step("查询商品"):
            time.sleep(1.2)
            sp_id = r.json()['data']['id']
            print("商品id是：", sp_id)
            goodsname = r.json()['data']['goodsname']
            print("修改之前的商品名称是：", goodsname)

        with allure.step("修改商品"):
            time.sleep(1.2)
            r2 = update_goods(s=login_fixtrue, base_url=base_url, sp_id=sp_id, goodsname="商品名称", goodscode=goodscode)
            print(r2.json())
            print("修改之后的商品名称是:", r2.json()['data']['goodsname'])
