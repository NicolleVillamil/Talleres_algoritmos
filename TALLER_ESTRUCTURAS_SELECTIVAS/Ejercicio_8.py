#entrada
P=int(input())
Q=int(input())
#caja negra
if((P**3+Q**4-2*P**2)>680):
    print("P="+str(P)+" y Q="+str(Q)+" Satisfacen la expresión")
else:
    print("P y Q no Satisfacen la expresión")