import os
import pytest
from iexcloud import set_mode, set_token, set_test_token, get_token, get_url
from iexcloud.constants import IEX_CLOUD, IEX_CLOUD_TEST


def test_set_mode():

    set_mode("PRODUCTION")
    assert os.environ["IEX_MODE"] == "PRODUCTION"

    set_mode("TEST")
    assert os.environ["IEX_MODE"] == "TEST"

    with pytest.raises(ValueError):
        set_mode("INVALID_MODE")


def test_set_token():

    set_token("production_token")
    assert os.environ["IEX_TOKEN"] == "production_token"


def test_set_test_token():

    set_test_token("test_token")
    assert os.environ["IEX_TEST_TOKEN"] == "test_token"


def test_get_token():

    set_token("production_token")
    set_test_token("test_token")

    set_mode("TEST")
    assert get_token() == "test_token"

    with pytest.raises(OSError):

        del os.environ["IEX_TEST_TOKEN"]
        get_token()

    set_mode("PRODUCTION")
    assert get_token() == "production_token"

    del os.environ["IEX_MODE"]
    assert get_token() == "production_token"

    with pytest.raises(OSError):

        del os.environ["IEX_TOKEN"]
        get_token()


def test_get_url():

    set_mode("PRODUCTION")
    assert get_url() == IEX_CLOUD

    set_mode("TEST")
    assert get_url() == IEX_CLOUD_TEST
