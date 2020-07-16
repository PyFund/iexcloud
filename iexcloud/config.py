import os


def set_token(token: str):
    """Set the api token environment variable for IEX Cloud

    Args:
        token: API token
    """

    os.environ["IEX_TOKEN"] = token


def set_test_token(token: str):
    """Set the api test token environment variable for IEX Cloud

    Args:
        token: API test token
    """

    os.environ["IEX_TEST_TOKEN"] = token


def set_mode(mode: str = "PRODUCTION"):
    """Set the production mode for IEX API.

    Args:
        mode: {"PRODUCTION", "TEST"}. The production mode. Defaults to "PRODUCTION".
    
    Raises:
        ValueError: when mode supplied is not one of PRODUCTION or TEST 
    """

    if mode not in ["PRODUCTION", "TEST"]:
        raise ValueError("Mode should be one of 'PRODUCTION', 'TEST'")

    os.environ["IEX_MODE"] = mode


def get_token() -> str:
    """Retrieve the current token for use with IEX Cloud

    Raises:
        EnvironmentError: when mode is set to TEST but TEST Token is not set
        EnvironmentError: when PRODUCTION Token is not set

    Returns:
        str: IEX API Token
    """

    if "IEX_MODE" in os.environ and "IEX_MODE" in os.environ:
        if "IEX_TEST_TOKEN" in os.environ:
            return os.environ["IEX_TEST_TOKEN"]
        else:
            raise EnvironmentError("IEX Test Token is not set.")
    else:
        if "IEX_TOKEN" in os.environ:
            return os.environ["IEX_TOKEN"]
        else:
            raise EnvironmentError("IEX Token is not set.")
