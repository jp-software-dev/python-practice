# Importar el modulo random para elegir una palabra al azar
import random

def jugar_ahorcado():
    # Definir una lista de palabras ocultas para el juego
    palabras = ["python", "programacion", "teclado", "pantalla", "desarrollo"]
    
    # Elegir una palabra aleatoria de la lista
    palabra_secreta = random.choice(palabras)
    
    # Crear un conjunto (set) vacio para guardar las letras que el usuario adivina
    letras_adivinadas = set()
    
    # Definir la cantidad de errores permitidos antes de perder
    intentos_restantes = 6
    
    print("Bienvenido al Juego del Ahorcado!")
    
    # Iniciar el bucle principal del juego que continuara mientras queden intentos
    while intentos_restantes > 0:
        # Crear una lista con las letras adivinadas o guiones bajos para las letras ocultas
        estado_palabra = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        
        # Unir la lista en un texto separado por espacios y mostrarlo al usuario
        print("\nPalabra:", " ".join(estado_palabra))
        print(f"Intentos restantes: {intentos_restantes}")
        
        # Comprobar si ya no hay guiones bajos, lo que significa que gano el juego
        if "_" not in estado_palabra:
            print(f"\nFelicidades Adivinaste la palabra: {palabra_secreta}")
            # Salir de la funcion porque el juego termino con victoria
            return
            
        # Pedir al usuario una letra, quitar espacios y convertir a minuscula
        letra_usuario = input("Ingresa una letra: ").strip().lower()
        
        # Validar que el usuario ingrese exactamente una sola letra (que no mande palabras completas ni numeros)
        if len(letra_usuario) != 1 or not letra_usuario.isalpha():
            print("Por favor, ingresa solo una letra valida.")
            # Volver al inicio del bucle sin restar intentos usando continue
            continue
            
        # Validar si el usuario ya habia ingresado esa letra antes
        if letra_usuario in letras_adivinadas:
            print("Ya intentaste con esa letra. Prueba con otra.")
            continue
            
        # Agregar la letra nueva al conjunto de letras adivinadas
        letras_adivinadas.add(letra_usuario)
        
        # Evaluar si la letra ingresada NO esta dentro de la palabra secreta
        if letra_usuario not in palabra_secreta:
            # Restar un intento al contador si la letra es incorrecta
            intentos_restantes -= 1
            print("Letra incorrecta.")
            
    # Si el bucle termina porque los intentos llegan a 0, mostrar mensaje de derrota
    print(f"\nPerdiste! Te quedaste sin intentos. La palabra era: {palabra_secreta}")

# Punto de entrada para ejecutar el juego directamente
if __name__ == "__main__":
    jugar_ahorcado()