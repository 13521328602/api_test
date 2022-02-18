import pytest
import requests
from api.login_api import login


@pytest.fixture(scope="session")
def login_fixtrue(base_url):
    s = requests.Session()
    login(s, base_url, "test", "123456")
    yield s
    s.close()

