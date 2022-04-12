#Entradas
n1=int(input("Ingrese la cantidad de billetes de 50000: "))
n2=int(input("Ingrese la cantidad de billetes de 20000: "))
n3=int(input("Ingrese la cantidad de billetes de 10000: "))
n4=int(input("Ingrese la cantidad de billetes de 5000: "))
n5=int(input("Ingrese la cantidad de billetes de 2000"))
n6=int(input("Ingrese la cantidad de billetes de 1000: "))
n7=int(input("Ingrese la cantidad de billetes de 500: "))
n8=int(input("Ingrese la cantidad de billetes de 100: "))
#Caja Negra
dinero1=n1*50000
dinero2=n2*20000
dinero3=n3*10000
dinero4=n4*5000
dinero5=n5*2000
dinero6=n6*1000
dinero7=n7*500
dinero8=n8*100
dinerof=dinero1+dinero2+dinero3+dinero4+dinero5+dinero6+dinero7+dinero8
#Salidas
print(f"El valor total del dinero que tiene el banco es de:{dinerof}COP")