from pymongo import MongoClient

uri="mongodb://admin:admin1@ds249503.mlab.com:49503/c4e23-vlog"

#1 connect
client=MongoClient(uri)

#2 ge default database
db = client.get_database()

#3 get collection
posts = db["post"]
movies=db["movies"]

#4 creat data
new_post={
    "title":"hom nay troi nang",
    "content":"toi van di hoc",
}
new_movie={
    "title":"hihi",
    "rating":9
}
#5 insert data
# posts.insert_one(new_post)
# movies.insert_one(new_movie)

#5' read data
post_list = posts.find()
p= post_list[0]
for i in post_list:
    print(p["title"])
    print(p["content"])
#6 close connection
client.close()

