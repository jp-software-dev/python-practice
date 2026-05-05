def verificar_palidromo():
    # Solicita al usuario que ingrese una palabra o frase
    texto_original = input("Ingrese una palabra o frase: ")

    # Valida que el usuario haya ingresado un texto
    if not texto_original:
        # Manda un mensaje de error si no se ha ingresado ningún texto
        print("No se ha ingresado ningún texto.")
        return
    
    # Elimina espacios y convierte a minúsculas para la comparación
    texto_limpio = texto_original.lower().replace(" ", "")
    
    # Invierte el texto limpio para compararlo con el original
    texto_invertido = texto_limpio[::-1]

    # Compara si el texto es o no un palíndromo
    if texto_limpio == texto_invertido:
        print(f'\nEl texto "{texto_original}" es un palíndromo.')
    else:
        print(f'\nEl texto "{texto_original}" no es un palíndromo.')

# Punto de entrada del programa
if __name__ == "__main__":
    verificar_palidromo()