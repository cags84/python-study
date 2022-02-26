# Diccionarios no se pueden repetir
# Se escribe entre llaves {}

diccionario = {
    "c1": "valor1",
    "c2": "valor2",
    "c3": "valor3"
}

print(type(diccionario))
print(diccionario)

# Extraer una clave
resultado = diccionario["c1"]
print(type(resultado))
print(resultado)

# Definir un diccionario
cliente = {
    "nombre": "Juan",
    "apellido": "Fuentes",
    "peso": 88,
    "talla": 1.76
}

consulta = cliente['apellido']
consulta = cliente['talla']
print(consulta)

dic = {
    "c1": 55,
    "c2": [
        10, 20, 30
    ],
    "c3": {
        "s1": 100,
        "s2": 200
    }
}

print(type(dic))
print(dic["c2"])
print(dic["c2"][1])
print(dic["c3"]["s1"])

# Ejercicio
dic = {
    "c1": ["a", "b", "c"],
    "c2": ["d", "e", "f"]
}

# Imprimir la letra e pero en mayusculas
print(dic["c2"][1].upper())

dic = {
    1: 'a',
    2: 'b'
}

print(dic)

dic[3] = 'c'

print(dic)
print(type(dic))

# Sobreescribir
dic[2] = 'B'
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())