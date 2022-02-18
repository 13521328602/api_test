import requests

for i in range(1, 101):
    url = "http://49.235.92.12:7005/api/v1/register"
    body = {
            "username": "test_user_{}".format(i),
            "password": "123456"
        }
    r = requests.post(url, json=body)
    print(r.json())
    with open("test_user_paw.txt", 'a') as file:
        file.write("test_user_{},123456\n".format(i))
