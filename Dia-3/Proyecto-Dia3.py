# Proyecto del día 3
# 1. Pedir al usuario que ingrese un texto, puede ser un texto cualquiera
# 2. Le va a pedir que ingrese 3 letras a su elección
# 3. Devolver la siguiente información
# 3.1 Cuantas veces aparece cada una de las letra (Almacenar estos datos en una lista y no permita contar, cambiar a minusculas)
# 3.2 Cuantas palabras hay a lo largo de todo el texto(transforma en lista para contar)
# 3.3 Primera letra del texto y tambien la última
# 3.4 Mostrar el texto en forma inversa
# 3.5 Nos debe indicar si la palabra Python aparece en la lista

texto_ingresado = input("Digita un texto: ")
letras = input("Digita 3 letras que quieras buscar: ")

texto_ingresado = texto_ingresado.lower()
lista_letras = list(letras.lower())

print()
print("======================================================")

print(f"Texto Original:\n {texto_ingresado}")

print("\n")
# Buscar la letra de la posición 1
find_letra_1 = texto_ingresado.count(lista_letras[0])
print(f"La letra {lista_letras[0]} aparece {find_letra_1} en el texto")
find_letra_2 = texto_ingresado.count(lista_letras[1])
print(f"La letra {lista_letras[1]} aparece {find_letra_2} en el texto")
find_letra_3 = texto_ingresado.count(lista_letras[2])
print(f"La letra {lista_letras[2]} aparece {find_letra_3} en el texto")

print()
# Cantida de palabras
cantidad_palabras = texto_ingresado.split()
print(f"La cantidad de palabras en el texto es igual a {len(cantidad_palabras)} \n")

# Primera letra y última del texto
print(f"La primera letra del texto es {texto_ingresado[0]} y la última es {texto_ingresado[-1]} \n")

# El texto en forma inversa
texto_inverso = texto_ingresado.split()
texto_inverso.reverse()
texto_inverso = " ".join(texto_inverso)
print(f"El texto en forma inversa es: \n {texto_inverso} \n")

# Debe indicar si el el texto Python existe en el texto
find_python_in_text = "python" in texto_ingresado
dic = {
    True: 'Si',
    False: 'No'
}
print(f"Existe la palabra \"Python\" en el documento: {dic[find_python_in_text]}")