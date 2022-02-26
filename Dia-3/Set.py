# Set
# Se declara con set(...)
# con llaves { 1, 2, 3 }
# Los elementos no se repiten
# No estan ordenados en indice por posición
# Son elementos inmutables
# No se pueden guardar listas y diccionarios

mi_set = set([1, 2, 3, 4, 5])
mi_set = set({1, 2, 3, 4, 5})
mi_set = set((1, 2, 3, 4, 5))
print(type(mi_set))
print(mi_set)

otro_set = {1, 2, 3, 4, 5}
print(type(otro_set))
print(otro_set)

# No tiene un orden interno
# Para buscar
print(mi_set)

# Acepta un tuple
otro_set1 = {1, 2, 3, 4, 5, (1, 2)}
print(otro_set1)

# Conocer la cantidad de elementos len
len_1 = len(otro_set)
print(len_1)

# Puedo saber si existe un elemento en el set
print(2 in otro_set1)

# Union de set
s1 = {1, 2, 3}
s1.add(6)
s1.add(2)
s1.pop() # Aleatorio
s1.remove(2)
s1.discard(2)
s2 = {3, 4, 5}
s3 = s1.union(s2)

s3.clear()

print(type(s3))
print(s3)

