from mongoengine import *


#creat collection
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField() #0: Female, 1: Male
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    image = StringField()
    description = StringField()
    measurements = ListField()
