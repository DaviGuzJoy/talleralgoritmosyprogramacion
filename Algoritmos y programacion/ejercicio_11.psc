Algoritmo C_Calificaciones
	Escribir "Inserte valor de la primera calificacion parcial: "
	leer parcial1
	Escribir "Inserte valor de la segunda calificacion parcial: "
	leer parcial2
	Escribir "Inserte valor de la tercer calificacion parcial: "
	leer parcial3
	Escribir "Inserte calificacion del examen final: "
	leer examenf
	escribir "Inserte calificacion trabajo final; "
	leer trabajof
	parciales<-(parcial1+parcial2+parcial3)/3*0.55
	eva<-examen*0.30
	proyecto<-trabajo*0.15
	final<-parciales+eva+proyecto
	Escribir "Nota final de la asignatura: " final 
	
FinAlgoritmo