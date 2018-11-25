from mongoengine import Document,IntField,StringField
class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()
