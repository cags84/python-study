# Su funcion en ayudarnos a encontrar un indice
#

lista = ['a', 'b', 'c']
indice = 0

for letra in lista:
    print(indice, letra)
    indice += 1

print("\n")

# Una mejora con enumerador
for (indice, item) in enumerate(lista):
    print(indice, item)

for (indice, item) in enumerate(range(50, 55)):
    print(indice, item)

lista = ["a", "b", "c"]
mis_tuples = list(enumerate(lista))
print(mis_tuples[1][0])


print("\n")
lista = ["Python"]
lista_indices = list(enumerate(lista))
print(lista_indices)


lista = list("Python")
lista = tuple(enumerate(lista))
print(lista)

lista_indices = tuple(enumerate("Python"))
lista_indices = list(lista_indices)
print(type(lista_indices), lista_indices)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for (indice, item) in enumerate(lista_nombres):
    if item[0] == "M":
        print(indice)