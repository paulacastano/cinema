from pymongo import MongoClient

database_url = "mongodb://paula:1234@localhost:27018"

client = MongoClient(database_url)
db = client["cinema"]

def get_room_by_id(room_id):
    return db["rooms"].find_one({"_id": room_id})