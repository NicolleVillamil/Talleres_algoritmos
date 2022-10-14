#Entradas
km=int(input("ingrese el kilometraje: "))
#caja negra
recargo=(km-300)
if(km<=300):
    pago=50000
elif(300<km<=1000):
    pago=70000+(30000*recargo)
elif(300<km>1000):
    pago=150000+(9000*recargo)
print(pago)