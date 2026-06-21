import sqlite3  # Libreria nativa de Python para bases de datos locales ligeras
import random   # Para seleccionar caracteres al azar
import string   # Para obtener facilmente todas las letras y numeros

def inicializar_db():
    # Se conecta al archivo 'urls.db'. Si no existe, lo crea automaticamente.
    conexion = sqlite3.connect('urls.db')
    cursor = conexion.cursor()
    
    # Creamos la tabla 'enlaces' solo si no existe en el archivo
    # Usamos UNIQUE en url_corta para que el sistema rechace duplicados por seguridad
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enlaces (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url_original TEXT NOT NULL,
            url_corta TEXT NOT NULL UNIQUE
        )
    ''')
    conexion.commit() # Guardamos los cambios estructurales
    return conexion

def generar_codigo_corto(longitud=6):
    # string.ascii_letters incluye a-z y A-Z. string.digits incluye 0-9
    caracteres = string.ascii_letters + string.digits
    # Selecciona un caracter aleatorio 6 veces y los une en un solo texto
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def acortar_url(conexion, url_original):
    cursor = conexion.cursor()
    
    # Primero consultamos si el usuario ya habia guardado esta misma URL antes
    cursor.execute("SELECT url_corta FROM enlaces WHERE url_original = ?", (url_original,))
    resultado = cursor.fetchone() # Extrae un solo registro si lo encuentra

    if resultado:
        print(f"\n[!] Esta URL ya estaba acortada: bit.ly/{resultado[0]}")
        return

    # Si la URL es nueva, generamos su codigo
    url_corta = generar_codigo_corto()
    
    try:
        # Insertamos el nuevo registro usando consultas parametrizadas (?) para evitar inyecciones SQL
        cursor.execute("INSERT INTO enlaces (url_original, url_corta) VALUES (?, ?)", (url_original, url_corta))
        conexion.commit() # Guardamos los cambios en el disco duro
        print(f"\n[+] URL acortada con exito: bit.ly/{url_corta}")
    except sqlite3.IntegrityError:
        # Si por alguna casualidad extrema el codigo generado ya existia (violando el UNIQUE), 
        # llamamos a la funcion de nuevo para que genere otro diferente
        acortar_url(conexion, url_original)

def ver_urls(conexion):
    cursor = conexion.cursor()
    # Obtenemos absolutamente todo lo guardado en la tabla
    cursor.execute("SELECT url_original, url_corta FROM enlaces")
    registros = cursor.fetchall() # Extrae todos los resultados como una lista de tuplas
    
    print("\n--- URLs Guardadas ---")
    if not registros:
        print("La base de datos esta vacia.")
    else:
        # Desempaquetamos la tupla directamente en el bucle for
        for original, corta in registros:
            print(f"bit.ly/{corta} -> {original}")
    print("----------------------")

def menu():
    conexion = inicializar_db() # Arrancamos la DB antes de entrar al menu
    
    while True:
        print("\n--- ACORTADOR DE URLs (SQLite) ---")
        print("1. Acortar una nueva URL")
        print("2. Ver todas las URLs acortadas")
        print("3. Salir")
        
        opcion = input("Elige una opcion (1-3): ").strip()
        
        if opcion == '1':
            url = input("Ingresa la URL original (ej. https://ejemplo.com): ").strip()
            if url:
                acortar_url(conexion, url)
        elif opcion == '2':
            ver_urls(conexion)
        elif opcion == '3':
            # Es buena practica cerrar la conexion a la base de datos al terminar
            print("Cerrando la base de datos... ¡Hasta luego!")
            conexion.close()
            break
        else:
            print("[-] Opcion no valida.")

# Punto de entrada estandar
if __name__ == "__main__":
    menu()