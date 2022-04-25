"""
Km-->float-->km
"""
#Entradas
km=float(input("Ingrese la cantidad de kilometros: "))
#Caja Negra
if(km<300):
    valor=50000
    print(f"Lo que se cancela es:{valor}")
elif(km>1000):
    valor=(km-1000)*(9000+150000)
    print(f"Lo que se cancela sera:{valor}")