#entrada
A=int(input())
B=int(input())
C=int(input())
D=int(input())
#caja negra
if(C<=5):
    um=A*1000
    d=B*100
    N=um+d
else:
    um=A*1000
    d2=(B+1)*100
    N=um+d2
print("El numero redondeado es:",N)
