import tkinter as tk
from movies.movie_create import crear_pelicula
from movies.movies_screen import open_cartelera

def ver_cartelera():
    # Aquí puedes agregar la lógica para mostrar la cartelera de películas
    print("Mostrando cartelera de películas...")
    open_cartelera()

# Crear ventana principal
root = tk.Tk()
root.title("App de Películas")
root.geometry("600x400")

# Crear la barra de menú
menubar = tk.Menu(root)
root.config(menu=menubar)

# Menú "Películas"
peliculas_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Películas", menu=peliculas_menu)

# Opción del menú para crear nueva película
peliculas_menu.add_command(label="Crear película", command=crear_pelicula)
peliculas_menu.add_command(label="Ver cartelera", command=ver_cartelera)

# Ejemplo de contenido principal
tk.Label(root, text="Bienvenido a la App de Películas", font=("Helvetica", 16)).pack(pady=20)

root.mainloop()
