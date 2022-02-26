# Loop While

monedas = 5

while monedas > 0:
    print(f"Tengo { monedas } monedas")
    monedas -= 1
else:
    print("No tengo más monedas")

respuesta = "s"
while respuesta == "s":
    respuesta = input("Quieres continuar? (s/n) ")
else:
    print("Gracias!")

# Palabras clave
# pass, pasar no hacer nada
# break
# continue

#respuesta = "s"
#while respuesta == "s":
#    pass
#print("hola")

nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == "r":
        break
    print(letra)

# Continue
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == "r":
        continue
    print(letra)

numero = 50

while numero >= 0:
    if numero % 5 == 0:
        print(numero)
    numero = numero - 1
