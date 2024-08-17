#1.
num1 = int(input("Ingrese número: "))
num2 = int(input("Ingrese número: "))

suma = num1 + num2
producto = num1 * num2
concatenacion = str(num1) + str(num2)

print(f"Suma: {suma}, Producto: {producto}, Concatenación: {concatenacion}")

#2.
cadena = input("Ingrese una cadena de texto: ")
cadenaInvertida = cadena[::-1]

print(cadena.upper())
print(len(cadena))
print(cadenaInvertida)

letra = input("Ingrese una letra: ")
cantidad = cadena.count(letra)

#3.
decimal = int(input("Ingrese un número decimal: "))
print(f"El número decimal {decimal} en binario es: {bin(decimal)[2:]}")

binario = int(input("Ingrese un número binario: "))
print(f"El número binario {binario} en decimal es: {int(binario, 2)}")

#4.
cadenaTexto = input("Ingrese una cadena de texto: ")
numero = int(input("Ingrese un número: "))

while numero != 0:
    print(cadenaTexto)
    numero -= 1

