a12=[]
suma=0
for i in range(1,13):
    x=(5*i)+1
    a12.append(x)
for i in range(12):
    suma+=a12[i]
assert (a12[11]==61 and suma==402)
print("Prueba superada😎")