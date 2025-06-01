import tkinter as tk
from users.users_db import get_users
from users.users_detail import open_users_detail

def open_users():
    users = get_users()

    users_screen = tk.Toplevel()
    users_screen.title("Vista de Usuarios")
    users_screen.geometry("400x600")
    users_screen.configure(bg="white")

    users_frame = tk.Frame(users_screen, bg="white")
    users_frame.pack(pady=15)
    title_label = tk.Label(users_frame, text="Usuarios", bg="white", font=("Helvetica", 16))
    title_label.pack(pady=10)

    for user in users:
        name_label= user["email"]
        card = tk.Frame(users_frame, bg="white", bd=1, relief="solid")
        card.pack(padx=0, pady=2, fill="x")
        card.bind("<Button-1>", lambda e, user=user: open_users_detail(user["email"]))
        label = tk.Label(card, bg="white", text=name_label, font=("Helvetica", 10))
        label.pack(anchor="center", padx=30, pady=5)
        label.bind("<Button-1>", lambda e, user=user: open_users_detail(user["email"]))