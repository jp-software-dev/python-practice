from PIL import Image, ImageFilter
import os

def menu_editor():
    print("\n--- Editor de Imagenes Basico ---")
    # Pedimos la ruta de la imagen. Al estar en Windows, puedes usar el nombre directo si esta en la misma carpeta
    ruta = input("Ingresa el nombre o ruta de la imagen (ej. foto.jpg): ").strip()
    
    # Validacion basica: comprobamos que el archivo realmente exista antes de intentar abrirlo
    if not os.path.exists(ruta):
        print("[-] Error: La imagen no existe o la ruta es incorrecta.")
        return

    try:
        # Cargamos la imagen en la memoria usando PIL
        img = Image.open(ruta)
        # Mostramos propiedades utiles de la imagen extraidas de sus metadatos
        print(f"[+] Imagen cargada exitosamente: Formato {img.format} | Tamano {img.size}")
    except Exception as e:
        # Capturamos cualquier error (ej. si el usuario intenta abrir un .txt en vez de una imagen)
        print(f"[-] Error al abrir el archivo: {e}")
        return

    # Bucle infinito para permitir aplicar multiples filtros uno tras otro
    while True:
        print("\n--- Menu de Edicion ---")
        print("1. Convertir a Blanco y Negro")
        print("2. Aplicar Filtro de Desenfoque (Blur)")
        print("3. Redimensionar Imagen")
        print("4. Guardar y Salir")
        
        opcion = input("Elige una opcion (1-4): ").strip()
        
        if opcion == '1':
            # .convert("L") cambia el modo de color a Luminancia (escala de grises)
            img = img.convert("L")
            print("[+] Filtro Blanco y Negro aplicado.")
            
        elif opcion == '2':
            # Aplicamos un filtro predefinido de Pillow para difuminar la imagen
            img = img.filter(ImageFilter.BLUR)
            print("[+] Filtro de Desenfoque aplicado.")
            
        elif opcion == '3':
            try:
                # El redimensionado exige que le pasemos una tupla de valores (ancho, alto) en enteros
                ancho = int(input("Ingresa el nuevo ancho en pixeles: "))
                alto = int(input("Ingresa el nuevo alto en pixeles: "))
                
                # .resize modifica la matriz de pixeles a la nueva resolucion
                img = img.resize((ancho, alto))
                print(f"[+] Imagen redimensionada a {ancho}x{alto} pixeles.")
            except ValueError:
                print("[-] Error: Las medidas deben ser numeros enteros.")
                
        elif opcion == '4':
            nombre_salida = input("Ingresa el nombre para guardar la imagen (ej. final.jpg): ").strip()
            
            # Si el usuario solo presiona Enter sin escribir nombre, le asignamos uno por defecto
            if not nombre_salida:
                nombre_salida = "imagen_editada.jpg"
                
            # Renderizamos y guardamos el archivo final en el disco duro de Windows
            img.save(nombre_salida)
            print(f"[+] Imagen guardada correctamente como '{nombre_salida}'. ¡Hasta luego!")
            # Rompemos el bucle para terminar el programa
            break
            
        else:
            print("[-] Opcion no valida.")

# Punto de entrada estandar del script
if __name__ == "__main__":
    menu_editor()