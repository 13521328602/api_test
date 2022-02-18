import requests
from requests import Response
import pytest
# 跨请求保持参数


# @pytest.fixture(scope='session')
def login(s: requests.Session, base_url, user: str, pwd: str) -> Response:
    url = base_url + "api/v1/login"
    body = {
        "username": user,
        "password": pwd
    }

    r = s.post(url, json=body)
    token = r.json()['token']
    h = {
        "Authorization": "Token {}".format(token)
    }
    s.headers.update(h)
    #print(s.headers)
    return r


if __name__ == '__main__':
    s = requests.session()
    base_url = "http://49.235.92.12:7005/"
    i = login(s, base_url, "test", "123456")
    print(s.headers)
    print(i.json())

