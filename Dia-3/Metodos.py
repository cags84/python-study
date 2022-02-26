# Metodos en Python

texto = "Este es el texto de Federico"

resultado = texto

# transformar todos los caracteres en mayusculas
print(texto.upper())
print(texto[2::2].upper())

# transformar todos los caracteres en minusculas
print(texto.lower())

# separar un string
resultado1 = texto.split("t")
print(resultado1)

# unir elementos de un string
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = ",".join([a, b, c, d])
print(e)

# buscar un determinado caracter dentro del string, la diferencia es que index lanza una excepción mientras que
# find devuelve un -1
resultado = texto.find("j")

# Metodo replace, tomar un fragmento de tu texto y reemplazarlo por otro
resultado = texto.replace("e", "x")

print(resultado)
