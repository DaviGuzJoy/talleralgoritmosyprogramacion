#Entradas
naranjas=int(input("Ingrese la cantidad de naranjas: "))
docena=float(input("Ingrese el valor de la docena de naranjas: "))
profit=float(input("Ingrese el valor de las ganancias: "))
#Caja Negra
dinero=docena/12*naranjas
dinero2=dinero+profit
porcentaje=dinero2*100/dinero
porcentajefinal=porcentaje-200
#Salidas
print(f"El porcentaje de la ganancia obtenia{porcentajefinal}")