# Funciones
# Los metodos son funciones que fueron incorporados a los objetos
# Bloques de codigo que pueden ser ejectutados en diferentes contextos

# Palabra clave def -> le dice a python que es una funcion

def mi_funcion(nombre):
    """
    Esta bueno describir la funcion, sirve para documentar el codigo
    """
    # Bloque de la funcion
    print(f"Hola {nombre}, desde la funcion")


# De esta forma ejecutamos la funcion
mi_funcion('Carlos')


def saludar_persona(nombre):
    """
    Esta funcion saluda a una persona
    :param nombre: str
    :return: str
    """
    print(f"Hola {nombre} desde la funcion saludar_persona")


saludar_persona("Carlos Guzmán")


# Práctica crear funciones @1
# Declara una función llamada saludar, que cada viez que sea llamada imprima en pantalla "¡Hola Mundo!"

def saludar():
    print("¡Hola mundo!")


saludar()

# Práctica crear funciones @2
# Declara una funcion llamada bienvenida, que tome como argumento el nombre de una persona, y que cada
# vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"
# Para probar su funcionamiento, crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras
nombre_persona = "Carlos Guzman"


def bienvenida(nombre):
    print(f"¡Bienvenido {nombre}!")


bienvenida(nombre_persona)

# Práctica crear funciones @2
# Declara una funcion llamada cuadrado, que tome como argumento un número cualquieram y que cada vez que sea llamada,
# imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor)
# El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asignarle un número
# cualquiera para probar la funcion creada.
un_numero = 10


def cuadrado(numero):
    potencia = numero ** 2
    print(f"{potencia}")


cuadrado(un_numero)
