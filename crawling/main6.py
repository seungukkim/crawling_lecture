
import requests 
import pandas as pd
from bs4 import BeautifulSoup

def crawling(soup):

    pclass = soup.find("tbody")
    # print(pclass)
    result = [] 
    for a in pclass.find_all("p",class_="title"):
        # print(a.get_text())
        result.append(a.get_text())
    # print(result[0])
    links = []
    for a in pclass.find_all("a"):
        # print(a['href'])
        # result.append(a.get_text())
        links.append(a['href'])
    a=pd.Series(result,links)
    print(a)
    a.to_csv('file.csv',encoding='utf-8-sig')


    return None


def main():

    url = "https://www.dreamspon.com/scholarship/list.html"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    print(crawling(soup))
    

if __name__ == "__main__":
    main()