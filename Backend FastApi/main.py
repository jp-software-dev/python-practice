"""
Clase 1 - 16 de junio
Introducción a FastAPI: primer servidor "Hola Mundo"

Cómo correr este archivo:
    1. Activa tu entorno virtual.
    2. Ejecuta: fastapi dev main.py
    3. Abre en el navegador: http://localhost:8000
    4. Documentación automática: http://localhost:8000/docs
"""

from fastapi import FastAPI

app = FastAPI(
    title="Mi primer API",
    description="API de ejemplo para la clase 1 del curso de FastAPI.",
    version="0.1.0",
)

productos = [
    {"id": 1, "nombre": "Espresso", "precio": 35.0},
    {"id": 2, "nombre": "Capuchino", "precio": 45.0},
    {"id": 3, "nombre": "Latte", "precio": 50.0}
]

clientes = [
    {"id": 1, "nombre": "Ana López", "email": "ana.lopez@email.com"},
    {"id": 2, "nombre": "Carlos Pérez", "email": "carlos.perez@email.com"},
    {"id": 3, "nombre": "María Gómez", "email": "maria.gomez@email.com"},
    {"id": 4, "nombre": "Jorge Ruiz", "email": "jorge.ruiz@email.com"},
    {"id": 5, "nombre": "Lucía Fernández", "email": "lucia.fernandez@email.com"}
]

# Ruta raíz
@app.get("/")
async def raiz():
    return {"mensaje": "¡Hola Mundo desde FastAPI!"}

# Saludo
@app.get("/saludo")
async def saludo():
    return {
        "mensaje": "Bienvenidos al curso de FastAPI",
        "clase": 1
    }

# Despedida
@app.get("/despedida")
async def despedida():
    return {
        "mensaje": "Bye.",
        "clase": 1
    }

# Mostrar todos los productos
@app.get("/menu")
async def ver_menu():
    return {"menu": productos}

# Mostrar un producto por ID
@app.get("/menu/{product_id}")
async def ver_producto(product_id: int):

    for producto in productos:
        if producto["id"] == product_id:
            return producto
        
    return {"error": "Producto no encontrado"}

# Buscar productos por precio 
@app.get("/buscar/{precio}")
async def buscar(precio: float):
    resultado = []

    for producto in productos:
        if producto["precio"] <= precio:
            resultado.append(producto)

    return {"productos": resultado}

# Buscar clientes por ID
@app.get("/clientes/{cliente_id}")
async def ver_clientes(cliente_id: int):

    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return cliente
    
    return {"error": "Cliente no encontrado"}