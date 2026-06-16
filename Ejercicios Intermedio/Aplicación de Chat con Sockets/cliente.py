import socket
import threading

def recibir_mensajes(cliente):
    # Este bucle corre en un hilo separado para escuchar constantemente al servidor
    while True:
        try:
            # Recibimos los bytes del servidor y los decodificamos a texto (utf-8)
            mensaje = cliente.recv(1024).decode('utf-8')
            if mensaje:
                print(f"\n{mensaje}")
        except:
            # Si hay error (servidor caido), avisamos y cerramos
            print("\nError de conexion con el servidor.")
            cliente.close()
            break

def iniciar_cliente():
    # Debe coincidir exactamente con los datos del servidor
    host = '127.0.0.1'
    puerto = 5555
    nombre = input("Ingresa tu nombre de usuario: ")

    # Preparamos el socket del cliente
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Intentamos hacer la conexion fisica al servidor
        cliente.connect((host, puerto))
        print("Conectado al chat. (Escribe 'salir' para abandonar)")
    except:
        print("No se pudo conectar al servidor. ¿Esta encendido?")
        return

    # Iniciamos un hilo dedicado EXCLUSIVAMENTE a recibir mensajes
    # Si no hacemos esto, input() bloquearia el codigo y no podriamos leer mensajes nuevos 
    # hasta que enviaramos uno.
    hilo_recibir = threading.Thread(target=recibir_mensajes, args=(cliente,))
    hilo_recibir.start()

    # El bucle principal (el hilo original) se dedica EXCLUSIVAMENTE a enviar mensajes
    while True:
        mensaje = input("Tu: ")
        
        # Comando para desconectarse limpiamente
        if mensaje.lower() == 'salir':
            cliente.close()
            break
            
        # Formateamos el mensaje con el nombre y lo pasamos a bytes (encode) antes de enviarlo
        mensaje_formateado = f"{nombre}: {mensaje}"
        cliente.send(mensaje_formateado.encode('utf-8'))

if __name__ == "__main__":
    iniciar_cliente()