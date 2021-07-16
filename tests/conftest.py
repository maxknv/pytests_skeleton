import logging

import pytest

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def my_fixture():
    logging.info("my_fixture call")
    yield "hello world"
    logging.info("my_fixture terminate")
