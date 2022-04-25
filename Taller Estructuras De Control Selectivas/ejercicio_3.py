"""
A-->int-->A
B-->int-->B
C-->int-->C
D-->int-->D
"""
#Entradas
A=int(input())
B=int(input())
C=int(input())
D=int(input())
#Caja Negra
if D==0:
    op=(A-C)**2
    print(f"resultado:{op}")
elif(D>0):
    op=(A-C)**3/D
    print(f"resultado:{op}")
    





