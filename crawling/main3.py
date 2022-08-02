from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://ai-dev.tistory.com/2"
html = urlopen(url)
bs_obj=BeautifulSoup(html,"html.parser")

title=bs_obj.find_all("h1")


table01=bs_obj.find_all("td")
table = bs_obj.find_all("td",{"style":"width: 33.3333%; text-align: center;"})
for idx,element in enumerate(table):
    print(idx,element.text)