# Control_Flujo

if 10 > 9:
    print("Es correcto")

x = True
if x:
    print("Es Correcto")

if 5 == 2:
    print("Es igual")
else:
    print("No es igual")

mascota = "conejo"

if mascota == "gato":
    print("Tienes un gato")
elif mascota == "perro":
    print("Tienes un perro")
elif mascota == "pez":
    print("Tienes un pez")
else:
    print("No se qué animal tienes")

edad = 16
calificacion = 5

if edad < 18:
    print("Eres menor de edad")
    if calificacion > 7:
        print("Aprobaste el curso :)")
    else:
        print("No aprobaste el curso :(")
else:
    print("Eres adulto")

num1 = input("Ingresa un número: ")
num2 = input("Ingresa otro número: ")

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
