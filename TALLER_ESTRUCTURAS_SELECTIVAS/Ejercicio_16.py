from cmath import sqrt
import math
#Entrada
from tokenize import Double
datos=input()
(a,b,c)=datos.split(" ")
a=float(a)
b=float(b)
c=float(c)
#caja negra
raiz=(b**2-4*a*c)
if(raiz<0 or a==0):
   print("Impossivel calcular")
else:
   R1=(-b+sqrt(raiz))/(2*a)
   R2=(-b-sqrt(raiz))/(2*a)
   print("R1 = "+str("{:.5f}".format(R1) ))
   print("R2 = "+str("{:.5f}".format(R2) ))
