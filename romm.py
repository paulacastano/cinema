import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Base de datos simulada de usuarios (solo correos válidos)
usuarios = [
    "juan@example.com",
    "maria@example.com",
    "ana@example.com",
    "carlos@example.com"
]

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Sala de Cine - Selección y Asignación de Asientos")
ventana.geometry("520x500")

# Cargar imágenes de sillas
img_libre = ImageTk.PhotoImage(Image.open("silla-libre.png").resize((40, 40)))
img_seleccionada = ImageTk.PhotoImage(Image.open("silla-seleccionada.png").resize((40, 40)))

asientos_seleccionados = []
botones = {}

# Función para seleccionar asiento
def seleccionar_asiento(numero_asiento):
    if numero_asiento in asientos_seleccionados:
        asientos_seleccionados.remove(numero_asiento)
        botones[numero_asiento].config(image=img_libre)
    else:
        asientos_seleccionados.append(numero_asiento)
        botones[numero_asiento].config(image=img_seleccionada)

# Función para confirmar selección visual
def confirmar_seleccion():
    if asientos_seleccionados:
        seleccion = ", ".join(str(a) for a in asientos_seleccionados)
        messagebox.showinfo("Confirmación", f"Asientos seleccionados: {seleccion}")
    else:
        messagebox.showwarning("Advertencia", "No has seleccionado ningún asiento.")

# Función para asignar asientos a un correo
def asignar_asientos():
    correo = entrada_correo.get().strip()
    if not correo:
        messagebox.showwarning("Error", "Ingresa un correo electrónico.")
        return

    if correo in usuarios:
        if asientos_seleccionados:
            seleccion = ", ".join(str(a) for a in asientos_seleccionados)
            messagebox.showinfo("Éxito", f"Asientos {seleccion} asignados a {correo}.")
            # Limpiar selección
            for a in asientos_seleccionados:
                botones[a].config(state="disabled")  # Deshabilitar asiento
            asientos_seleccionados.clear()
        else:
            messagebox.showwarning("Advertencia", "Primero selecciona uno o más asientos.")
    else:
        messagebox.showerror("Usuario no encontrado", f"El correo {correo} no está registrado.")

# Crear los botones de asientos
fila = 0
columna = 0
for i in range(1, 21):
    btn = tk.Button(ventana, image=img_libre, command=lambda n=i: seleccionar_asiento(n), bd=0)
    btn.grid(row=fila, column=columna, padx=10, pady=10)
    botones[i] = btn
    columna += 1
    if columna == 5:
        columna = 0
        fila += 1

# Entrada de correo
label_correo = tk.Label(ventana, text="Buscar usuario por correo:")
label_correo.grid(row=5, column=0, columnspan=5, pady=(20, 5))

entrada_correo = tk.Entry(ventana, width=40)
entrada_correo.grid(row=6, column=0, columnspan=5, pady=5)

# Botón de asignar
btn_asignar = tk.Button(ventana, text="Asignar asientos al usuario", command=asignar_asientos, bg="green", fg="white")
btn_asignar.grid(row=7, column=0, columnspan=5, pady=10)

# Botón de confirmar visualmente
btn_confirmar = tk.Button(ventana, text="Ver asientos seleccionados", command=confirmar_seleccion, bg="blue", fg="white")
btn_confirmar.grid(row=8, column=0, columnspan=5, pady=5)

ventana.mainloop()
