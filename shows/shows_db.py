from pymongo import MongoClient
import datetime

database_url = "mongodb://paula:1234@localhost:27018"

client = MongoClient(database_url)
db = client["cinema"]

def get_shows_by_movie(movie_id=None):
    today =  datetime.date.today()
    # Aquí podrías cargar las funciones desde la base de datos
    shows = db["shows"].find({"movieId": movie_id, "date": today.strftime("%Y-%m-%d")})
    return list(shows)

def get_show_by_id(show_id):
    # Aquí podrías buscar una función por su ID
    show = db["shows"].find_one({"_id": show_id})
    return show