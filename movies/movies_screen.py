import tkinter as tk
from tkinter import Canvas, Scrollbar, Frame, Toplevel, Label
from PIL import Image, ImageTk
from movies.movies_detail import abrir_detalle
from movies.movies_db import get_movies

# Cargar imagen (usa la misma para todas como ejemplo)
def cargar_imagen(ruta, size=(150, 150)):
    imagen = Image.open(ruta)
    imagen = imagen.resize(size, Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(imagen)

def open_cartelera():
    # Crear ventana
    # Obtener el ancho y alto de la pantalla
    cartelera = Toplevel()
    cartelera.title("Cartelera de Películas")
    ancho_pantalla = cartelera.winfo_screenwidth()
    alto_pantalla = cartelera.winfo_screenheight()
    cartelera.geometry(f"{ancho_pantalla}x{alto_pantalla}")
    cartelera.configure(bg="#f0f0f0")

    # Crear un canvas y un scrollbar
    canvas = Canvas(cartelera)
    scrollbar = Scrollbar(cartelera, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Contenedor
    main_frame = Frame(canvas, bg="#f0f0f0")
    canvas.create_window((0, 0), window=main_frame, anchor="nw")
    # Hacer que el canvas se actualice con el tamaño del contenido
    def configurar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    main_frame.bind("<Configure>", configurar_scroll)

    # Encabezado
    Label(canvas, text="🎬 Peliculas en cartelera 🎬", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)


    # Mostrar cards con imagen
    for index, movie in enumerate(get_movies()):
        pelicula = movie["title"]  # Cambia esto según tu estructura de datos
        imagen_route = "poster.jpg"
        if movie.get("image"):
            imagen_route = movie["image"]

        imagen_pelicula = cargar_imagen(imagen_route)
        row = index // 6
        col = index % 6

        card = Frame(main_frame, bg="white", bd=1, relief="solid")
        card.grid(row=row, column=col, padx=10, pady=10)

        label_img = Label(card, image=imagen_pelicula, bg="white")
        label_img.image = imagen_pelicula  # Importante: evitar que se elimine por el recolector
        label_img.pack(padx=10, pady=(10, 5))

        label_text = Label(card, text=pelicula, font=("Helvetica", 12), bg="white", wraplength=140, justify="center")
        label_text.pack(padx=10, pady=(0, 10))

        # Asociar clic al frame y a los elementos internos
        card.bind("<Button-1>", lambda e, movie=movie: abrir_detalle(movie, imagen_pelicula))
        label_img.bind("<Button-1>", lambda e, movie=movie: abrir_detalle(movie, imagen_pelicula))
        label_text.bind("<Button-1>", lambda e, movie=movie: abrir_detalle(movie, imagen_pelicula))

    # Configurar columnas
    main_frame.grid_columnconfigure(0, weight=5)
    main_frame.grid_columnconfigure(1, weight=5)
    main_frame.grid_columnconfigure(2, weight=5)
    main_frame.grid_columnconfigure(3, weight=5)
    main_frame.grid_columnconfigure(4, weight=5)
