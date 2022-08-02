from urllib.request import urlopen
from bs4 import BeautifulSoup

url="https://www.dreamspon.com/scholarship/list.html"
html = urlopen(url)
bs_obj=BeautifulSoup(html,"html.parser")

list1=bs_obj.find_all("p",{"class":"title"})
list2=list1[0].find_all("a")

print(list2[0])

# com_list=bs_obj.find_all("ul",{"style":"list-style-type: disc;"})
# com_list02=com_list[0].find_all("li")
# for idx,element in enumerate(com_list02):
#     print(idx,element.text)