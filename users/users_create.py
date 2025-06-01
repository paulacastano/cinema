import tkinter as tk
import uuid
from tkinter import Toplevel, filedialog, messagebox
from users.users_db import insert_user


def crear_user():
    def guardar_user():
        name = entry_name.get()
        email = entry_email.get()
        password = entry_password.get()

        if not name or not email or not password:
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        # Aquí podrías guardar en una base de datos o estructura de datos
        user = {
            "_id": str(uuid.uuid4()),  # Generar un ID único
            "name": name,
            "email": email,
            "password": password,
        }
        insert_user(user)  # Guardar en la base de datos
        messagebox.showinfo("Éxito", "Usuario guardado correctamente.")
        ventana.destroy()

    ventana = Toplevel()
    ventana.title("Crear nuevo usuario")
    ventana.geometry("400x300")
    ventana.configure(bg="white")

    # Campos del formulario
    tk.Label(ventana, text="Nombre:", bg="white").pack(pady=(10, 0))
    entry_name = tk.Entry(ventana, width=40)
    entry_name.pack(pady=5)

    tk.Label(ventana, text="Email:", bg="white").pack(pady=(10, 0))
    entry_email = tk.Entry(ventana, width=40)
    entry_email.pack(pady=5)

    tk.Label(ventana, text="Password:", bg="white").pack(pady=(10, 0))
    entry_password = tk.Entry(ventana, width=40)
    entry_password.pack(pady=5)

    # Botón guardar
    btn_guardar = tk.Button(ventana, text="Guardar usuario", command=guardar_user, bg="#4CAF50", fg="white")
    btn_guardar.pack(pady=20)