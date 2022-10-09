#entradas
Lec_ant=float(input("Ingrese la lectura anterior de kilovatios: "))
Lec_act=float(input("Ingrese la lectura actual de kilovatios: "))
Costo=float(input("Ingrese el costo por kilovatio: "))
#caja negra
monto=abs(Lec_act-Lec_ant)*Costo
#salida
print("El monto total a pagar en un mes de luz electrica es:",monto)