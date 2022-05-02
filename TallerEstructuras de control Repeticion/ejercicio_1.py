"""
Numero1-->int-->N
Numero2-->int-->K
int(N,K)-->int-->k HALLAR K
"""
#Entradas
N=int(input(" "))
K=int(input(" "))
#Caja Negra
while(K>=N):
    print("\nN El valor debe ser mayor a K")
    N=int(input("Ingresar de nuevo el valor N: "))
    K=int(input("Ingresar de nuevo el valor K: "))
R=(N-K+1)
for i in range (R-1):
    N-=1
    print(N)