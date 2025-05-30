from tkinter import Toplevel, messagebox, Button, Label, Entry
from PIL import Image, ImageTk
from users.users_db import get_user_by_email
from shows.shows_db import get_show_by_id
from booking.booking_db import create_bookings, get_bookings_by_show_id
from booking.generate_recipe import generar_recibo_pdf
import uuid
import os
import platform

asientos_seleccionados = []
botones = {}

def open_room_screen(show_id):
    """
    Opens the room screen.
    """
    # Cargar imágenes (usa PIL para mejor compatibilidad)
    img_libre = ImageTk.PhotoImage(Image.open("silla-libre.png").resize((40, 40)))
    img_seleccionada = ImageTk.PhotoImage(Image.open("silla-seleccionada.png").resize((40, 40)))

    def create_booking(user_id, chair_id, date, time_slot, price, room_id):
        return {
            "_id": str(uuid.uuid4()),
            "userId": user_id,
            "showId": show_id,
            "roomId": room_id,
            "chairId": chair_id,
            "date": date,
            "timeSlot": time_slot,
            "amount": price
        }

    # Función para asignar asientos a un correo
    def asignar_asientos():
        correo = entrada_correo.get().strip()
        if not correo:
            messagebox.showwarning("Error", "Ingresa un correo electrónico.")
            return

        user = get_user_by_email(correo)
        if not user:
            messagebox.showerror("Usuario no encontrado", f"El correo {correo} no está registrado.")
            return
        else:
            if asientos_seleccionados:
                seleccion = ", ".join(str(a) for a in asientos_seleccionados)
                show = get_show_by_id(show_id)
                bookings = []
                for a in asientos_seleccionados:
                    # Aquí podrías guardar la reserva en la base de datos
                    bookings.append(create_booking(user["_id"], a, show["date"], show["timeSlot"], show["price"], show["roomId"]))
                messagebox.showinfo("Confirmación", f"Asientos seleccionados: {seleccion}")
                
                # Limpiar selección
                for a in asientos_seleccionados:
                    botones[a].config(state="disabled")  # Deshabilitar asiento
                create_bookings(bookings)

                show_date = show["date"] + "-" + show["timeSlot"]

                nombre_recibo = generar_recibo_pdf(
                    user["email"],
                    asientos_seleccionados,
                    show["movieId"],
                    show["roomId"],
                    show_id,
                    f"{show_date}",
                    show["price"]
                )
                asientos_seleccionados.clear()
                if platform.system() == "Windows":
                    os.startfile(nombre_recibo)
                room_screen.destroy()
            else:
                messagebox.showwarning("Advertencia", "Primero selecciona uno o más asientos.")

    def seleccionar_asiento(numero_asiento):
        if numero_asiento in asientos_seleccionados:
            asientos_seleccionados.remove(numero_asiento)
            botones[numero_asiento].config(image=img_libre)
        else:
            asientos_seleccionados.append(numero_asiento)
            botones[numero_asiento].config(image=img_seleccionada)
    
    room_screen = Toplevel()
    room_screen.title("Sala de Cine")
    room_screen.geometry("310x400")
    room_screen.configure(bg="#f0f0f0")

    # Crear botones con icono de silla
    fila = 0
    columna = 0
    for i in range(1, 21):
        btn = Button(room_screen, image=img_libre, command=lambda n=i: seleccionar_asiento(n), bd=0)
        btn.grid(row=fila, column=columna, padx=10, pady=10)
        botones[i] = btn
        columna += 1
        if columna == 5:
            columna = 0
            fila += 1
    
    bookings = get_bookings_by_show_id(show_id)
    booking_asientos = [booking["chairId"] for booking in bookings]
    for a in booking_asientos:
        botones[a].config(state="disabled")

    # Entrada de correo
    label_correo = Label(room_screen, text="Buscar usuario por correo:")
    label_correo.grid(row=5, column=0, columnspan=5, pady=(20, 5))

    entrada_correo = Entry(room_screen, width=40)
    entrada_correo.grid(row=6, column=0, columnspan=5, pady=5)

    # Botón de asignar
    btn_asignar = Button(room_screen, text="Asignar asientos al usuario", command=asignar_asientos, fg="black")
    btn_asignar.grid(row=7, column=0, columnspan=5, pady=10)

    