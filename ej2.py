#1.
frutas = ["frutilla","banan","manzana"]

frutas.append("Pera")
frutas.append("Durazno")
frutas.sort() #Alfabéticamente
print(frutas)
frutas.pop(0) #Elimina el elemento de la primer posición
print(frutas)

#2.
ciudades = ("Buenos Aires", "Roma")
print("Primer elemento: ", ciudades[0])
print("Último elemento: ", ciudades[-1])

listaCiudades = list(ciudades)
print(listaCiudades)

#3.
comida = ["Milanesa","Fideos","Asado","Pizza"]
comidaUpper = []
for elemento in comida:
    comidaUpper.append(elemento.upper())