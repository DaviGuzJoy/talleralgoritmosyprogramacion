archivo = open('paises.txt', 'r')
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M 
"""
lista=[]
ciudad=[]
c=0
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
    a="".join(lista)
    ciudad.append(a)
    lista=[]
  for i in ciudad:
    if(i[0]=="M"):
      c=c+1
      print(i)
print(c)
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
""""
lista=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  pais.append(a)
  lista=[]
for i in pais:
  if(i[0]=="U"):
    print(i)
    print("No existen capitales que inicien con la letra U en el texto:")
  """
#Cuente e imprima cuantos paises que hay en el archivo
""""
lista=[]
for i in archivo:
  lista.append(i)
print(len(lista))
"""
#Busque e imprima la ciudad de Singapur
"""
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  if(a[0]=="S" and a[7]=="r"):
    c=a.index(":")
    lista=[]
    break
  lista=[]
for i in range(c+2,len(a)):
  lista.append(a[i])
a="".join(lista)
print(a)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  if(a=="Venezuela"):
    break
  lista=[]
print(i)
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
lista=[]
ciudades=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudades.append(a)
  lista=[]
for i in ciudades:
  if(i[0]=="E"):
    print(i)
    lista.append(i)
print(len(lista))
"""
#Buesque e imprima la Capiltal de Colombia
"""
capitalcol=[]
cp=("Colombia: Bogotá")
a=cp.index(":")
r=(len(cp))
for i in range(a+1,r):
  capitalcol.append(cp[i])
bogogod="".join(capitalcol)
print(bogogod)
"""
#imprima la posicion del pais de Uganda
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a="".join(lista)
  c=c+1
  if(a=="Uganda: Kampala⧵n "):
    break
  lista=[]
print(c)
"""
#imprima la posicion del pais de Mexico
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1
  if(a=="México: Ciudad de México⧵n"):
    break
  lista=[]
print(c)
"""
#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
""""
lista=[]
for i in archivo:
  lista.append(i)
  new=open('paises.txt','w')
  for i in lista:
    if(i=="Madagascar: rey julien⧵n"):
      new.write("Madagascar: Antananarivo⧵n")
    else:
     new.write(i)
new.close()
"""
#Agregue un país que no esté en la lista 
"""
newcountry=open('paises.txt','a')
newcountry.write("⧵nAnor londo:pais ")
newcountry.close()
"""
archivo.close()
