from urllib.request import urlopen
import json
import mlab
from quiz import Questions

mlab.connect()

url = " https://opentdb.com/api.php?amount=50"
connect = urlopen(url)

page_content = connect.read().decode("utf8")
dic = json.loads(page_content)

li = dic["results"]
for qu in li:
    q = Questions(Category=qu["category"],Type=qu["type"],Difficulty=qu["difficulty"],Question=qu["question"],Correct_answer=qu["correct_answer"],Incorrect_answer=qu["incorrect_answers"])
    q.save()






