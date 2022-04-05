Algoritmo C_Velocidades
	escribir "Inserte velocidad km/h del vehiculo 1: "
	leer vc1
	escribir "Inserte velocidad km/h del vehiculo 2: "
	leer vc2
	escribir "Inserte distancia entre ambos vehiculos: "
	leer ditancia
	tiempo1<-distancia/vc1
	distancia1<-tiempo1*vc2
	tiempo<-(distancia1+distancia)/vc1
	tiempofinal<-redon(tiempo*60)
	escribir "Minutos que transcuriran para que los dos vehiculos se encuentren: " tiempofinal
	
FinAlgoritmo