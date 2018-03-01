from mongoengine import Document, StringField, IntField, BooleanField


class Customer(Document):
    name = StringField()
    gender = IntField() #0: Female, 1: Male
    email = StringField()
    phonenumber = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()
