# 7 - Funciones con Argumentos Indefinidos
# *args -> argumentos son variables
# **kwargs

def suma(a, b):
    return a + b


print(suma(5, 6))


# Con *args
def suma(*args):
    print(type(args))
    total = 0

    for arg in args:
        total += arg

    return total


print(suma(5, 6, 10, 40))


# args con la funcion sum

def sumar_con_sum(*args):
    return sum(args)


print(sumar_con_sum(5, 6, 10, 40))


# Práctica sobre Argumentos indefinidos (*args) @1

def suma_cuadrados(*args):
    suma = 0

    for arg in args:
        suma += arg ** 2

    return suma


print(f"Total: {suma_cuadrados(1, 2, 3)}")


# Práctica sobre Argumentos indefinidos (*args) @2

def suma_absolutos(*args):
    total = 0
    for arg in args:
        total += abs(arg)
    return total


print(suma_absolutos(-1, 1, -1))


# Práctica sobre Argumentos indefinidos (*args) @3

def numeros_persona(*args):
    nombre = args[0]
    lista_numeros = list(args[1:])
    suma_numeros = 0

    for num in lista_numeros:
        suma_numeros += num

    return f"{nombre}, la suma de tus números es {suma_numeros}"


print(numeros_persona('Carlos', 1, 2, 3, 4))
