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