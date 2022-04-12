#Entradas
nombre=str(input("Inserte el nombre del trabajador: "))
numeroh=int(input("Inserte el numero de horas: "))
pagoxh=float(input("Inserte el valor del pago por hora: "))
horasplus=int(input("Inserte la cantidad de horas extra: "))
hijost=int(input("Inserte la cantidad de hijos: "))
hp=pagoxh*0.25+pagoxh
pagotr=(numeroh*pagoxh)+(hp*horasplus)
deducciones=pagotr-pagotr*0.14
asignaciones=250000+180000+173000*hijost
sueldon=pagotr+asignaciones-deducciones
print(f"El sueldo netro es:{sueldon}")
print(f"El total de asignaciones es:{asignaciones}")
print(f"El total de las deducciones es:{deducciones}")