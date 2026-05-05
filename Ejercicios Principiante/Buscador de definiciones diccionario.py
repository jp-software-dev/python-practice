# Importamos la libreria requests para poder hacer peticiones a servidores en internet
import requests

def buscar_definicion():
    # 1. Pedimos al usuario la palabra que desea buscar y la guardamos en la variable 'palabra'
    palabra = input("Ingrese la palabra que desea buscar: ")

    # 2. Validamos que el usuario no haya presionado 'Enter' dejando el espacio en blanco
    if not palabra:
        print("No ingresaste ninguna palabra, intentalo de nuevo.")
        # 'return' detiene la ejecucion de la funcion aqui mismo para no continuar con el error
        return
    
    # 3. Construimos la URL de la API.
    # se uso una f-string (f"...") para inyectar la variable 'palabra' al final de la direccion.
    # se uso /en/ para consultar la base de datos en ingles.
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{palabra}"

    # 4. Iniciamos el bloque try para intentar ejecutar el codigo que depende de internet
    try:
        print("Buscando en el diccionario...")

        # 5. Hacemos la peticion 'GET' a la URL. Es el equivalente a abrir la pagina web.
        respuesta = requests.get(url)

        # 6. Verificamos si la respuesta del servidor es 200 (que significa Exito)
        if respuesta.status_code == 200:
            
            # 7. Convertimos la informacion recibida a formato JSON (listas y diccionarios de Python)
            datos = respuesta.json()
            
            # 8. Extraemos la definicion exacta navegando por la estructura de datos:
            definicion = datos[0]['meanings'][0]['definitions'][0]['definition']

            # 9. Mostramos la informacion estructurada al usuario
            print("\nResultado encontrado.")
            print(f"Palabra: {palabra}")
            print(f"Definición: {definicion}")
            
        # 10. Si el status_code NO es 200 (por ejemplo es 404), entramos al 'else'
        else: 
            print("\nNo se encontro una definicion para la palabra ingresada.")
            print("Verifica que la palabra este escrita correctamente o intenta con otra palabra.")
    
    # 11. Este bloque 'except' solo se activa si la peticion falla por completo 
    except requests.exceptions.RequestException:
        print("\nError de conexion. Revisa tu conexion a internet.")

# 12. Validamos que este script se este ejecutando directamente y no importando desde otro archivo
if __name__ == "__main__":
    buscar_definicion()