#Entradas
precio_producto=float(input("Ingrese el precio pagado del producto: "))
pvp=float(input("Ingrese el precio de venta al publico: "))
#Caja negra
dto=((pvp-precio_producto)/pvp)*100
#Salida
print("El % de descuento es:",dto)