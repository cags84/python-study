# Proyecto día 4

# El programa le va a preguntar al usuario su nombre y le va a decir
# pensar un número entre el 8 y el 100 y tenes solo 8 intentos para adivinarlo
# En cada intento el usuario dira un numero y el programa podra responder cuatro cosas distintas
# 1. Si el número que dijo el usuario es menor a 1 0 superior a 100, le debe decir que elogio un numero que no esta permitido
# 2. Si < al que penso el programa le va a decir que es incorrecta y ha elegido un numero menor al que se tiene
# 3. si > al que penso el programa le va a decir que es incorrecta y ha elegido un numero mayor al que se tiene
# 4. Si acierta le va a decir que ha ganado y cuantos intentos ha tomado

# Si no acerto en los cuatros intentos se le va a pedir que elija otro numero y vuelve arrancar
# Hasta que gane o se agoten los ocho intentos
from random import randint

nombre = input("Dime tu nombre: ")
num_intentos = 1
numero_aleatorio = randint(1, 100)
numero_intentos_maximo = 8

while num_intentos <= numero_intentos_maximo:
    print(f"\nIntento #{ num_intentos } - Te quedan { numero_intentos_maximo - num_intentos }")
    numero_ingresado = int(input("Piensa en un numero entre 1 y 100: "))

    if numero_ingresado == numero_aleatorio:
        print(f"\tFelicitaciones acertaste el número y solo te tomo { num_intentos } intento")
        break
    elif numero_ingresado > numero_aleatorio:
        print(f"\tEl numero que ingresaste es mayor al generado")
    elif numero_ingresado < numero_aleatorio:
        print(f"\tEl numero que ingresaste es menor al generado")
    else:
        print(f"\tEl numero { numero_ingresado } esta fuera de rango, es de 1 a 100")

    num_intentos += 1
else:
    print(f"\n\nLo siento has perdido :( ... el número secreto era { numero_aleatorio }")
