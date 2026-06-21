import sqlite3

def conectar_db():
    # Conecta a la DB o la crea si no existe
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    
    # Creamos la tabla 'productos'. Usamos REAL para el precio (admite decimales).
    # UNIQUE en 'nombre' evita que agreguemos dos veces el mismo articulo.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL
        )
    ''')
    conexion.commit()
    return conexion

def agregar_producto(conexion):
    # Guardamos todo en minusculas para evitar duplicados como "Laptop" y "laptop"
    nombre = input("Nombre del producto: ").strip().lower()
    
    # Bloque try-except para evitar que el programa falle si el usuario escribe texto en vez de numeros
    try:
        cantidad = int(input("Cantidad en stock: "))
        precio = float(input("Precio unitario: "))
    except ValueError:
        print("[-] Error: La cantidad debe ser entera y el precio un numero.")
        return

    cursor = conexion.cursor()
    try:
        # Consulta SQL (C - Create)
        cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)", (nombre, cantidad, precio))
        conexion.commit()
        print(f"[+] Producto '{nombre.capitalize()}' agregado con exito.")
    except sqlite3.IntegrityError:
        # Salta si intentamos insertar un nombre que ya existe (violacion de UNIQUE)
        print("[-] Error: Este producto ya existe en el inventario.")

def ver_inventario(conexion):
    cursor = conexion.cursor()
    # Consulta SQL (R - Read)
    cursor.execute("SELECT id, nombre, cantidad, precio FROM productos")
    productos = cursor.fetchall()

    print("\n--- INVENTARIO ACTUAL ---")
    if not productos:
        print("El inventario esta vacio.")
    else:
        # Formateo de tabla para consola
        print(f"{'ID':<5} | {'NOMBRE':<20} | {'CANTIDAD':<10} | {'PRECIO'}")
        print("-" * 55)
        for prod in productos:
            # prod[0] es el ID, prod[1] el nombre, etc.
            print(f"{prod[0]:<5} | {prod[1].capitalize():<20} | {prod[2]:<10} | ${prod[3]:.2f}")
    print("-" * 55)

def actualizar_cantidad(conexion):
    # Mostramos el inventario primero para que el usuario sepa que ID elegir
    ver_inventario(conexion)
    try:
        id_prod = int(input("Ingresa el ID del producto a actualizar: "))
        nueva_cantidad = int(input("Ingresa la nueva cantidad en stock: "))
    except ValueError:
        print("[-] Error: Ingresa valores numericos validos.")
        return

    cursor = conexion.cursor()
    # Consulta SQL (U - Update). Filtramos por el ID unico.
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id_prod))
    
    # rowcount nos dice cuantas filas fueron modificadas. Si es 0, el ID no existia.
    if cursor.rowcount > 0:
        conexion.commit()
        print(f"[+] Cantidad actualizada correctamente.")
    else:
        print("[-] Error: No se encontro ningun producto con ese ID.")

def eliminar_producto(conexion):
    ver_inventario(conexion)
    try:
        id_prod = int(input("Ingresa el ID del producto a eliminar: "))
    except ValueError:
        print("[-] Error: Ingresa un ID numerico valido.")
        return

    cursor = conexion.cursor()
    # Consulta SQL (D - Delete)
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))
    
    if cursor.rowcount > 0:
        conexion.commit()
        print("[+] Producto eliminado del inventario.")
    else:
        print("[-] Error: No se encontro ningun producto con ese ID.")

def menu():
    conexion = conectar_db()
    
    while True:
        print("\n--- GESTOR DE INVENTARIO ---")
        print("1. Agregar nuevo producto (Create)")
        print("2. Ver inventario (Read)")
        print("3. Actualizar stock (Update)")
        print("4. Eliminar producto (Delete)")
        print("5. Salir")
        
        opcion = input("Elige una opcion (1-5): ").strip()
        
        if opcion == '1':
            agregar_producto(conexion)
        elif opcion == '2':
            ver_inventario(conexion)
        elif opcion == '3':
            actualizar_cantidad(conexion)
        elif opcion == '4':
            eliminar_producto(conexion)
        elif opcion == '5':
            print("Cerrando el sistema... ¡Hasta luego!")
            conexion.close()
            break
        else:
            print("[-] Opcion no valida.")

# Punto de entrada
if __name__ == "__main__":
    menu()