# 9.4 Ejericio 4
# Escribe una función llamada contar_primos() que requiera un solo argumento numérico.
# Esta función va a mostrar en pantalla cuántos números primos hay en el rango que va desde cero hasta ese número incluido, y va a devolver la cantidad de números primos que encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos.

def contar_primos(num1):
    total_numeros_primos = 0
    cantidad_primos = 0

    for x in range(0, num1 + 1):

        if x <= 0 or x == 1:
            pass

        for y in range(1, x + 1):
            if x % y == 0:
                cantidad_primos += 1

        if cantidad_primos == 2:
            total_numeros_primos += 1

        cantidad_primos = 0

    return total_numeros_primos


def menu():
    numero = int(input(f"Por favor ingresa un numero: "))
    cantidad_numeros_primos = contar_primos(numero)

    print(f"La cantidad de números primos que hay desde 0 al {numero} es: {cantidad_numeros_primos}")


menu()
