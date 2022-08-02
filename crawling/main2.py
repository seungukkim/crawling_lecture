from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https:"+"//ai-dev.tistory.com/2"
html = urlopen(url)
bs_obj=BeautifulSoup(html,"html.parser")
title=bs_obj.find_all("h1")
table_tag=bs_obj.find_all("table")
table_tag01=table_tag[0].find_all("td")
for idx, element in enumerate(table_tag01):
    print(idx,element.text)