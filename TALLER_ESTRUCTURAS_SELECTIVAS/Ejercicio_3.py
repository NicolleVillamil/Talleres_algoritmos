#entradas
A=int(input("A: "))
B=int(input("B: "))
C=int(input("C: "))
D=int(input("D: "))
#Caja negra
if(D==0):
    si=(A-C)**2
    print(si)
if(D>0):
    no=((A-B)**3)/D
    print(no)
