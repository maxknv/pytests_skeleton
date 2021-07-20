import pytest

from tests.utils.curl import Curl


@pytest.fixture(scope="session")
def httpserver_listen_address():
    """
    Just a fixture to make pytest http server listen on pre-configured port
    :return:
    """
    return "127.0.0.1", 65065


class TestIt:
    @pytest.mark.smoketest
    def test_github(self):
        code, content = Curl.request_get('https://api.github.com')
        assert code == 200 and 'authorizations_url' in content

    @pytest.mark.smoketest
    def test_smth(self, my_fixture):
        a = " ".join(["hello", "world"])
        assert a == my_fixture

    def test_with_httpclient(self, httpserver):
        httpserver.expect_request("/foo").respond_with_json({"foo": "bar"})
        code, json = Curl.request_get(httpserver.url_for("/foo"))
        assert code == 200 and json == {'foo': 'bar'}