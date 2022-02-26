# Compresion de lista
# Dinamica de construir listas

palabra = 'python'
lista = []

for letra in palabra:
    lista.append(letra)

print(type(lista), lista)

# Con compresion de listas
lista = [letra for letra in palabra]
print(type(lista), lista)

lista = [n for n in range(0, 21, 2)]
print(type(lista), lista)

lista = [n/2 for n in range(0, 21, 2)]
print(type(lista), lista)

# Con if
lista = [n for n in range(0, 21, 2) if (n * 2 > 10)]
print(type(lista), lista)

# Con if y else
lista = [n if (n * 2 > 10) else 'no' for n in range(0, 21, 2)]
print(type(lista), lista)

pies = [10, 20, 30, 40, 50]
metros = [p * 3.281 for p in pies]
print(type(metros), metros)

# Práctica comprensión de Lista #1
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [v ** 2 for v in valores]
print(type(valores_cuadrado), valores_cuadrado)

# Práctica comprensión de Lista #2
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [p for p in valores if (p % 2 == 0)]
print(type(valores_pares), valores_pares)

# Práctica comprensión de Lista #3
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [((t-32)*(5/9)) for t in temperatura_fahrenheit]
print(type(grados_celsius), grados_celsius)
