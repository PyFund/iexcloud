from iexcloud import set_test_token, set_mode, Stock


def test_env_init():

    set_mode("TEST")
    set_test_token("Tpk_f26565bf30a611e9958142010a80043c")


def test_dividend():

    stock = Stock("KO")
    result = stock.get_dividend("1y")
    assert list(result.columns) == [
        "exDate",
        "paymentDate",
        "recordDate",
        "declaredDate",
        "amount",
        "flag",
        "currency",
        "description",
        "frequency",
        "date",
    ]


def test_earning():

    stock = Stock("KO")
    result = stock.get_earning(2)
    assert list(result.columns) == [
        "actualEPS",
        "consensusEPS",
        "announceTime",
        "numberOfEstimates",
        "EPSSurpriseDollar",
        "EPSReportDate",
        "fiscalPeriod",
        "fiscalEndDate",
        "yearAgo",
        "yearAgoChangePercent",
        "currency",
    ]


def test_logo():

    stock = Stock("KO")
    result = stock.get_logo()
    assert isinstance(result, str)


def test_news():

    stock = Stock("KO")
    result = stock.get_news(1)
    assert list(result.columns) == [
        "datetime",
        "headline",
        "source",
        "url",
        "summary",
        "related",
        "image",
        "lang",
        "hasPaywall",
    ]


def test_price():

    stock = Stock("KO")
    result = stock.get_price("1m")
    assert list(result.columns) == [
        "date",
        "open",
        "close",
        "high",
        "low",
        "volume",
        "uOpen",
        "uClose",
        "uHigh",
        "uLow",
        "uVolume",
        "change",
        "changePercent",
        "label",
        "changeOverTime",
    ]


def test_peer():

    stock = Stock("KO")
    result = stock.get_peer()
    assert isinstance(result, list)


def test_profile():

    stock = Stock("KO")
    result = stock.get_profile()
    assert list(result.keys()) == [
        "symbol",
        "companyName",
        "exchange",
        "industry",
        "website",
        "description",
        "CEO",
        "securityName",
        "issueType",
        "sector",
        "primarySicCode",
        "employees",
        "tags",
        "address",
        "address2",
        "state",
        "city",
        "zip",
        "country",
        "phone",
    ]


def test_split():

    stock = Stock("KO")
    stock = Stock("APRN")
    result = stock.get_split("5y")
    assert list(result.columns) == [
        "exDate",
        "declaredDate",
        "ratio",
        "toFactor",
        "fromFactor",
        "description",
        "date",
    ]


def test_json():

    stock = Stock("KO", output="json")
    result = stock.get_price("5d")

    assert isinstance(result, str)
