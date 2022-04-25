from datetime import datetime
#Sacar la fecha actual del sistema
ahora= datetime.now()
año_actual=ahora.year
mes_actual=ahora.month
dia_actual=ahora.day
#Pedir la fecha de nacimiento con el formato incluido en el pc
fecha_nacimiento=input("Digite fecha de nacimiento: ")
año_nacimiento,mes_nacimiento,dia_nacimiento=fecha_nacimiento.split("/")
año_nacimiento=int(año_nacimiento)
mes_nacimiento=int(mes_nacimiento)
dia_nacimiento=int(dia_nacimiento)
#Calcular la edad
edad=0
edad=año_actual-año_nacimiento
#Calcular signo
zodiaco=""
if((mes_nacimiento>=11 and dia_nacimiento>=22)and (mes_nacimiento<=12 and dia_nacimiento<=21)):
    zodiaco="Sagitario"
elif((mes_nacimiento>=12 and dia_nacimiento>=22)and (mes_nacimiento<=1 and dia_nacimiento<=20)):
    zodiaco="Capricornio"
elif((mes_nacimiento>=1 and dia_nacimiento>=21)and (mes_nacimiento<=2 and dia_nacimiento<=19)):
    zodiaco="Acuario"
elif((mes_nacimiento>=2 and dia_nacimiento>=20)and (mes_nacimiento<=3 and dia_nacimiento<=19)):
    zodiaco="Piscis"
elif((mes_nacimiento>=3 and dia_nacimiento>=21)and (mes_nacimiento<=4 and dia_nacimiento<=20)):
    zodiaco="Aries"
elif((mes_nacimiento>=4 and dia_nacimiento>=21)and (mes_nacimiento<=5 and dia_nacimiento<=21)):
    zodiaco="Tauro"
elif((mes_nacimiento>=5 and dia_nacimiento>=22)and (mes_nacimiento<=6 and dia_nacimiento<=21)):
    zodiaco="Geminis"
elif((mes_nacimiento>=6 and dia_nacimiento>=22)and (mes_nacimiento<=7 and dia_nacimiento<=22)):
    zodiaco="Cancer"
elif((mes_nacimiento>=7 and dia_nacimiento>=23)and (mes_nacimiento<=8 and dia_nacimiento<=23)):
    zodiaco="Leo"
elif((mes_nacimiento>=8 and dia_nacimiento>=24)and (mes_nacimiento<=9 and dia_nacimiento<=22)):
    zodiaco="Virgo"
elif((mes_nacimiento>=9 and dia_nacimiento>=23)and (mes_nacimiento<=10 and dia_nacimiento<=22)):
    zodiaco="Libra"
elif((mes_nacimiento>=10 and dia_nacimiento>=23)and (mes_nacimiento<=11 and dia_nacimiento<=21)):
    zodiaco="Escorpio"
print(f"La edad y signo del zodiaco es", (edad)(zodiaco))
