Food = ['Pizza', 'Pasta', 'Burger', 'Patatoes', 'Hot Dog', 2, 5.0, False]
Food[0] = "Ice cream"

Food.append('Sushi') #Agrega valores al final de la lista
Food.remove('Burger') #Omite elementos de la lista
Food.pop() #Eliina el ultimo elemento de la lista
Food.insert(0, "Cake") #Añade valores a la lista con su debida cordenada
Food.sort() #Acomoda la lista alfabeticamente
Food.clear() #Limpia la lisat completa

for x in Food:
    print(x)