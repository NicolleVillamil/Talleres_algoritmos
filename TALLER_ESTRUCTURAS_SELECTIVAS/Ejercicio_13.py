from datetime import datetime
from tokenize import single_quoted
hoy = datetime.now()
## de hoy
dia_actual=hoy.day
mes_actual=hoy.month
año_actual=hoy.year
#Entrada
fecha_nacimiento=input("poner en formato dd/mm/yy: ")
(dia,mes,año)=fecha_nacimiento.split("/")
dia_nacimiento=int(dia)
mes_nacimiento=int(mes)
año_nacimiento=int(año)
#Caja negra
#---------------Calcular edad------------
edad=0
if(mes_actual>mes_nacimiento):
    edad=año_actual-año_nacimiento
elif(mes_actual<mes_nacimiento):
    edad=(año_actual-año_nacimiento)-1
elif(mes_actual==mes_nacimiento):
    if(dia_actual<dia_nacimiento):
        edad=(año_actual-año_nacimiento)-1
    elif(dia_actual>dia_nacimiento):
        edad=(año_actual-año_nacimiento)
    elif(dia_actual==dia_nacimiento):
        edad=(año_actual-año_nacimiento)
print("la edad es:",edad,"años")
signo=""
if(dia_nacimiento>=21 and mes_nacimiento==1)or(dia_nacimiento<=19 and mes_nacimiento==2):
    signo="Acuario"
if(dia_nacimiento>=20 and mes_nacimiento==2)or(dia_nacimiento<=19 and mes_nacimiento==3):
    signo="Piscis"
if(dia_nacimiento>=21 and mes_nacimiento==3)or(dia_nacimiento<=20 and mes_nacimiento==4):
    signo="Aries"
if(dia_nacimiento>=21 and mes_nacimiento==4)or(dia_nacimiento<=21 and mes_nacimiento==5):
    signo="Tauro"
if(dia_nacimiento>=22 and mes_nacimiento==5)or(dia_nacimiento<=21 and mes_nacimiento==6):
    signo="Geminis"
if(dia_nacimiento>=22 and mes_nacimiento==6)or(dia_nacimiento<=22 and mes_nacimiento==7):
    signo="Cancer"
if(dia_nacimiento>=23 and mes_nacimiento==7)or(dia_nacimiento<=23 and mes_nacimiento==8):
    signo="Leo"
if(dia_nacimiento>=24 and mes_nacimiento==8)or(dia_nacimiento<=22 and mes_nacimiento==9):
    signo="Virgo"
if(dia_nacimiento>=23 and mes_nacimiento==9)or(dia_nacimiento<=22 and mes_nacimiento==10):
    signo="Libra"
if(dia_nacimiento>=23 and mes_nacimiento==10)or(dia_nacimiento<=21 and mes_nacimiento==11):
    signo="Escorpión"
if(dia_nacimiento>=22 and mes_nacimiento==11)or(dia_nacimiento<=21 and mes_nacimiento==12):
    signo="Sagitario"
if(dia_nacimiento>=22 and mes_nacimiento==12)or(dia_nacimiento<=20 and mes_nacimiento==1):
    signo="Capricornio"
print("El signo es:",signo)


