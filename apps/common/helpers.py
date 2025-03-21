# import re
# import requests





# def get_long_lat(location) -> tuple:

#     YANDEX_PATTERN = r'"longitute":(-?\d+\.\d+) , "latitude":(-?\d+\.\d+)'
#     GOOGLE_PATTERN = r"@(-?\d+\.\d+) , (-?\d+\.\d+)"
#     results = {}

#     try:
#         if re.match(r"https://yandex.\w+/?", location):
#            results["long"] , results["lat"] = str(location).split("/?ll")[-1].split("&")[0].split("?2C")
#            return results , True
#         elif re.match(r"https://(www.)*goo\w[.]\w+/?", location):
#             response = requests.get(location)
#             if response == 200:
#                 page_url = response.url
#                 ll = re.findall(YANDEX_PATTERN , page_url)
#                 results["long"] , results["lat"] = ll[0]
#                 return results , True
#     except Exception as e:
#         print(e)
#         return results , False
#     return results , False
