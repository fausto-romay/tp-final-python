#1.
conjunto1 = {7,11,6}
conjunto2 = {14,22,5}
union = conjunto1.union(conjunto2)
diferencia = conjunto1.difference(conjunto2)
interseccion = conjunto1.intersection(conjunto2)
print(f"Unión: {union}, Diferencia: {diferencia}, Intersección: {interseccion}")

#2.
diccionario = { "Fausto" : 19, "Paula" : 20, "Maxi" : 21 }
nombre = list(diccionario.keys())[0]
edad = diccionario[nombre]
print(edad)

diccionario["Eze"] = 17
diccionario.pop("Maxi", 21)
print(diccionario)

#3.
productos = { "Galletitas" : 1200, "Alfajor" : 1000, "Yogur" : 500, "Cereal" : 1500, "Coca-Cola" : 2300 }
print(productos["Coca-Cola"])

for producto in productos:
    productos[producto] *= 1.10

print(productos)

#4.
conj1 = {1,2,3,4,5}
conj2 = {4,5,6,7,8}
print(conj1.intersection(conj2))
print(conj1.difference(conj2))