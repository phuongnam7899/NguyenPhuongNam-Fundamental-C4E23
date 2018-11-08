from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#1 connect to page
url = "https://dantri.com.vn"
connection = urlopen(url) 


#2 dowload the content of page
raw_data=connection.read()
page_content = raw_data.decode("utf8") 
# with open("dantri.html","wb") as f:
# f.write(raw_data)


#3 find the ROI(region of interest) region
soup = BeautifulSoup(page_content, "html.parser")
ul = soup.find("ul","ul1 ulnew")#href=...,id="..."


#4 extract data
news_list=[]
li_list = ul.find_all("li")
for li in li_list:
    a= li.h4.a
    title=a.string
    link=url+ a["href"]
    news=OrderedDict({
        "title":title,
        "link":link,
    })
    news_list.append(news)
#5 save data
pyexcel.save_as(records=news_list,dest_file_name="dantri.xlsx")

