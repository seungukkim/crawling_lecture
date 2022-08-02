
from selenium import webdriver
from bs4 import BeautifulSoup
driver=webdriver.Chrome('C:\\Users\\human\\Desktop\\crawling_exercise\\chromedriver.exe')
driver.implicitly_wait(3)
driver.get("https://www.livesport.com/kr/team/ulsan-hyundai/EVEwgyOM/")

page = driver.page_source

bs_obj = BeautifulSoup(page,"html.parser")
win=bs_obj.find_all("span",{"class":"wld wld--w"})
tiewin=bs_obj.find_all("span",{"class":"wld wld--wo"})
draw = bs_obj.find_all("span",{"class":"wld wld--d"})
lose =bs_obj.find_all("span",{"class":"wld wld--l"})
tielose=bs_obj.find_all("span",{"class":"wld wld--lo"})

n_win=len(win)+len(tiewin)
n_draw = len(draw)
n_lose = len(lose)+len(tielose)

report = {'win':n_win, 'draw':n_draw, 'lose':n_lose}

max_n = max(report.values())
for key in report:
    if(report[key]==max_n):
        print(key)