# Zip
# lo que hace basicamente es combinar 2 o mas listas
# Voy a tener la union de las dos listas en formato de tuple
# Solo funciona con la lista mas corta

nombres = ["Ana", "Hugo", "Valeria"]
edades = [65, 29, 42, 58]
ciudades = ['Lima', 'Madrid', 'Mexico']

combinados = zip(nombres, edades, ciudades)
print(type(combinados), combinados)

# Para poder verlo, tenemos que castearlo en una lista
print("\n")
combinados = list(combinados)
print(type(combinados), combinados)

print("\n")
for nombre, edad, ciudad in combinados:
    print(f"{ nombre } tiene { edad } años y vive en { ciudad }")

print("\n")
# Practica ZIP # 1
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinados = zip(capitales, paises)
combinados = list(combinados)

for (capitales, paises) in combinados:
    print(f"La capital de { paises } es { capitales }")

print("\n")
# Practica ZIP # 2
marcas = ["Sony", "Apple", "Nike"]
productos = ["Camiseta", "Macbook Pro", "Zapatillas"]

mi_zip = zip(marcas, productos)
print(mi_zip)


print("\n")
# Practica ZIP # 3
lista = []

spanish = ["uno", "dos", "tres", "cuatro", "cinco"]
portuguese = ["um", "dois", "três", "quatro", "cinco"]
english = ["one", "two", "three", "four", "five"]

lista = zip(spanish, portuguese, english)
numeros = list(lista)

print(type(numeros), numeros)