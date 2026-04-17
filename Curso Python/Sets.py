utensilios = {"Tenedor", "Cuchara", "Cuchillo"}
platos = {"Plato", "Bol", "Taza", "Cuchillo"}

utensilios.add("Plato") #Agrega elementos a utensilios
utensilios.remove("Tenedor") #Remueve elementos de utensilios
utensilios.pop() #Elimina uun valor al asar
utensilios.clear() #Sirve para eliminar(limpiar) todos los valores
utensilios.update(platos) #Junta ambas listas

for x in utensilios:
    print(x)

print(utensilios.difference(platos)) #Omite elementos que se repiten en ambas listas
print(utensilios.intersection(platos)) #Nos regresa los valores repetidos en ambas listas