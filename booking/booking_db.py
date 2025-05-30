from pymongo import MongoClient

database_url = "mongodb://paula:1234@localhost:27018"

client = MongoClient(database_url)
db = client["cinema"]

def create_bookings(bookings):
    db["bookings"].insert_many(bookings)

def get_bookings_by_show_id(show_id):
    """
    Retrieves bookings for a specific show by its ID.
    """
    bookings = db["bookings"].find({"showId": show_id})
    return list(bookings)