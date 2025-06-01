from reportlab.lib.pagesizes import A7
from reportlab.pdfgen import canvas
from movies.movies_db import get_movie_by_id
from rooms.room_db import get_room_by_id
from reportlab.lib.units import mm

def generar_recibo_pdf(correo, asientos, pelicula, sala, funcion, date, price):
    nombre_archivo = f"recibo_{correo.replace('@', '_at_')}.pdf"
    amount = price * len(asientos)  # Assuming price is per seat
    movie = get_movie_by_id(pelicula)
    room = get_room_by_id(sala)
    if not room:
        raise ValueError("Sala no encontrada")

    if not movie:
        raise ValueError("Película no encontrada")
    
    c = canvas.Canvas(nombre_archivo, pagesize=A7)
    
    
    text = c.beginText(5 * mm, A7[1] - 10 * mm)
    text.setFont("Helvetica", 10)

    text.textLine("================================")
    text.textLine("          RECIBO DE COMPRA      ")
    text.textLine("              TU CINE           ")
    text.textLine("================================")
    text.textLine("")
    text.textLine(f"Correo del usuario: {correo}")
    text.textLine(f"Asientos: {', '.join(map(str, asientos))}")
    text.textLine(f"Película: {movie['title']}")
    text.textLine(f"Sala: {room['name']}")
    # text.textLine(f"Número de función: {funcion}")
    text.textLine(f"Fecha y hora: {date}")
    text.textLine(f"Total: ${amount}")
    text.textLine("")
    text.textLine("¡Gracias por tu compra!")

    c.drawText(text)
    c.save()

    return nombre_archivo