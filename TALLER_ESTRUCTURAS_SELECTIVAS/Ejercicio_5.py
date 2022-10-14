#entradas
VenA=int(input("Ventas del departamento A: "))
VenB=int(input("Ventas del departamento B: "))
VenC=int(input("Ventas del departamento C: "))
Sueldo_bt=int(input("Ingrese el sueldo bruto mensual del trabajador: "))
#caja negra
Ven_total=VenA+VenB+VenC
incentivo=Ven_total*0.33
if(VenA>incentivo):
    sueldoA=(Sueldo_bt*0.2)+Sueldo_bt
else:
    sueldoA=Sueldo_bt
print("El pago a los vendedores del departamento A es:",sueldoA)
if(VenB>incentivo):
    sueldoB=(Sueldo_bt*0.2)+Sueldo_bt
else:
    sueldoB=Sueldo_bt
print("El pago a los vendedores del departamento B es:",sueldoB)
if(VenC>incentivo):
    sueldoC=(Sueldo_bt*0.2)+Sueldo_bt
else:
    sueldoC=Sueldo_bt
print("El pago a los vendedores del departamento C es:",sueldoC)


