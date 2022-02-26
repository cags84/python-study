# Funciones Dinamicas
#

suma = 586 + 40


def chequear_3_cifras(numero):
    return numero in range(100, 1000)


resultado = chequear_3_cifras(suma)
print(resultado)

# Otro ejemplo
lista = [502, 782, 1002, 1002]


def chequear_3_cifras(lista_numeros):
    lista_3_cifras = []

    for num in lista_numeros:
        if num in range(100, 1000):
            lista_3_cifras.append(num)
        else:
            pass
    return lista_3_cifras


resultado = chequear_3_cifras(lista)
print(type(resultado), resultado)

# Práctica Funciones Dinámicas @1
# Crea una función todos_positivos que devuelva True su tidos los valores de una lista
# lista_numeros son positivos. Y false si al menos uno de los valores es negativo.

lista_numeros = [1, 502, 709, 200, -1060]


def todos_positivos(lista):
    for num in lista:
        if num < 0:
            return False
        else:
            pass
    return True


respuesta = todos_positivos(lista_numeros)
print(respuesta)

# Práctica Funciones Dinámicas @2

lista_numeros = [1, 1, 1, 10, -1060, 1001]


def suma_menores(lista):
    suma = 0
    for num in lista:
        if (num > 0) and (num < 1000):
            suma += num
        else:
            pass
    return suma


resultado = suma_menores(lista_numeros)
print(resultado)

# Práctica Funciones Dinámicas @3

lista_numeros = [1, 50, 502, 755, 34]


def cantidad_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += 1
        else:
            pass
    return suma


resultado = cantidad_pares(lista_numeros)
print(resultado)
