#Entradas
horas = float (input ('Ingrese las horas trabajadas: '))
pago_hora = float (input ('Ingrese el pago por 1 hora: '))
#Caja negra
sueldo_base=horas*pago_hora
impuestos=sueldo_base*0.20
sueldo_neto=sueldo_base-impuestos
#Salida
print("El sueldo neto a recibir es",sueldo_neto)