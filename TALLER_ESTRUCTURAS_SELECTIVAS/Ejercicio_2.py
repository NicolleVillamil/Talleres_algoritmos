#entradas
Sueldo_bruto=int(input("Ingrese su sueldo bruto: "))
#Caja negra
if(Sueldo_bruto<900000):
    n=(Sueldo_bruto*0.15)+Sueldo_bruto
else:
    n=(Sueldo_bruto*0.12)+Sueldo_bruto
print("Nuevo sueldo",n)
