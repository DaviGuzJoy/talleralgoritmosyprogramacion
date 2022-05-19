
estudiantes = { 
    "1": { 
    "nombre": "Lorea", 
    "nota": 8 
    }, 
    "2": { 
    "nombre": "Markel", 
    "nota": "4.2" 
    }, 
    "3": { 
    "nombre": "Julen", 
    "nota": 6.5 
    } 
} 
c=0
win=[]
lose=[]
medianotas=[]
for i in range (0,10):
    stname=input("ingrese el nombre del estudiante: ")
    stnota=float(input("Nota del estudiante: "))
    c=c+1
for key in estudiantes:
    nombre=estudiantes[key]["nombre"]
    nota=estudiantes[key]["nota"]
    if (nota<6):
        lose.append(nombre)
    else:
        win.append(nombre)
    medianotas.append(nota)
print("Estos son los estudiantes suspendidos".join(lose))
print("Estos son los estudiantes que aprobaron".join(win))
print("Media de notas de los estudiantes",round(sum(medianotas)/len(medianotas),2))


    
    
    
