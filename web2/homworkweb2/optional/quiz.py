from mongoengine import StringField,ListField,Document

class Questions(Document):
    Category = StringField()
    Type = StringField()
    Difficulty = StringField()
    Question = StringField()
    Correct_answer = StringField()
    Incorrect_answer = ListField()
    