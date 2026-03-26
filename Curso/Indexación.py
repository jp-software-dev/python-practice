name = 'Pepe SMITH!'

#if name[0].islower():
#    name = name.capitalize() #Cambia letras de minusculas a mayusculas

first_name = name[:4].upper() #Se espesifica un rango para aceder a mi 1 nombre y convertimos a mayusculas
last_name = name[5:].lower() #Se espesifica un rango para aceder a mi apellido y convertimos a mayusculas
last_character = name[-1] #Imprime el ultimo caracter

print(first_name) 
print(last_name)
print(last_character)