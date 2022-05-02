consume=int(input("¿Consume licor? Digite 1 para si y 2 para No: "))
ag=0
ron=0
cvz=0
tq=0
wy=0
other=0
licor=0
listam=[]
listam.append(consume)
listalicor=[]
listaedad=[]
listacvz=[]
listawy=[]
listam=[]
listaf=[]
listap=[]
while True:
    if((consume==2)):
        print(f"Aguardiente {ag}\nRon {ron}\nCerveza {cvz}\nTequila {tq}\nwhisky {wy}\nOtro {other}")
        print(len(listam))
        print(len(listaf))
        print(sum(listam))
        print(sum(listap)/sum(listacvz))
        print(len(listawy)/len(listam))
        break
    elif(consume==1):
        edad=int(input("Ingrese su edad: "))
        listaedad.append(edad)
        sexo=str(input("Ingrese su genero. 1 para femenino y 2 para masculino: "))
        licor=int(input("1.Aguardiente, 2.Ron, 3.Cerveza, 4.Tequila, 5.Whisky, 6.Otro: "))
        listalicor.append(licor)
        print("Encuesta nueva")
        consume=int(input("Continuar el siguiente encuestado, 1 para sí, 2 para detener la encuesta: "))
        if(licor==1):
            ag=ag+1
        elif(licor==2):
            ron=ron+1 
        if(licor==3):
            cvz=cvz+1
            listacvz.append(cvz)
            if(licor==3 and edad>0):
                ed=edad
                listap.append(ed)
                continue
        if(licor==4):
            tq=tq+1
        if(licor==5):
            wy=wy+1
            listawy.append(wy)
        if(licor==6):
            other=other+1  
        elif(edad>=0):
            listaedad.append(edad)
            continue
        elif(edad<=18)and(sexo==1):
            tl=edad+sexo
            listaf.append(tl)
            continue
        elif(20>=edad<=25)and(sexo==2) and (licor!=5):
            sumaedsx=edad+sexo
            if(licor!=5):
                listam.append(sumaedsx)
            continue