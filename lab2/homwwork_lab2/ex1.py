from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel
from youtube_dl import YoutubeDL


# part 1
url="https://www.apple.com/itunes/charts/songs/"
connection= urlopen(url)

raw_data= connection.read()
page_content= raw_data.decode("utf8")

soup= BeautifulSoup(page_content,"html.parser")
section = soup.find("section","section chart-grid")

songs_list=[]
li_list=section.div.ul.find_all("li")
for li in li_list:
    a_h3=li.h3.a
    a_h4=li.h4.a
    title= a_h3.string
    artist= a_h4.string
    link= url + a_h3["href"]
    song={
        "title" : title,
        "artist":artist
    }
    songs_list.append(song)
pyexcel.save_as(records=songs_list,dest_file_name="itune top song.xlsx")


# part 2
options ={
    "default_search":"ytsearch",
    "max download":1
}
dl= YoutubeDL(options)
key_list=[]
for song in songs_list:
    key_search= song["title"] +" "+ song["artist"]
    key_list.append(key_search)
dl.download(key_list)
