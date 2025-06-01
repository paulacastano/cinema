# COMANDOS

- Desactiva ambiente virtual

```shell
deactivate
```

# INICIALIZAR EL PROYECTO

## REQUISITOS

- Python 3.10 o superior
- Docker desktop

## COMO EJECUTAR

Crear el contenedor con la base de datos

```shell
docker-compose up --build
```

Crear un ambiente virtual con el comando

```shell
python -m venv .venv
```

Activa ambiente virtual

```shell
.venv\Scripts\Activate.ps1
```

Se recomienda ejecutar los comandos para generar datos en el sistema

1. Ingrese a la carpeta de migraciones

```shell
cd ./migrations
```

2. Ejecute el script para generar las movies y los shows

```shell
python ./generate_movies.py [number-of-movies]
python ./generate_shows.py [number-of-shows]
```

Regrese a la carpeta raiz (`cd ..`) y ejecute la applicacion mediante el comando

```shell
python main.py
```
