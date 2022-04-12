#Entradas
preciopc=float(input("Ingrese el precio del computador: "))
preciopcC=float(input("Ingrese el precio del computador pagado en cuotas: "))
#Caja Negra
pc=preciopc/12
pcc=preciopcC/12
valorf=pcc*100/pc
porcentaje=abs(valorf-100)
#Salidas
print(f"El porcentaje del interes por la cuota sobre el valor del computador es:{porcentaje}%")
