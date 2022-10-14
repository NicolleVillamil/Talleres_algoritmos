#entradas
lec_act=int(input("Ingrese la Lectura de energia actual:"))
lec_ant=int(input("Ingrese la Lectura de energia anterior:"))
#Caja negra
energia=abs(lec_act-lec_ant)
pago=""
if(0<=energia<=100):
    pago=4600*energia
elif(101<=energia<=300):
    pago=80000*energia
elif(301<=energia<=500):
    pago=100000*energia
elif(energia>=501):
    pago=120000*energia
#Salida
print("el total a pagar:",pago)
