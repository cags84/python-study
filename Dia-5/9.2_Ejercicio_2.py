# 9.2 Ejercicio #2

# Escribe una función (puedes ponerle cualquier nombre que quieras) que reciba cualquier palabra como parámetro, y que devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.

# Por ejemplo si al invocar esta función pasamos la palabra "entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']

def mi_funcion(palabra):

    no_repetidas = set()

    for letra in palabra:
        no_repetidas.add(letra)

    palabra_new = list(no_repetidas)
    palabra_new.sort()
    return palabra_new


print(mi_funcion("cascarrabias"))