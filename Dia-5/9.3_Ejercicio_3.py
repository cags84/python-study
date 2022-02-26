# 9.3 Ejercicio #3
# Escribe una función que requiera una cantidad indefinida de argumentos. Lo que hará esta función es devolver True si en algún momento se ha ingresado al numero cero repetido dos veces consecutivas.

# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False

def mi_funcion(*args):
    """
    Mi Función
    :param args:
    :return:
    """

    item_old = 0
    item_new = 0

    for key, item in enumerate(args):

        if key != 0:
            item_new = item
            if item_old == item_new:
                return True
            else:
                item_old = item
        else:
            item_old = item
            item_new = item

    return False

print(mi_funcion(5, 6, 1, 0, 0, 9, 3, 5))
print(mi_funcion(6, 0, 5, 1, 0, 3, 0, 1))
