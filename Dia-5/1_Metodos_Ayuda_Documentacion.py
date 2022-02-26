# Metodos, Ayuda y Documentación
# La ayuda de la documentación de Python y PyCharm

dic = {
    'clave1': 100,
    'clave2': 500
}

a = dic.popitem()

print(type(a), a)
print(type(dic), dic)

# Práctica Métodos y Ayuda @1
texto = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(f"\nTexto original:\n {texto}")
# Utilizando el metodo lstrip()
# 1. ,
# 2. :
# 3. %
# 4. _
# 5. #

texto_modificado = texto.lstrip(',:%_#')
print(f"\nTexto modificado:\n { texto_modificado }")

# Práctica Métodos y Ayuda @2
# Añadir el elemento naranja como el cuarto elementos, utilizando el metodo insert
print("\n")
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3, 'naranja')
print(frutas)

# Práctica Métodos y Ayuda @2
# Verifica que los set a continuación forman conjuntos aislados, es decir que no tienen elementos en común
print("\n")
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)


