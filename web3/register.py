from mongoengine import StringField,Document

class Register(Document):
    user_name = StringField()
    pass_word = StringField()
    mail = StringField()