Algoritmo inicio_ventas
	//Entrada
	Escribir "Digite su saldo base"
	Leer sueldo_base
	Escribir "Dijite el valor de su primer venta"
	Leer venta1
	Escribir "Dijite el valor de su segunda venta"
	Leer venta2
	Escribir "Dijite el valor de su tercera venta"
	Leer venta3
	//Caja negra
	comision<-(venta1+venta2+venta3)*0.1
	pago_final<-comision+sueldo_base
	//Salidas
	Escribir "Comision: " comision 
	Escribir "Pago total: " pago_final
FinAlgoritmo
