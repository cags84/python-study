# Loops

# for
# por cada elemento imprimir holas

# Ejemplo 1
nombres = ["Juan", "Ana", "Carlos", "Belén", "Fran"]
nombre: str
for nombre in nombres:
    print(f"Hola { nombre }")

print("\n")

# Ejemplo 2
letras = ['a', 'b', 'c']
for letra in letras:
    numero_letra = letras.index(letra) + 1
    print(f"Letra { numero_letra }: { letra }")

print("\n")
lista = ["pablo", "laura", "fede", "luis", "julia"]
for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print("Nombre que no comienza con L")

print("\n")
numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(f"El valor de sumatoria es: { mi_valor }")

####
print("\n")
palabra = "python"

for letra in palabra:
    print(letra)

### For con tupla
print("\n")
for letra in (1, 2, 3):
    print(letra)

### For con lista
print("\n")
for letra in [1, 2, 3]:
    print(letra)

### For con diccionario
print("\n")
for letra in {"uno": 1, "dos": 2, "tres": 3}:
    print(letra)

### For con diccionario
print("\n")
for objeto in [[1,2], [2.3], [3,4]]:
    print(objeto)


### For con diccionario
print("\n")
for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)

# Diccionarios
dic = {
    'clave1': 'a',
    'clave2': 'b',
    'clave3': 'c'
}

for a, b in dic.items():
    print(a, b)

for item in dic.keys():
    print(item)

for item in dic.values():
    print(item)
