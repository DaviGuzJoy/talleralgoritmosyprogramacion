import math
#Entradas
a=float(input("Ingrese lado a: "))
b=float(input("Ingrese lado b: "))
c=float(input("Ingrese lado c: "))
#Caja Negra
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#Salidas
print("El area es: ",round(area,2))

