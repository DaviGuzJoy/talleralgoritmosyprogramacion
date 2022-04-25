import math
"""
Lectura actual-->int-->anualr
Lectura anterior-->int--lastr
"""
anualr=int(input("Lectura actual de luz: "))
lastr=int(input("Lectura anterior de luz: "))
#caja negra
value=abs(anualr-lastr)
value1=""
if (value>=0 and value<=100):
    value1=vl*4600
    print(f"Debe pagar: {value1}")
elif value>=101 and value<=300:
    value1=vl*80.00
    print(f"Debe pagar: {value1}")
elif (value>=301 and value<=500):
    value1=(value*100000)
    print(f"Debe pagar: {value1}")
elif (value>=501):
    value1=(value*120000)
    print(f"Debe pagar: {value1}")