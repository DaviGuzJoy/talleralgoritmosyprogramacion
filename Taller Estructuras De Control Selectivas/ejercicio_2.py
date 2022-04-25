"""
suledo-->float-->sueldo

"""
#Entradas
sueldo=float(input("Ingrese el valor del sueldo: "))
#Caja Negra
if(sueldo<=900000):
    aumento=(sueldo*0.15)+sueldo
    print(f"El nuevo sueldo sera de:{sueldo}")
elif(sueldo>=900000):
    sueldo=(sueldo*0.12)+sueldo
    print(f"El nuevo sueldo sera de:{sueldo}")

