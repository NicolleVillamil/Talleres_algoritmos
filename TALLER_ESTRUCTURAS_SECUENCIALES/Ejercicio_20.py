#Entrada
P=float(input("Ingrese el precio a contado: "))
T=float(input("Ingrese el precio de T en COP: "))
#Caja negra
VTC=12*T
Recargo=VTC-P
Porcen=((Recargo/P)*100)/12
#Salida
print("el porcentaje",Porcen,"%")