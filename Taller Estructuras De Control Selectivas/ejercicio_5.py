"""
sueldo-->float-->sueldo
resd1-->float-->resd1
resd1--?float-->resd2
resd3-->float-->resd3
"""
#Entradas
sueldo=float(input("Ingrese el sueldo: "))
resd1=float(input("Las ventas de la residencia nr1: "))
resd2=float(input("Las ventas de la residencia nr2: "))
resd3=float(input("Las ventas de la residencia nr3: "))
#Caja Negra
ventas=(resd1+resd2+resd3)
profit=(ventas*0.33)
sueldoplus=(sueldo*0.20)+sueldo
if(resd1>profit):
    print(f"El sueldo respecto a la residencia 1 es:{sueldoplus}")
else:
    print(f"El sueldo respecto a la residencia 2 es:{sueldo}")
if(resd2>profit):
    print(f"El sueldo respecto a la residencia 2 es:{sueldoplus}")
else:
    print(f"El sueldo respecto a la residencia 2 es:{sueldo}")
if(resd3>profit):
    print(f"El sueldo respecto a la residencia 3 es:{sueldoplus}")
else:
    print(f"El sueldo respecto a la residencia 3:{sueldo}")#Caja Negra
