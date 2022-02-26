# Interacciones entre funciones
from random import shuffle, randint, choice

# Lista inicial

palitos = ['-', '--', '---', '----']


# Funcion que se encarga de mezclar los palitos

def mezclar(lista):
    shuffle(lista)
    return lista


# Pedirle al usuario intento

def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un número del 1 al 4: ")

    return int(intento)


# Comprobar intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == intento:
        print("A lavar los platos")
    else:
        print("Te salvaste!")
    print(f"Te ha tocado {lista[intento - 1]}")


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)


# Práctica sobre Interacción entre Funciones @1

def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return (f"La suma de tus dados es {suma_dados}. Lamentable")
    elif (suma_dados > 6) and (suma_dados < 10):
        return (f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        return (f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")


dados = lanzar_dados()
print(evaluar_jugada(dados[0], dados[1]))

# Práctica sobre Interacción entre Funciones @2

lista_numeros = [1, 2, 15, 7, 2]


def reducir_lista(lista):
    new_lista = set()

    for num in lista:
        new_lista.add(num)

    new_lista = list(new_lista)
    new_lista.sort()
    new_lista.pop()

    return new_lista


def promedio(lista):
    suma_promedio = 0

    for num in lista:
        suma_promedio += num

    promedio_num = suma_promedio / len(lista)
    return promedio_num


lista_reducida = reducir_lista(lista_numeros)
print(promedio(lista_reducida))

# Práctica sobre Interacción entre Funciones @3
print("\n")
lista_numeros = [1, 2, 15, 7, 2]


def lanzar_moneda():
    opcion = choice(['Cara', 'Cruz'])
    return opcion


def probar_suerte(opcion, lista):

    if opcion == 'Cara':
        print(f"La lista se autodestruirá")
        lista = []
        return lista

    print(f"La lista fue salvada")
    return lista


opcion_carta = lanzar_moneda()
print(probar_suerte(opcion_carta, lista_numeros))
