	Algoritmo inicio_calificaciones
	//Entradas
	Escribir "Dijite su nota del 1 parcial"
	Leer parcial1
	Escribir "Dijite su nota del 2 parcial"
	Leer parcial2
	Escribir "Dijite su nota del 3 parcial"
	Leer parcial3
	Escribir "Dijite su nota del examen final"
	Leer examen_final
	Escribir "Dijite su nota del trabajo final"
	Leer Trabajo_final
	//Caja negra
	pp<-((parcial1+parcial2+parcial3)/3)*0.55
	ef<-examen_final*0.3
	tf<-Trabajo_final*0.15
	nota<-pp+ef+tf
	//Salida
	Escribir "Nota final:" nota	
FinAlgoritmo
