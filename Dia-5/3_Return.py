# Return
# Las funciones normalmente deben devolver algo

def multiplicar(num1, num2):
    return num1 * num2


resultado = multiplicar(5, 5)
print(resultado)


# Práctica Return @1
# Crea una función llamada potencia que tome dos valores numéricos como argumentos.
# Deberá devolver el número que resulte de resolver una potencia. Utilizando el primer
# número como base, y el segundo como exponente:
# 3^e = resultado
# 3 -> Base (Primer argumento)
# e -> Exponente (Segundo argumento)
# resultado -> potencia

def potencia(num1, exp):
    res = num1 ** exp
    return res


resultado = potencia(2, 2)
print(resultado)

# Práctica Return @2
dolares = 100


def usd_a_eur(monto):
    conversion = monto * 0.85
    return conversion


print(f"${dolares} dolares es €{usd_a_eur(dolares)} euros")

# Práctica Return @3
palabra = "Python"


def invertir_palabra(texto):
    invertir_texto = texto[::-1].upper()
    return invertir_texto


print(invertir_palabra(palabra))
