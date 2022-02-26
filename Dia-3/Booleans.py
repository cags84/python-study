# Tipo de datos Boleeans
# Solo puede tener dos valores, True, False
# Declaracion de forma indirecta 5 > 4, implicitamente tambien es boolean
# 5 in lista, tambien devuelve un booleano
# Los booleanos son la base de la inteligencia artificial

var1 = True
var2 = False

print(type(var1), var1)
print(type(var2), var2)

# De forma implicita
numero = 5 > 2 + 3
print(type(numero), numero)

# Funcion bool
numero = bool(5 > 6)
print(type(numero), numero)

# Preguntar por un valor
lista = [1, 2, 3, 4]
control = 5 in lista
control_not = 5 not in lista
print(type(control), control)
print(type(control_not), control_not)

