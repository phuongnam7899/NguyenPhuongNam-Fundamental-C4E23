from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url="http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
connection= urlopen(url)
raw_data= connection.read()
page_content = raw_data.decode("utf8")
soup= BeautifulSoup(raw_data)
table_full=[]
table_html= soup.find("div",style="overflow:hidden;width:100%;border-bottom:solid 1px #cecece;")
tr_list= table_html.find_all("tr")
for tr in tr_list:
    td_list= tr.find_all("td")
    rows={}
    for i in range(len(td_list)):
        if td_list[i].string != None:
            if i==0:
                rows["Hạng mục"]=td_list[i].string.strip()
            elif i==1:
                rows["Qúy 4-2016"]=td_list[i].string.strip()
            elif i==2:
                rows["Quý 1-2017"]=td_list[i].string.strip()
            elif i==3:
                rows["Quý 2-2017"]=td_list[i].string.strip()
            elif i==4:
                rows["Quý 3-2017"]=td_list[i].string.strip()
    if rows != {}:
        table_full.append(rows)
pyexcel.save_as(records=table_full,dest_file_name="Kết quả hoạt động kinh doanh công ty cổ phần sữa Việt Nam.xlsx")
