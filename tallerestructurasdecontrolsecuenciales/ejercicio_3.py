#Entradas
sueldo=float(input("Ingrese valor del sueldo base: "))
venta1=float(input("Valor de la primera venta: "))
venta2=float(input("Valor de la segunda venta: "))
venta3=float(input("Valor de la tercera venta: "))
#Caja Negra
comision=(venta1*0.10)+(venta2*0.10)+(venta3*0.10)
sueldot=sueldo+comision
print(f"El valor total de las comisiones:{comision} ")
print(f"El sueldo total en el mes es:{sueldot}")
