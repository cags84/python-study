# Propiedades String en Python

# Los String son inmutables
nombre = "Carina"
#nombre[0] = "K"
print(nombre)

n1 = "Karina"
n2 = "na"
print(n1 + n2)

# Multiplicar los strings
print(n1 * 10)

# Puede contener varias líneas de código

poema = """
    Mil pequeños peces blancos
    como si hirviera
    el color del agua
"""

print(poema)

# Se puede consultar si en un string existe una pablabra, caracter
print("agua" in poema)
print("agua" not in poema)
