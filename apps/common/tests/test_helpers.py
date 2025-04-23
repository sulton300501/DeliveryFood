from apps.common.helpers import get_long_lat


def test_yandex_link():
    url = "https://yandex.uz/?ll=69.275822%2C41.2965807"
    result, status = get_long_lat(url)
    assert status is True
    assert result["long"] == "69.275822"
    assert result["lat"] == "41.2965807"


def test_google_link():
    url = url = "https://www.google.com/maps/place/@41.2965807,69.275822,17z"
    result, status = get_long_lat(url)
    assert status is True
    assert result["long"] == "41.2965807"
    assert result["lat"] == "69.275822"
