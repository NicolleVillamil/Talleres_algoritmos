Algoritmo inicio_horas
	//Entrada
	Escribir "Digite los minutos"
	Leer min 
	//caja negra
	h<-trunc(min/60)
	min<-trunc(min MOD 60)
	//salida
	Escribir "Horas:" h " Minutos:" min
FinAlgoritmo
