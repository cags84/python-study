# Las tuplas en Python son inmutables, se escriben entre ()
# Ocupan menos espacio en memoria
# Almacenar estructura que no queremos que sean modificadas

# Con o sin parentesis
mi_tuple = (1, 2, 3, 4)
mi_tuple = 1, 2, 3, 4
print(type(mi_tuple))

# Pueden contener cualquier tipo de objeto
t = (1, 2.3, "otro", {1,2})
print(type(t))
print(t)

# Index de los elementos
print(mi_tuple[-2])

# Son inmutables al igual que los string, una vez creado el objeto no se puede tocar
mi_tuple = (1, 2, (10, 20), 4)
print(mi_tuple[2])
print(mi_tuple[2][1])

# Casting, tranformar a una lista por ejemplo
mi_lista = list(mi_tuple)
print(type(mi_lista))
print(mi_lista)

# Asignar el contenido de un tuple a diferentes variabkes
# Destructuracion
t = (1, 2, 3)
x, y, z = t
print(x, y, z)

# len
t = (1, 2, 3, 1)
print(len(t))

# Cuantas veces aparece un elemento en un tuple
print(t.count(1))

# En que indice se encuentra el elemento
print(t.index(2))