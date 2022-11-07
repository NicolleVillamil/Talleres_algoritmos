c=0
L=0
E=0
S=0
P=0
M=0
H=0
I=0
while True:
    P+=1
    consume=int((input("¿Consume Licor? Ingrese\n 1-Si ó 0-No: " )))
    K=int(input("¿Cual es su licor preferido? Ingrese\n 1-Aguardiente 2-Ron 3-Cerveza 4-Tequila 5-Whisky 6-Otro: "))
    Edad=int(input("Ingrese su edad: "))
    sexo=int((input("Ingrese\n 1-Mujer ó 0-Hombre: " )))
    S=int(input("Si desea continuar ingrese\n 1-Si ó 2-No: "))
    if(consume==1):
        c=c+1
    if(K==3 and consume==1):
            L=L+1
            I=I+Edad
    if(K==5):
        E=E+1
    if((consume==1 or consume==0 ) and sexo==1 and Edad<18):
        M+=1
    if(sexo==0 and Edad>=20 and Edad<=25 and consume==1):
        if(K!=1):
            H=H+1
            W=H+M
    if(S==2):
            break
print("Cantidad de encuestados:",P)
print("Personas que consumen licor:",c)
print("Mujeres menores de edad:",M)
print("Hombres que no consumen aguardiente y su edad esta entre 20 y 25 años:",H)
if(L==0):
    print("Ningun encuestado consume cerveza")
if(K==5):
    print("El porcentaje de personas que consumen wisky:",round((E/P)*100,2))
print("Promedio de las personas que consumen cerveza:",round(I/L,2))










