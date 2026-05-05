# Importar la libreria requests para hacer peticiones a servidores web en internet
import requests

def notificar_clima():
    # Solicitar al usuario la ciudad y eliminar espacios en blanco a los lados
    ciudad = input("Ingresa el nombre de la ciudad para ver su clima: ").strip()
    
    # Validar que el usuario no haya dejado el texto en blanco al presionar Enter
    if not ciudad:
        # Mostrar mensaje de error y terminar la ejecucion de la funcion
        print("No ingresaste ninguna ciudad.")
        return
        
    # Construir la URL del servicio wttr.in solicitando la respuesta en formato JSON (?format=j1)
    url = f"https://wttr.in/{ciudad}?format=j1"
    
    # Iniciar el bloque try para manejar posibles errores de red o falta de internet
    try:
        print(f"Buscando el clima actual en {ciudad}...")
        
        # Ejecutar la peticion GET para descargar la informacion del servidor
        respuesta = requests.get(url)
        
        # Comprobar si la conexion fue exitosa verificando el codigo HTTP 200 (OK)
        if respuesta.status_code == 200:
            # Convertir el texto recibido del servidor a un diccionario de Python
            datos = respuesta.json()
            
            # Extraer la temperatura navegando por las llaves del diccionario JSON
            temperatura = datos['current_condition'][0]['temp_C']
            
            # Extraer la descripcion del clima desde otra seccion del diccionario
            descripcion = datos['current_condition'][0]['weatherDesc'][0]['value']
            
            # Imprimir los datos extraidos de forma limpia en la terminal
            print("\nReporte del Clima:")
            print(f"Ciudad: {ciudad.capitalize()}")
            print(f"Temperatura: {temperatura} grados Celsius")
            print(f"Condicion: {descripcion}")
            
        else:
            # Mostrar error si el servidor responde pero la ciudad no existe (ej. error 404)
            print("\nNo se pudo encontrar el clima para esa ciudad.")
            print("Verifica que el nombre este escrito correctamente.")
            
    # Capturar el error especifico si la computadora no logra conectarse a internet
    except requests.exceptions.RequestException:
        print("\nError de conexion. Verifica tu internet e intenta de nuevo.")

# Punto de entrada principal para asegurar que el codigo corra directamente
if __name__ == "__main__":
    notificar_clima()