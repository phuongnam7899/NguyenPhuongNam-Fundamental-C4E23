from urllib.request import urlopen
from bs4 import BeautifulSoup

page_content = urlopen("https://learn.freecodecamp.org/").read().decode("utf8")

soup = BeautifulSoup(page_content,"html.parser")
li= soup.find("li","superblock open")
li_list= li.ul.ul.find_all("li")
print(len(li_list))
