"""
Clase 1 - 16 de junio
Introduccion a FastApi: primer servidor "Hola Mundo".

Comó Correr este archivo:
    1. Activar tu entorno Virtual.
    2. Ejecuta FastApi dev main.py
    3. Abre el navegador: http://localhost:8000
    4. Documentación automatica: http//localhost:800/docs    
"""
from fastapi import FastAPI

app = FastAPI(
    title="Mi primer API",
    description="API de ejemplo para la clase 1 del curso de FastApi.",
    version="0.1.0"
)

@app.get("/")
async def raiz():
    return{"mensaje": "Hola Mundo Desde FastAPI"}

@app.get("/Saludo")
async def saludo():
    return{"mensaje": "Bienvenidos al curso de FastAPI", "Clase": 1}