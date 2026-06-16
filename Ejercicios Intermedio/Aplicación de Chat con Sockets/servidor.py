# 'socket' es la base de las conexiones de red (TCP/IP)
import socket
# 'threading' nos permite manejar multiples clientes al mismo tiempo (multitarea)
import threading

def manejar_cliente(cliente, direccion, clientes):
    print(f"[+] Nueva conexion: {direccion}")
    # Bucle infinito para escuchar los mensajes de este cliente en especifico
    while True:
        try:
            # Recibimos hasta 1024 bytes de informacion del cliente
            mensaje = cliente.recv(1024)
            # Si el mensaje esta vacio, significa que el cliente se desconecto
            if not mensaje:
                break
                
            # Broadcast: Enviamos el mensaje recibido a todos los demas clientes conectados
            for c in clientes:
                if c != cliente:
                    c.send(mensaje)
        except:
            # Si ocurre un error (ej. el cliente cierra la ventana de golpe), salimos del bucle
            break
            
    # Cuando el bucle termina, limpiamos la conexion
    print(f"[-] Desconectado: {direccion}")
    clientes.remove(cliente)
    cliente.close()

def iniciar_servidor():
    # 127.0.0.1 es la direccion "localhost" (tu propia computadora)
    host = '127.0.0.1'
    # Puerto arbitrario donde el servidor estara "escuchando"
    puerto = 5555
    
    # AF_INET = IPv4 | SOCK_STREAM = Protocolo TCP (seguro y ordenado)
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Asignamos la IP y el puerto al servidor
    servidor.bind((host, puerto))
    # Ponemos al servidor en modo escucha
    servidor.listen()
    print(f"Servidor escuchando en {host}:{puerto}...")

    # Lista para llevar el registro de todas las computadoras conectadas
    clientes = []

    while True:
        # accept() detiene el codigo hasta que alguien se conecta. Devuelve el objeto cliente y su IP
        cliente, direccion = servidor.accept()
        clientes.append(cliente)
        
        # Se creo un "hilo" nuevo. Esto permite que el servidor atienda a este cliente 
        # mientras sigue esperando nuevas conexiones en el bucle principal.
        hilo = threading.Thread(target=manejar_cliente, args=(cliente, direccion, clientes))
        hilo.start()

if __name__ == "__main__":
    iniciar_servidor()