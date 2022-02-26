# Proyecto de DIA - 2

# Comisiones del 13% por ventas totales

nombre_empleado = input("Dime tu nombre: ")
total_ventas = float(input("Cual fue el total de la ventas: "))

comision = total_ventas * 13 / 100
comision = round(comision)

print(f"Ok {nombre_empleado}. este mes ganaste ${comision} por comisión")
