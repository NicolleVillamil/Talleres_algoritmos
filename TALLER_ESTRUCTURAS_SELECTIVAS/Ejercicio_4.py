#entradas
piezas=int(input("Ingrese la cantidad de piezas: "))
costo_uni=int(input("Ingrese el costo unitario: "))
#Caja negra
mt=piezas*costo_uni
print("El monto total a pagar es:",mt)
if(mt>5000000):
    empre=mt*0.55; credibanco=mt*0.3; credifabrica=mt*0.15
else:
    empre=mt*0.7; credifabrica=mt*0.3
interes=credifabrica*0.2
#salidas
print("Monto a invertir por la empresa:",round(empre,9))
print("Pago por credito:",credifabrica)
print("Pago por intereses:",interes)
print("La cantidad de prestamo al banco:",credibanco)

