import requests
import time


def get_goods(s, base_url, sp_id):
    # 查询单个商品
    url = base_url + "api/v2/goods/{}".format(sp_id)
    r = s.get(url)
    return r


def add_goods(s: requests.session, base_url, goodsname: str, goodscode: str, **kwargs):
    # 新增商品
    url = base_url + "api/v2/goods"

    body = {
        "goodsname": goodsname,
        "goodscode": goodscode
    }
    body.update(kwargs)
    r2 = s.post(url, json=body)
    return r2


def update_goods(s, base_url, sp_id, goodsname, goodscode):
    # 修改商品
    url = base_url + "api/v2/goods/{}".format(sp_id)
    body = {
        "goodsname": goodsname,
        "goodscode": goodscode
    }
    r = s.put(url, json=body)
    return r


if __name__ == '__main__':
    from api.login_api import login
    import requests
    s = requests.session()
    r1 = login(s, "test", "123456")
    r3 = get_goods(s, sp_id=2)
    #print(r3.text)
    goodscode = "sp_" + str(int(time.time()))
    r2 = update_goods(s, 18705, "商品名称", goodscode)
    print(r2.json())
    #goodscode = "sp_" + str(int(time.time()))
    #r4 = add_goods(s, "《selenium 入门到精通12》", goodscode=goodscode, merchantid=12)
    #print("-"*20)
    #print(r4.text)

