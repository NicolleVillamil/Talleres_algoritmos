#Entradas
Matematicas=float(input("Ingrese la nota del examen de matematicas: "))
Mate_T1=float(input("Ingrese la nota de la tarea 1 de matematicas: "))
Mate_T2=float(input("Ingrese la nota de la tarea 2 de matematicas: "))
Mate_T3=float(input("Ingrese la nota de la tarea 3 de matematicas: "))
Fisica=float(input("Ingrese la nota del examen de fisica: "))
Fisica_T1=float(input("Ingrese la nota de la tarea 1 de fisica: "))
Fisica_T2=float(input("Ingrese la nota de la tarea 2 de fisica: "))
Quimica=float(input("Ingrese la nota del examen de quimica: "))
Quimica_T1=float(input("Ingrese la nota de la tarea 1 de quimica: "))
Quimica_T2=float(input("Ingrese la nota de la tarea 2 de quimica: "))
Quimica_T3=float(input("Ingrese la nota de la tarea 3 de quimica: "))
#Caja negra
Mp=Matematicas*0.9+(((Mate_T1+Mate_T2+Mate_T3)/3)*0.1)
Fp=Fisica*0.8+((Fisica_T1+Fisica_T2)/2*0.2)
Qp=Quimica*0.85+(((Quimica_T1+Quimica_T2+Quimica_T3)/3)*0.15)
Gp=(Mp+Fp+Qp)/3
#Salidas
print("El promedio de Matemáticas es:",Mp)
print("El promedio de Física:",Fp)
print("El promedio de Química:",Qp)
print("El promedio general es:",Gp)
