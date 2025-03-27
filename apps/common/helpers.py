import re

import requests


def get_long_lat(location) -> tuple:
    """
    return:content,status code
    example:
        error: ({}, 404),
        success: ({'long': '41.2965807', 'lat': '69.275822'}, 200)
    """
    YANDEX_PATTERN = r'"longitude":(-?\d+\.\d+),"latitude":(-?\d+\.\d+)'  # noqa
    GOOGLE_PATTERN = r"@(-?\d+\.\d+),(-?\d+\.\d+)"
    results = {}
    try:
        if re.match("https://yandex.\w+/?", location):  # noqa
            results["long"], results["lat"] = str(location).split("/?ll=")[-1].split("&")[0].split("%2C")
            return results, True
        elif re.match("https://(www.)*goo\w*[.]\w+/?", location):  # noqa
            response = requests.get(location)
            if response.status_code == 200:
                page_url = response.url
                ll = re.findall(GOOGLE_PATTERN, page_url)
                results["long"], results["lat"] = ll[0]
                return results, True
    except Exception as e:
        print(e)
        return results, False
    return results, False
