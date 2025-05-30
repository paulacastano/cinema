import json
from faker import Faker
import sys
import uuid
import random

movies = []

def generar_titulo_pelicula():
    adjetivo = Faker().word(ext_word_list=[
        "oscuro", "brillante", "secreto", "perdido", "maldito", "eterno", "imposible", "legendario"
    ])
    sustantivo = Faker().word(ext_word_list=[
        "destino", "venganza", "amor", "misterio", "guerra", "aventura", "profecía", "viaje"
    ])
    nombre = Faker().first_name()
    lugar = Faker().city()

    estructuras = [
        f"{adjetivo.capitalize()} {sustantivo.capitalize()}",
        f"El {sustantivo.capitalize()} de {nombre}",
        f"{sustantivo.capitalize()} en {lugar}",
        f"{adjetivo.capitalize()} {nombre}",
        f"{sustantivo.capitalize()} sin retorno",
    ]

    return random.choice(estructuras)

if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
        for i in range(num):
            movie = {
                "_id": str(uuid.uuid4()),
                "title": generar_titulo_pelicula(),
                "duration": Faker().random_int(min=60, max=180),
                "genres": Faker().random_elements(
                    elements=["Accion", "Aventura", "Comedia", "Drama", "Terror", "Ciencia Ficcion", "Romance"],
                    length=1
                ),
            }
            movies.append(movie)
        with open("movies.json", "w") as f:
            f.write(json.dumps(movies, indent=4))
    except ValueError:
        print("Argument is not a valid integer.")
else:
    print("No integer argument provided.")
