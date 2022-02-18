import requests


def user_register(base_url, username: str="test", password: str="123456"):
    url = base_url + "api/v1/register"
    body = {
        "username": username,
        "password": password
    }

    r = requests.post(url, json=body)
    return r


if __name__ == '__main__':
    r2 = user_register("test", "123456")
    print(r2.json())
