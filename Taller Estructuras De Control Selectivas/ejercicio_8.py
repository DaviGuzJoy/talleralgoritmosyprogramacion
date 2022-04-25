"""
P-->int-->P
Q-->int-->Q
"""
#Entradas
P=int(input())
Q=int(input())
#Caja Negra
expre=(P**3+Q**4-2*P**2)
if (expre>680):
    print(f"El valor sera:{expre}","y P y Q satisfacen la expresion")
else:
    print(f"El valor sera:{expre}","y P y Q no logran satisfacer la expresion")

