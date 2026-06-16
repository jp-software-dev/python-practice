# Importamos la libreria integrada para manejar bases de datos locales
import sqlite3

def inicializar_bd():
    # Conecta o crea el archivo inventario.db en la misma carpeta local
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    
    # Crea la tabla con restricciones (UNIQUE asegura que no haya dos productos con el mismo nombre)
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nombre TEXT UNIQUE NOT NULL,
                       cantidad INTEGER NOT NULL,
                       precio REAL NOT NULL)''')
    conexion.commit()
    return conexion

def menu_inventario():
    # Establecemos la conexion al arrancar el programa
    conexion = inicializar_bd()
    cursor = conexion.cursor()

    while True:
        print("\n--- Gestor de Inventario ---")
        print("1. Agregar nuevo producto")
        print("2. Ver inventario")
        print("3. Actualizar cantidad de un producto")
        print("4. Salir")
        
        opcion = input("Elige una opcion (1-4): ").strip()

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            # Bloque try/except por si el usuario escribe letras en los campos numericos
            try:
                cantidad = int(input("Cantidad en stock: "))
                precio = float(input("Precio unitario: "))
                
                # Insercion de datos segura usando parametros (?) para evitar inyecciones SQL
                cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)", 
                               (nombre, cantidad, precio))
                conexion.commit()
                print(f"\n[+] '{nombre}' agregado al inventario.")
            except ValueError:
                print("\n[-] Error: La cantidad debe ser entera y el precio decimal/entero.")
            # Capturamos el error especifico si se rompe la regla UNIQUE de la tabla
            except sqlite3.IntegrityError:
                print(f"\n[-] Error: El producto '{nombre}' ya existe en la base de datos.")

        elif opcion == "2":
            # Consulta para traer todos los registros de la tabla
            cursor.execute("SELECT id, nombre, cantidad, precio FROM productos")
            productos = cursor.fetchall()
            
            if not productos:
                print("\nEl inventario esta vacio.")
            else:
                print("\nID | Nombre | Cantidad | Precio")
                print("-" * 40)
                # Recorremos la lista de resultados. 
                # :.2f formatea el precio para que siempre muestre 2 decimales (ej. 15.00)
                for p in productos:
                    print(f"{p[0]} | {p[1]} | {p[2]} | ${p[3]:.2f}")

        elif opcion == "3":
            # Solicitamos el ID porque es la llave primaria, la forma mas exacta de buscar un registro
            id_prod = input("Ingresa el ID del producto a actualizar: ").strip()
            try:
                nueva_cant = int(input("Nueva cantidad total en stock: "))
                
                # Ejecutamos el comando UPDATE para modificar unicamente la columna 'cantidad'
                cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cant, id_prod))
                
                # rowcount nos devuelve cuantas filas se modificaron. Si es 0, el ID no existia.
                if cursor.rowcount > 0:
                    conexion.commit()
                    print("\n[+] Cantidad actualizada correctamente.")
                else:
                    print("\n[-] Error: ID no encontrado en el inventario.")
            except ValueError:
                print("\n[-] Error: La cantidad debe ser un numero entero.")

        elif opcion == "4":
            print("Cerrando conexion a la base de datos... ¡Hasta luego!")
            break
        else:
            print("Opcion no valida.")

    # Buena practica de seguridad y rendimiento: cerrar la base de datos al salir
    conexion.close()

# Punto de entrada del script
if __name__ == "__main__":
    menu_inventario()