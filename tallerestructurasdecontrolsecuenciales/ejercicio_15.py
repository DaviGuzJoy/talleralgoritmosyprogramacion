#Entradas
valor1=float(input("Ingrese el valor del costo oficial del producto: "))
valorpb=float(input("Ingrese el valor que corresponde de venta al publico: "))
#Caja Negra
valorf=valorpb*100/valor1
porcentajedesc=abs(valorf-100)
#Salidas
print(f"El porcentaje del producto con el descuento aplicado es de:{porcentajedesc}%")