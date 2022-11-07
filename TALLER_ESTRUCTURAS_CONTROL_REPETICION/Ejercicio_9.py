a=0
g=0
d=0
while True:
    tipo=int(input())
    if(tipo==4):
        break
    if(tipo==1):
        a=a+1
    elif(tipo==2):
        g=g+1
    elif(tipo==3):
        d=d+1
print("MUITO OBRIGADO")
print("Alcool:",a)
print("Gasolina:",g)
print("Diesel:",d)