from mongoengine import Document,StringField

class To_do_list(Document):
    name = StringField()
    description = StringField()
    completed = StringField()