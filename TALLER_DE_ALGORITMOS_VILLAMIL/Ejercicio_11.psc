Algoritmo inicio_calificaciones
	//Entradas
	Escribir "Dijite su promedio de los 3 parciales"
	Leer promedio_parciales
	Escribir "Dijite su nota del examen final"
	Leer examen_final
	Escribir "Dijite su nota del trabajo final"
	Leer Trabajo_final
	//Caja negra
	pp<-promedio_parciales*0.55
	ef<-examen_final*0.3
	tf<-Trabajo_final*0.15
	nota<-pp+ef+tf
	//Salida
	Escribir "Nota final:" nota	
FinAlgoritmo
