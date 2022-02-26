# Funciones Min y Max
# Sirven para detectar los valores mas bajo y mas altos de una coleccion

menor = min(58, 96, 72, 64)
print(menor)

maximo = max(58, 96, 72, 64)
print(maximo)

lista = [58, 96, 72, 64]
print(max(lista))
print(f"El menor es {min(lista)} y el mayor es {max(lista)}")

nombres = ['Juan', 'Pablo', 'Alicia', 'Carlos']
print(f"{min(nombres)}")

# Comienza siempre con las mayusculas
nombre = 'Carlos'
print(f"{ min(nombre.lower()) }")

# Como se comporta con los diccionarios
dic = {
    "c1": 45,
    "c2": 11
}
print(f"Buscar por items: {min(dic.items())} ")
print(f"Buscar por keys: {min(dic.keys())} ")
print(f"Buscar por valores: {min(dic.values())} ")

# Práctica Min y Max #1
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max(lista_numeros)
print(valor_maximo)

# Práctica Min y Max #2
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros) - min(lista_numeros)
print(rango)

# Práctica Min y Max #3
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(ultimo_nombre, edad_minima)


