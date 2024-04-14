from mongoengine import connect

def initialize_db():
    connect(
        db='essai',
        host='mongodb+srv://admin:louay@cluster0.g7oulyh.mongodb.net/'
    )