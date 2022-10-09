import math
#Entradas
ladoa=float(input("Ingrese el lado a: "))
ladob=float(input("Ingrese el lado b: "))
ladoc=float(input("Ingrese el lado c: "))
#Caja negra
s=(ladoa+ladob+ladoc)/2
area=math.sqrt(s*(s-ladoa)*(s-ladob)*(s-ladoc))
#Salida
print("El area es:",area)
