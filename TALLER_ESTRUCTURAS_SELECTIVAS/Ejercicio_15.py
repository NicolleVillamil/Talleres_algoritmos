#entradas
edad=int(input("Ingrese su edad en meses: "))
sexo=input("Ingrese M (mujer) o H (hombre): ")
hemo=float(input("Igrese su nivel de hemoglobina: "))
#caja negra
rango="Positivo"
M="M"
H="H"
if(0<=edad<=1 and 13<=hemo<=26):
    rango="Negativo"
elif(1<edad<=6 and 10<=hemo<=18):
    rango="Negativo"
elif(6<edad<=12 and 11<=hemo<=15):
    rango="Negativo"
elif(12<edad<=60 and 11.5<=hemo<=15):
    rango="Negativo"
elif(60<edad<=120 and 12.6<=hemo<=15.5):
    rango="Negativo"
elif(120<edad<=180 and 13<=hemo<=15.5):
    rango="Negativo"
elif(edad>180 and 12<=hemo<=16 and sexo==M):
    rango="Negativo"
elif(edad>15 and 14<=hemo<=18 and sexo==H):
    rango="Negativo"
#Salida
print(rango)


