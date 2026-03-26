capitales = {
    'EE.UU': 'Washington D.C',
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago de Chile',
    'Brasil': 'Blasilia',
    'Cursos': ['Python', 'SQL'],
    'Años': 2026
}

capitales.update({'Alemania': 'Berlin'}) #Sirve ara agregar más valores al diccionario
capitales.pop({'EE.UU': 'Washington D.C'}) #Sirve para eliminar valores 
capitales.clear() #Limpia mi diccionario

print(capitales.get('Alemania')) #En caso de que no exita una clave en el diccionario manda un none 
print(capitales.keys()) #Nos trae las llaves de las claves que hay en el diccionario
print(capitales.values()) #Nos trae los Valores que hay en el diccionario
print(capitales.items()) #Nos trae todas las llaves y valores que hay en el diccionario

for key, value in capitales.items():
    print(key, value) #Nos trae todas las llaves y valores que hay en el diccionario en lista