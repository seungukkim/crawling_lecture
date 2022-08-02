import requests 
import pandas as pd
from bs4 import BeautifulSoup

def crawling(soup):

    tbody = soup.find("tbody")
    
    result = [] 
    for p in tbody.find_all("p",class_="title"):
        print(p.find("a").get_text())
        result.append(p.find("a").get_text())
   
  

    return None


def main():

    url = "https://music.bugs.co.kr/chart"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    print(crawling(soup))

if __name__ == "__main__":
    main()