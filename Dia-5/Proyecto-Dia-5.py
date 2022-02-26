# Proyecto Día 5

# El programa va a elegir una palabra  secreta y le va a mostrar al jugados solamente
# unos guiones que representa la cantidad de letras que tiene la palabra, el jugador
# en cada turno debera elegir una letra y si la letra se encuentra en la palabra oculta
# el programa le debe informar en que lugar se encuentra, pero si no pierde una vida
# y le debemos mostrar cuantas vidas tiene todavía, si se agota la vida antes que el
# jugador adivina la palabra, el jugador pierde pero si no el jugador gana.

# Importe el metodo choice, para elegir una palabra dentro de una lista de palabras
# crear funciones para: pedir_letra, validar_letra, chequear_letra, ver si gano, etc.
# primero se escriber las funciones y luego el codigo que las implementa.

from random import choice

intentos_permitidos = 0
numero_intentos = 0
lista_palabras = [
    "flecha", "camion", "computador", "estudiar", "comer", "jugar", "aprender"
]


def elegir_palabra_secreta(lista_de_palabras):
    palabra_aleatorea = choice(lista_de_palabras)
    return palabra_aleatorea


def mostrar_palabra_secreta(palabra):
    lista_guiones = []

    for letra in palabra:
        lista_guiones.append("_")

    print("\n")
    print(f"Adivina la palabra:  - \t tienes { len(palabra) } intentos!")
    print(lista_guiones)


def validar_letra(letra):
    if type(letra) != str:
        return False


def pedir_letra():
    letra_temp = input(f"\nDigita una letra: ")

    return letra_temp


palabra_secreta = elegir_palabra_secreta(lista_palabras)
mostrar_palabra_secreta(palabra_secreta)

while numero_intentos < len(palabra_secreta):
    letra = pedir_letra()

    numero_intentos += 1
else:
    print(f"\nLo siento perdiste! :(")
