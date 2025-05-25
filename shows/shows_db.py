from pymongo import MongoClient

database_url = "mongodb://paula:1234@localhost:27018"

client = MongoClient(database_url)
db = client["cinema"]

def get_shows(movie_id=None):
    # Aquí podrías cargar las funciones desde la base de datos
    shows = db["shows"].find({"movieId": movie_id})
    return list(shows)