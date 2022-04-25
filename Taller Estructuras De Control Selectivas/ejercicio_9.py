import math
"""
nombre-->str-->nombrec
value-->float-->value
"""
nombrec=(input("Ingrese nombre: "))
value=float(input("Ingrese el valor de la compra realizada: "))
#Caja Negra
if(value<50000):
    print("No se aplicara el descuento")
elif(value>=50000 and value<=100000):
    value1=abs(value*0.5-value)
    print(f"Nombre:{nombrec}\n {value}\n Valor final:{value1} Un descuento del 5%")
elif(value>=100000 and value<=700000):
    value1=abs(value*0.11-value)
    print(f"Nombre:{nombrec}\n {value}\n Valor final:{value1} un descuento del 11%")
elif(value>=700000 and value<=15000000):
    value1=abs(value*0.18-value)
    print(f"Nombre{nombrec}\n {value}\n valor final: {value1} un desucneto del 18%")
elif(value>1500000):
    value1=abs(value*0.25-value)
    print(f"nombre {nombrec}\n {value}\n valor final:{value1}un descuento del 25%")