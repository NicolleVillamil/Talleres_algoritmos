Algoritmo Velocidades
	//Entradas
	Escribir "Digite la velocidad de 1 vehiculo(km/h)"
	Leer v1
	Escribir "Digite la velocidad del 2 vehiculo(km/h)"
	Leer v2
	Escribir "Digite la distancia entre los vehiculos(km)"
	Leer d 
	//Caja negra
	t<-abs(d/(v1-v2)) 
	tmin<-t*60
	//Salida
	Escribir "Tiempo en que el vehiculo lento alcanzara al rapido es " tmin "min"
FinAlgoritmo