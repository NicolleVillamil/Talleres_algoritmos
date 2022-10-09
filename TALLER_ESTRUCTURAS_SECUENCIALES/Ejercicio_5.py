#Entradas
parcial1=float(input("Ingrese su nota del 1 parcial: "))
parcial2=float(input("Ingrese su nota del 1 parcial: "))
parcial3=float(input("Ingrese su nota del 1 parcial: "))
examen_final=float(input("Ingrese su nota del examen final: "))
trabajo_final=float(input("Ingrese su nota del trabajo final: "))
#Caja negra
pp=((parcial1+parcial2+parcial3)/3)*0.55
ef=examen_final*0.3
tf=trabajo_final*0.15
nota=pp+ef+tf
#Salida
print("La nota final es:",nota)