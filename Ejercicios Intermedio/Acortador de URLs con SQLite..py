import sqlite3
import random
import string

def inicializar_bd():
    conexion = sqlite3.connect("acortador.db")
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS enlaces
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       url_original TEXT NOT NULL,
                       url_corta TEXT NOT NULL UNIQUE)''')
    conexion.commit()
    return conexion

def generar_codigo():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(6))

def menu_acortador():
    conexion = inicializar_bd()
    cursor = conexion.cursor()

    while True:
        print("\n--- Acortador de URLs con SQLite ---")
        print("1. Acortar una nueva URL")
        print("2. Ver mis URLs guardadas")
        print("3. Salir")
        
        opcion = input("Elige una opcion (1-3): ").strip()

        if opcion == "1":
            original = input("Ingresa la URL completa (ej. https://github.com): ").strip()
            if not original:
                print("Error: La URL no puede estar vacia.")
                continue

            codigo = generar_codigo()
            
            try:
                cursor.execute("INSERT INTO enlaces (url_original, url_corta) VALUES (?, ?)", 
                               (original, codigo))
                conexion.commit()
                print(f"\n¡Exito! Tu URL acortada es: http://mi.link/{codigo}")
            except sqlite3.Error as e:
                print(f"\nError al guardar en la base de datos: {e}")

        elif opcion == "2":
            cursor.execute("SELECT id, url_original, url_corta FROM enlaces")
            registros = cursor.fetchall()

            if not registros:
                print("\nAun no tienes URLs guardadas.")
            else:
                print("\n--- Historial de URLs ---")
                for registro in registros:
                    print(f"[{registro[0]}] Original: {registro[1]} -> Corta: http://mi.link/{registro[2]}")

        elif opcion == "3":
            print("Cerrando la base de datos... ¡Hasta luego!")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")

    conexion.close()

if __name__ == "__main__":
    menu_acortador()