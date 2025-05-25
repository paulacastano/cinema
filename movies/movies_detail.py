import tkinter as tk
from shows.shows_db import get_shows

# Función que abre ventana nueva
def abrir_detalle(movie, imagen):
    title = movie["title"]
    duration = movie["duration"]
    genres = ",".join(movie["genres"])
    shows = get_shows(movie_id=movie["id"])

    detalle = tk.Toplevel()
    detalle.title(title)
    detalle.geometry("300x400")
    detalle.configure(bg="white")

    tk.Label(detalle, text=title, font=("Helvetica", 14, "bold"), bg="white").pack(pady=10)

    label_img = tk.Label(detalle, image=imagen, bg="white")
    label_img.image = imagen  # Mantener referencia
    label_img.pack(pady=10)

    tk.Label(detalle, text=f"Duration: {duration} minutos", bg="white", wraplength=250, justify="center").pack(pady=1)
    tk.Label(detalle, text=f"Genres: {genres}", bg="white", wraplength=250, justify="center").pack(pady=0)

    shows_frame = tk.Frame(detalle, bg="white")
    shows_frame.pack(pady=5)

    for show in shows:
        show_label= show["timeSlot"]
        card = tk.Frame(shows_frame, bg="white", bd=1, relief="solid")
        card.pack(padx=0, pady=2)
        tk.Label(card, bg="white", text=show_label, font=("Helvetica", 10)).pack(anchor="w", padx=30, pady=5)

    
