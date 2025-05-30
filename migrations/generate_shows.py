import json
from faker import Faker
import sys
import uuid
import random

shows = []

with open("movies.json", "r") as f:
    movies = json.load(f)

    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
            for i in range(num):
                show = {
                    "_id": str(uuid.uuid4()),
                    "movieId": random.choice(movies)["_id"],
                    "roomId": str(uuid.uuid4()),  # Assuming there are 10 rooms
                    "date": "2025-05-26",
                    "timeSlot": f"{Faker().random_int(min=10, max=22)}:00-{Faker().random_int(min=12, max=24)}:00",
                    "price": Faker().random_int(min=10, max=20)
                }
                shows.append(show)
            with open("shows.json", "w") as f:
                f.write(json.dumps(shows, indent=4))
        except ValueError:
            print("Argument is not a valid integer.")
    else:
        print("No integer argument provided.")
