#entradas
nombre=input("Ingrese su nombre: ")
mc=int(input("Ingrese el monto total de compra: "))
#caja negra
if(mc<50000):
    dto=0
    pagodto=mc
elif(50000<=mc<100000):
    dto=mc*0.05
    pagodto=(mc-dto)
elif(100000<=mc<700000):
    dto=mc*0.11
    pagodto=(mc-dto)
elif(700000<=mc<1500000):
    dto=mc*0.18
    pagodto=(mc-dto)
elif(mc>=1500000):
    dto=mc*0.25
    pagodto=(mc-dto)
#Salida
print("Nombre:",nombre)
print("Monto de compra:",mc)
print("Monto total a pagar:",pagodto)
print("El descuento es:",dto)