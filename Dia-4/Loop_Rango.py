# Loop con rango

lista = [1, 2, 3, 4]

for numero in lista:
    print(numero)

print("\n")
for numero in range(50, 0, -1):
    print(numero)

# Usar por fuera de los loops

lista = [1, 2, 3] # ... 10
lista = list(range(1, 101))
print(type(lista), lista)
