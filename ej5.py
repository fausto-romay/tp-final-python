#1.
def saludar(nombre):
    saludo = f"Hola {nombre}"
    return saludo

print(saludar("Fausto"))

#2.
def suma(a, b):
    resultado = a + b
    return resultado

print(suma(10, 50))

#3.
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

print(es_mayor_de_edad(19))