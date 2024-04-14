from mongoengine import Document, StringField

class User(Document):
    email = StringField(required=True)
    password = StringField(required=True)