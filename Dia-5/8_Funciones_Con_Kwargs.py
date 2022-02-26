# 8_ Argumentos indefinidos (**kwargs)
# key word args -> palabra claves
# Se le puede dar un nombre o indice del elemento

def suma(**kwargs):
    """
    Funcion de Suma
    :param kwargs:
    :return:
    """
    suma_total = 0
    for key, value in kwargs.items():
        suma_total += value
        print(f"{key} = {value}")

    return suma_total


print(suma(x=1, y=5, z=3))


# Mezclar *args y **kwargs

def suma(num1, num2, num3, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El primer valor es {num2}")
    print(f"El primer valor es {num3}")

    for arg in args:
        print(f"arg = {arg}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")


args = [1, 2, 3, 4]
kwargs = {
    'x': 'uno', 'y': 'dos', 'z': 'tres'
}

suma(15, 50, 40, *args, **kwargs)

# Práctica sobre Argumentos Indefinidos (**kwargs) @1

print("\n")


def cantidad_atributos(**kwargs):
    cantidad = 0

    for item in kwargs.items():
        cantidad += 1

    return cantidad


kwargs1 = {
    'x': 'uno', 'y': 'dos', 'z': 'tres'
}

print(
    type(kwargs1)
)

print(cantidad_atributos(x=1, y=5, z=3))


# Práctica sobre Argumentos Indefinidos (**kwargs) @2

def lista_atributos(**kwargs):
    lista = []

    for key, value in kwargs.items():
        lista.append(value)

    return lista


print(lista_atributos(x=1, y=5, z=3))

# Práctica sobre Argumentos Indefinidos (**kwargs) @3
print("\n")


def describir_persona(nombre, **kwargs):
    print(f"características de {nombre}:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


describir_persona("María", color_ojos="azules", color_pelo="rubio")


