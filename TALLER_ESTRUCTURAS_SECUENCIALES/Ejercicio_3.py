#Entradas
sueldo_base=float(input("Ingrese su sueldo base: "))
venta1=float(input("Ingrese su 1 venta: "))
venta2=float(input("Ingrese su 2 venta: "))
venta3=float(input("Ingrese su 3 venta: "))
#Caja negra
comision=(venta1+venta2+venta3)*0.1
total=comision+sueldo_base
#Salidas
print("Esto es lo ganado por comisiones",comision)
print("Esto es el total ganado:",total)

