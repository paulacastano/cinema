import json
import datetime
from faker import Faker
import sys
import uuid
import random

shows = []
current_date = datetime.date.today().strftime("%Y-%m-%d")

with open("movies.json", "r") as f:
    movies = json.load(f)
    with open("rooms.json", "r") as f_rooms:
        rooms = json.load(f_rooms)
        if len(sys.argv) > 1:
            try:
                num = int(sys.argv[1])
                for i in range(num):
                    start_time = Faker().random_int(min=10, max=22)
                    end_time = Faker().random_int(min=start_time + 1, max=min(start_time + 3, 24))
                    show = {
                        "_id": str(uuid.uuid4()),
                        "movieId": random.choice(movies)["_id"],
                        "roomId": random.choice(rooms)["_id"],  # Assuming there are 10 rooms
                        "date": current_date,
                        "timeSlot": f"{start_time}:00-{end_time}:00",
                        "price": Faker().random_int(min=10, max=20)
                    }
                    shows.append(show)
                with open("shows.json", "w") as f:
                    f.write(json.dumps(shows, indent=4))
            except ValueError:
                print("Argument is not a valid integer.")
        else:
            print("No integer argument provided.")
