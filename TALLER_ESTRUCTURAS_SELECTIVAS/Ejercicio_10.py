#entradas
cat=int(input("Ingrese a la categoria que pertenece: "))
suld_br=int(input("Ingrese su sueldo bruto: "))
#Caja negra
if(cat==1):
    if(suld_br==5000000):
        aumento=(suld_br*0.1)
elif(cat==2):
    if(suld_br==4300000):
        aumento=(suld_br*0.15)
elif(cat==3):
    if(suld_br==3600000):
        aumento=(suld_br*0.20)
elif(cat==4):
    if(suld_br==2000000):
        aumento=(suld_br*0.40)
elif(cat==5):
    if(suld_br==90000):
        aumento=(suld_br*0.60)
new=aumento+suld_br
#Salida
print("Su categoria es: "+str(cat)+ " y Su nuevo saldo bruto es: "+str(new))
