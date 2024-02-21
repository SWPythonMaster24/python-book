import requests
import json


# API를 호출하고 응답을 확인합니다
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# 데이터 구조를 살펴봅니다
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)