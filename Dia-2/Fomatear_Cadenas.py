# Formatear cadenas

x = 10
i = 5

# Primera forma, la tradicional
print("Mis numeros son " + str(x) + " y " + str(i))
# Segunda forma, con .format
print("Mis numeros son {} y {}".format(x, i))
print("La suma de {} y {} es igual a ".format(x, i, (x + i)))
# Desde Python 3.6, cadenas literales
print(f"Mis numeros son {x} y {i}")

# Otro ejemplo
color = "rojo"
matricula = 541926
print(f"El auto es {color} y la matricula es {matricula}")
