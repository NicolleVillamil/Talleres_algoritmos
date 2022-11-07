N=int(input("Cantidad de estudiantes: "))
notafinal=0
sumanota=0
e=0
f=0
a=" "
b=" "
c=0
for i in range (1,N+1):
    nombre=input("Nombre del estudiante: ")
    p_f=float(input("Puntaje final: "))
    sumanota=p_f+sumanota
    if(notafinal<=p_f):
        notafinal=p_f
        a=nombre
    if(notafinal>p_f):
        c=p_f
        b=nombre
print("Estudiante con mayor puntaje final:",a)
print("Estudiante con menor puntaje final:",b)
print("Máximo puntaje obtenido:",notafinal)
print("Mínimo puntaje obtenido:",c)
print("Promedio puntajes:",round(sumanota/N,2))