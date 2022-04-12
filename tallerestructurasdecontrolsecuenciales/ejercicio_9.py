#ENTRADASa
horast=int(input("Ingres la cantidad de horas trabajadas: "))
precioh=float(input("Ingrese el valor por hora trabajada: "))
#Caja Negra
salariob=horast*precioh
descuento=salariob*0.20
salarion=salariob-descuento
#Salidas
print(f"El salario netro del trabajor es:{salarion} ")