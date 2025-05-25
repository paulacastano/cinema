import tkinter as tk
from tkinter import Toplevel, filedialog, messagebox
from movies.movies_db import insert_movie

def crear_pelicula():
    def guardar_pelicula():
        titulo = entry_titulo.get()
        generos = entry_genero.get()
        duracion = entry_duracion.get()
        imagen = entry_imagen.get()

        if not titulo or not generos or not duracion or not imagen:
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        # Aquí podrías guardar en una base de datos o estructura de datos
        movie = {
            "title": titulo,
            "duration": int(duracion),
            "genres": generos.split(","),
            "image": imagen
        }
        insert_movie(movie)  # Guardar en la base de datos
        messagebox.showinfo("Éxito", "Película guardada correctamente.")
        ventana.destroy()

    def seleccionar_imagen():
        ruta = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.gif")]
        )
        if ruta:
            entry_imagen.delete(0, tk.END)
            entry_imagen.insert(0, ruta)

    ventana = Toplevel()
    ventana.title("Crear nueva película")
    ventana.geometry("400x300")
    ventana.configure(bg="white")

    # Campos del formulario
    tk.Label(ventana, text="Título:", bg="white").pack(pady=(10, 0))
    entry_titulo = tk.Entry(ventana, width=40)
    entry_titulo.pack(pady=5)

    tk.Label(ventana, text="Géneros:", bg="white").pack(pady=(10, 0))
    entry_genero = tk.Entry(ventana, width=40)
    entry_genero.pack(pady=5)

    tk.Label(ventana, text="Duración (min):", bg="white").pack(pady=(10, 0))
    entry_duracion = tk.Entry(ventana, width=40)
    entry_duracion.pack(pady=5)

    tk.Label(ventana, text="Imagen:", bg="white").pack(pady=(10, 0))
    frame_imagen = tk.Frame(ventana, bg="white")
    frame_imagen.pack(pady=5)

    entry_imagen = tk.Entry(frame_imagen, width=30)
    entry_imagen.pack(side=tk.LEFT, padx=(0, 5))
    btn_buscar = tk.Button(frame_imagen, text="Seleccionar", command=seleccionar_imagen)
    btn_buscar.pack(side=tk.LEFT)

    # Botón guardar
    btn_guardar = tk.Button(ventana, text="Guardar película", command=guardar_pelicula, bg="#4CAF50", fg="white", padx=10)
    btn_guardar.pack(pady=20)