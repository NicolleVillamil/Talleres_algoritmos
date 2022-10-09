#Entradas
hombres=int(input("Ingrese la cantidad de hombres en el grupo:"))
mujeres=int(input("Ingrese la cantidad de mujeres en el grupo:"))
#Caja negra
total=hombres+mujeres
ph=(hombres/total)*100
pm=(mujeres/total)*100
#Salidas
print("Este es el porcentaje de hombres",ph)
print("Este es el porcentaje de mujeres",pm) 