from pymongo import MongoClient

database_url = "mongodb://paula:1234@localhost:27018"

client = MongoClient(database_url)
db = client["cinema"]

def get_users():
    # Aquí podrías cargar las películas desde la base de datos
    users = db["users"].find()
    return list(users)

def get_user_by_email(email):
    # Aquí podrías buscar un usuario por correo electrónico
    user = db["users"].find_one({"email": email})
    return user

def insert_user(movie):
    # Aquí podrías insertar una nueva película en la base de datos
    db["users"].insert_one(movie)