#Entrada
mujeres=int(input("Digite cantidad de mujeres: "))
hombres=int(input("Digite cantidad de hombres: "))
#Caja Negra
total_estudiantes=mujeres+hombres
mp=(mujeres*100)/total_estudiantes
hp=(hombres*100)/total_estudiantes
#Salidas
print(f"El porcentaje de mujeres: {round(mp,2)} y el procentaje de hombres{round(hp,2)}")