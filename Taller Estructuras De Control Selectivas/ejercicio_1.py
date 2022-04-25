#Entradas
cantidad=float(input("Inserte la cantidad invertida en el banco: "))
tasa=int(input("Inserte la tasa de interes: "))
#Caja Negra
interes=cantidad*tasa
if interes>100000:
    print(f"Los interes ganados son ",(interes),"superan los 100000: ")
else:
    print(f"Los interes ganados son",(interes),"no superan los 100000")

print(f"El saldo total de la cuenta es:",(cantidad+interes))

