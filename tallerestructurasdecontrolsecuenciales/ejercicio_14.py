#Entradas
luzbf=int(input("Ingrese los kilovatios en la lectura anterior: "))
luzaf=int(input("Ingrese los kilovatios en la lectura actual: "))
valorkv=float(input("Ingrese el valor de el kilovatio: "))
#Caja Negra
valorluzbf=luzbf*valorkv
valorluzaf=luzaf*valorkv
valorf=abs(valorluzaf-valorluzbf)
#Salidas
print(f"El monto de la luz de la lectura pasada fue:{valorluzbf} ")
print(f"El monto de la luz en la lectura actual es:{valorluzaf}")
print(f"La diferencia entre los valores es de:{valorf}")