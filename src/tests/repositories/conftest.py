import pytest
from tests.test_app import fixture_test_app # pylint: disable=unused-import

@pytest.fixture(autouse=True, scope='function')
def auto_fixture_test_app(fixture_test_app): # pylint: disable=unused-argument, redefined-outer-name
    return None
