import pytest
from tests.test_app import fixture_test_app

@pytest.fixture(autouse=True, scope='function')
def auto_fixture_test_app(fixture_test_app):
    return None
