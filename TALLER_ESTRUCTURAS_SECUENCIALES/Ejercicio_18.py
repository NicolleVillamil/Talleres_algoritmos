#entradas
Bolivares=int(input("Cantidad de préstamo de Bolívares: "))
interes=int(input("Cantidad de intereses en 4 años: "))
#caja negra
anual=interes/4
ppr=(anual/Bolivares)*100
#salida
print("El porcentaje anual cobrado por el prestamo es de:",ppr)
