#Entradas
ca=int(input("ingrese la cantidad de chelines austriacos: "))
dg=int(input("ingrese la cantidad de dracmas griegos: "))
p=int(input("ingrese la cantidad de pesetas: "))
#Caja negra
ca=(ca*956.871)/100
dg=((dg*88.607)/100)*(1/20.110)
p_d=(p*1)/122.499
p_l=(p*100)/9.289
#Salida
print("Chelines austricos a pesetas es:",ca)
print("Dracmas griegos a francos franceses es:",dg)
print("Pasetas a dolares es:",p_d)
print("Pasetas a liras italianas es:",p_l)