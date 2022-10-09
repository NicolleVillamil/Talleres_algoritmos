#Entrada
X=int(input("Ingrese la cantidad de naranjas: "))
Y=int(input("Ingrese costo de docena: "))
K=int(input("Ingrese la venta de las naranjas: "))
#Caja negra
Precio_uni=(X*Y)/12
Porcen=(K-Precio_uni)*100/Precio_uni
#Salida
print("Las ganancias son:",Porcen)