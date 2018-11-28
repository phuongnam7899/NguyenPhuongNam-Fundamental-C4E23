from mongoengine import Document,StringField,IntField
class Bike(Document):
    model = StringField()
    daily_fee = StringField()
    image = StringField()
    year = StringField()
