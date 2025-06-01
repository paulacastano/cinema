import tkinter as tk
from users.users_db import get_user_by_email
from booking.booking_db import get_bookings_by_user_id
from movies.movies_db import get_movie_by_id
from shows.shows_db import get_show_by_id
from rooms.room_db import get_room_by_id

def open_users_detail(email):
    user = get_user_by_email(email)

    user_screen = tk.Toplevel()
    user_screen.title("Vista de Usuarios")
    user_screen.geometry("400x600")
    user_screen.configure(bg="white")

    user_frame = tk.Frame(user_screen, bg="white")
    user_frame.pack(pady=15)
    title_label = tk.Label(user_frame, text="Nombre: " + user["name"], bg="white", font=("Helvetica", 12), justify="left")
    title_label.pack(pady=5, fill="x")
    email_label = tk.Label(user_frame, text="Correo: " + user["email"], bg="white", font=("Helvetica", 12), justify="left")
    email_label.pack(pady=5, fill="x")

    bookings = get_bookings_by_user_id(user["_id"])
    bookings_dict = {}

    for book in bookings:
        showId = book["showId"]
        if showId in bookings_dict:
            bookings_dict[showId]["chairs"].append(book["chairId"])
        else:
            show = get_show_by_id(showId)
            movie = get_movie_by_id(show["movieId"])
            room = get_room_by_id(show["roomId"])
            bookings_dict[showId] = {
                "movie": movie,
                "show": showId,
                "room": room,
                "chairs": [book["chairId"]],
                "date": book["date"],
                "timeSlot": book["timeSlot"]
            }

    bookin_list = list(bookings_dict.values())
    for book in bookin_list:
        # sillas = ','.join(str(x) for x in book["chairs"])
        show_date = book["date"] + "-" + book["timeSlot"]
        sala = book["room"]["name"]
        genres = ', '.join(book["movie"]["genres"])
        movie_title = book["movie"]["title"]
        card = tk.Frame(user_frame, bg="white", bd=1, relief="solid")
        card.pack(padx=0, pady=2, fill="x")
        label = tk.Label(card, bg="white", text=movie_title, font=("Helvetica", 10))
        label.pack(anchor="center", padx=10, pady=2)
        label = tk.Label(card, bg="white", text=show_date, font=("Helvetica", 10))
        label.pack(anchor="center", padx=10, pady=2)
        label = tk.Label(card, bg="white", text=sala, font=("Helvetica", 10))
        label.pack(anchor="center", padx=10, pady=2)
        label = tk.Label(card, bg="white", text=genres, font=("Helvetica", 10))
        label.pack(anchor="center", padx=10, pady=2)