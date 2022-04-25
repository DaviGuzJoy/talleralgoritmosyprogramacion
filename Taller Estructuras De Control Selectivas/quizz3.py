#Ejercicio ajedrez, colores por cuadrado
#Entradas
L=int(input())
C=int(input())
#Caja Negra y Salidas para simplicar el proceso
if (L%2!=0):
    if (C%2!=0):
        print("#FFFFFF")
    else:
        print("#000000")
elif (L%2==0):
    if (C%2==0):
        print("#FFFFFF")
    else:
        print("#000000")
