#Entradas
nombre=str(input("Ingrese su nombre completo:"))
horas=float(input("Ingrese las horas trabajadas: "))
pago_hora=float(input("Ingrese el pago de 1 hora normal: "))
extras=float(input("Ingrese las horas extras: "))
hijos=int(input("Ingrese la cantidad de hijos: "))
#Caja negra
Sueldo_base=horas*pago_hora
Asignacion=250000+(173000*hijos)+180000
deducciones=Sueldo_base*(0.05+0.02+0.07)
sueldo_deducido=Sueldo_base-deducciones
horas_extras=horas*extras
mm=horas_extras*0.25+horas_extras
sueldo_neto=sueldo_deducido+Asignacion+mm
#Salidas
print("Las asignaciones son:",Asignacion)
print("Las deducciones son:",deducciones)
print("El Sueldo neto es:",sueldo_neto)
