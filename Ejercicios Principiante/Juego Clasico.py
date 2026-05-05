import random

def jugar():
    
    opciones = ['piedra', 'papel', 'tijera']
    puntuacion_usuario = 0
    puntuacion_pc = 0

    while True:
        jugada_usuario = input("\nElige piedra, papel o tijera: ").lower().strip()

        if jugada_usuario == 'salir':
            print("--- Marcador Final ---")
            print(f"Tú {puntuacion_usuario} | Computadora {puntuacion_pc}")
            break

        if jugada_usuario not in opciones:
            print("Entrada no válida. Por favor, escribe 'piedra', 'papel' o 'tijera'.")
            continue

        jugada_pc = random.choice(opciones)
        print(f"La computadora eligio: {jugada_pc}")

        if jugada_usuario == jugada_pc:
            print("Empate")
        elif(jugada_usuario == 'piedra' and jugada_pc == 'tijera') or \
            (jugada_usuario == 'papel' and jugada_pc == 'piedra') or \
            (jugada_usuario == 'tijera' and jugada_pc == 'papel'):
            print("Ganaste la ronda")
            puntuacion_usuario += 1
        else:
            print("La computadora gana esta ronda")
            puntuacion_pc += 1

if __name__ == "__main__":
    jugar()