#eNTRADAS
cantidad=int(input("Digite cantidad de estudiantes: "))
altura_mayor=0
for i in range (1,cantidad+1):
    #Entrada
    altura=float(input("Digite la altura: "))
    #Caja Negra
    if(altura_mayor<=altura):
        altura_mayor=altura
print(altura_mayor)


#cl=str(input("Consume licor, Y para si o N para no: "))