"""
Dividendo-->int-->D
Divisor-->int-->P
Restante-->int-->rt
Cociente-->int-->ct
"""
#Entradas
D=int(input())
p=int(input())
rt=0
ct=0
while(D>=p):
    D-=p
    rt=D
    ct+=1
print(ct)
print(rt)