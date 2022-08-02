from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://www.dreamspon.com/scholarship/list.html"
html = urlopen(url)
bs_obj=BeautifulSoup(html,"html.parser")

list1=bs_obj.find_all("p",{"class":"title"})
list2=list1[0].find_all("a")

print(list2[0]['href'])

# com_list=bs_obj.find_all("ul",{"style":"list-style-type: disc;"})
# com_list02=com_list[0].find_all("li")
# for idx,element in enumerate(com_list02):
#     print(idx,element.text)

import requests 
import pandas as pd
from bs4 import BeautifulSoup

def crawling(soup):

    div = soup.find("div", class_ = "list_issue")
  # print(div)
    result = [] 
    for a in div.find_all("a"):
    # print(a.get_text())
        result.append(a.get_text())

    links = []
    for a in div.find_all("a"):
    # print(a['href'])
    # result.append(a.get_text())
        links.append(a['href'])
    a=pd.Series(result,links)
    print(a)
    a.to_csv('file.csv',encoding='utf-8-sig')


    return None


def main():

    url = "https://www.naver.com/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    print(crawling(soup))

if __name__ == "__main__":
    main()