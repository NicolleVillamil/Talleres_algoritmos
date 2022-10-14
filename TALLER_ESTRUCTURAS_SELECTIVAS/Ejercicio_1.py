#Caja negra
inversion=int(input("Ingrese la inversion: "))
tasa_interes=float(input("Ingrese la tasa de interes: "))
#Caja negra
intereses=inversion*tasa_interes
ganancia_total=inversion+intereses
if(intereses>100000):
    print("El dinero por concepto de interes que obtiene es:",intereses,"(Intereses aptos para la reinversión)")
    print("Dinero total en la cuenta:",(ganancia_total))
else:
    print("El dinero por concepto de interes que obtiene es:",intereses)    

