import pytest


class TestIt:
    @pytest.mark.smoketest
    def test_smth(self, my_fixture):
        a = " ".join(["hello", "world"])
        assert a == my_fixture
