# Random
# Numeros aleatorios, como se importan metodos a python
# metodo randint(), es de la libreria propia de python llamada random
# Metodos a revisar
# randint()
# uniform()
# random()
# choice()
# shiffle()

from random import randint, uniform, random, choice, shuffle

numero_aleatorio = randint(1, 1000)
print(numero_aleatorio)

# Metodo uniform
# Un valor decimal entre el rango
numero_aleatorio = round(uniform(1, 400), 1)
print(numero_aleatorio)

# Metodo random
# No necesita parametros y devuelve un numero entre 0 o 1
numero_aleatorio = random()
print(numero_aleatorio)

# Choice
# Aleatorio dentro de una lista
colores = ['Azul', 'Rojo', 'Verde']
colores_aleatorios = choice(colores)
print(colores_aleatorios)

# shuffle
# mezclar, en los juegos de carta es util
# no devuelva nada, lo hace en situ, no se puede usar con string por ejemplo
# porque son inmutables.
numeros = list(range(5, 50, 5))
shuffle(numeros)
print(type(numeros), numeros)

# Practica random #1
aleatorio = randint(1, 10)
print(type(aleatorio), aleatorio)

# Practica random #2
aleatorio = random()
print(type(aleatorio), aleatorio)

# Practica random #3
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(type(sorteo), sorteo)
