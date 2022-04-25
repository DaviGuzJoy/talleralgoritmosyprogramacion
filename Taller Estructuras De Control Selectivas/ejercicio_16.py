import math
"""
a-->float-->a
B-->float-->b
C-->float-->c
#Salidas
x1-->float-->x1
"""
#Entradas
a=float(input("Digite A: "))
b=float(input("Digite B: "))
c=float(input("Digite C: "))
#Caja Negra
d=b**2-(4*a*c)
x1=0.0
x2=0.0
if(d>0):
    x1=(-b+math.sqrt(b**2-4*a*c))

