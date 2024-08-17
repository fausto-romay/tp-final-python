#1.
entero = int(input("Ingrese un número: "))
if entero % 2 == 0:
    print("¡Número par!")
else:
    print("¡Número impar!")

#2.
opcion = int(input("Ingrese una opcion: "))
if opcion == 1:
    print("Hola!")
elif opcion == 2:
    print("Chau!")
elif opcion == 3:
    pass
else:
    raise Exception("No existe dicha opcion!")

#3.
numero = int(input("Ingrese número: "))
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Cero")

#4.
for i in range(1, 11):
    print(i)

#5.
numActual = 0
sumaTotal = 0
while numActual != 101:
    numActual += 1
    sumaTotal += numActual
print(sumaTotal)
