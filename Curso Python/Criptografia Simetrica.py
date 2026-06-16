# Juan Pablo Mercado Arizmendi

from tkinter import N

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    
    for caracter in texto:
        
        if caracter.isalpha():
            inicio = ord('A') if caracter.isupper() else ord('a')
            nueva_posicion = (ord(caracter) - inicio + desplazamiento) % 26
            letra_cifrada = chr(inicio + nueva_posicion)
            resultado += letra_cifrada

        elif caracter.isdigit():
            inicio_num = ord('0')
            numero_posicion = (ord(caracter) - inicio_num + desplazamiento) % 10
            numero_cifrado = chr(inicio_num + numero_posicion)
            resultado += numero_cifrado
        else:
            resultado += caracter     

    return resultado

frase = input("Ingresa la frase que deseas cifrar: ")
try:
    salto = int(input("Ingresa el número de espacios para el desplazamiento: "))
    resultado = cifrado_cesar(frase, salto)

    print(f"Frase original: {frase}")
    print(f"Resultado:      {resultado}")

except ValueError:
    print("Error: El número de espacios debe ser un valor entero.")