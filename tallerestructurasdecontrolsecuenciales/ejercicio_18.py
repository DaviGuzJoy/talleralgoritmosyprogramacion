#Entradas
capital=float(input("Ingrese la cantidad del prestamo: "))
Tasaint=float(input("Ingrese la tasa de interes: "))
#Caja Negra
interes=(capital*4*Tasaint)/100
#Salidas
print(f"El cobro en intereses por el prestamo da un valor en Bolivares de:{interes}")