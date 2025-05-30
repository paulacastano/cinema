from pymongo import MongoClient

database_url = "mongodb://paula:1234@localhost:27018"

client = MongoClient(database_url)
db = client["cinema"]

def get_movies():
    # Aquí podrías cargar las películas desde la base de datos
    movies = db["movies"].find()
    return list(movies)

def get_movie_by_id(movie_id):
    # Aquí podrías buscar una película por su ID
    movie = db["movies"].find_one({"_id": movie_id})
    return movie

def insert_movie(movie):
    # Aquí podrías insertar una nueva película en la base de datos
    db["movies"].insert_one(movie)