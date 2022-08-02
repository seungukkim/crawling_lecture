from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://ai-dev.tistory.com/1"
html = urlopen(url)
bs_obj=BeautifulSoup(html,"html.parser")
title=bs_obj.find_all("h1")
contents = bs_obj.find_all("p")
print(contents[1])