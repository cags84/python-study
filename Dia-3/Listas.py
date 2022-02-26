# Listas en Python

mi_lista = ["a", "b", "c"]
# otra_lista = ["hola", 55, 6.1]

# Cuanto elementos contiene una lista
res = len(mi_lista)
print(f"La lista tiene {res} elementos")

# Extraer elementos de una lista
res = mi_lista[0]
print(res)

# Buscar los indices que van de..
res = mi_lista[0:2]
print(res)

# Concatenación de lista
mi_lista2 = ["d", "e", "f"]
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

# Alterar sus elementos
mi_lista3[0] = "alfa"
print(mi_lista3)

# Agregar elementos a la lista
mi_lista3.append("g")
print(mi_lista3)

# Eliminar elementos
mi_lista3.pop() # Elimina el último
print(mi_lista3)
mi_lista3.pop(1)
print(mi_lista3)

eliminado = mi_lista3.pop(1)
print(mi_lista3)
print(eliminado)

# Ordenar las listas
print("fff")
lista = ["g", "o", "b", "m", "c"]
print(lista)
lista.sort()
print(lista)

# Invertir el orden
print("fff")
lista.reverse()
print(lista)

print(type(mi_lista))
