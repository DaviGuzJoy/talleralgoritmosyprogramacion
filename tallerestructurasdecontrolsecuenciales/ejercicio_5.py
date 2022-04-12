#Entradas
parcial1=float(input("Resultado de la primera calificacion: "))
parcial2=float(input("Resultado de la segunda calificacion: "))
parcial3=float(input("Resultado de la tercera calificacionL: "))
examenf=float(input("Resultado del examen final: "))
trabajo=float(input("Resultado trabajo final: "))
#Caja Negra
parciales=(parcial1+parcial2+parcial3)/3*0.55
examen=examenf*0.30
trabajof=trabajo*0.15
notaf=parciales+examen+trabajof
print(f"El resultado final es:{notaf}")