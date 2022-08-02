import requests
from bs4 import BeautifulSoup

url="https://www.naver.com"

req = requests.get(url)
print(req.status_code)
# print(req.text)