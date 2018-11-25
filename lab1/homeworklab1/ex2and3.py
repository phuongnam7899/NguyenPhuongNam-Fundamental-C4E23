from pymongo import MongoClient
uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client=MongoClient(uri)
data_base= client.get_database()
posts=data_base["posts"]
new_post= {
    "title":"Something",
    "author":"Nguyễn Phương Nam",
    "content":'''
    La bàn chỉ giúp ta xác định phương hướng, còn đi theo hướng nào là quyết định của mỗi người
    Quyết định đến với Techkids của em cũng vậy, em đã nghe review của rât nhiều người trước khi chọn Techkids,nhưng chỉ khi đến học em mới hiểu được sự nhiệt tình của các anh,các anh dạy theo kiểu "đố không hiểu" luôn.
    Vô địch cũng được,không vô địch cũng được, học Techkids xong kiểu gì cũng vô địch:)
    ''',
}
posts.insert_one(new_post)
client.close()