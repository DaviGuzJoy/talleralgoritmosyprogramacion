"""
categoria-->int-->ct
sueldo-->float-->sueldo
aumento+salario bruto
"""
#Entradas
ct=int(input("Inserte la categoria en la que se encuentra el trabajador: "))
sueldo=float(input("Ingrese el sueldo del trabajor: "))
#Caja Negra
if(ct==1):
    value=(sueldo*0.10+sueldo)
    print(f"categoria{ct}\n salario bruto: {value}")
elif(ct==2):
    value=(sueldo*0.15+sueldo)
    print(f"categoria{ct}\n Salario bruto:{value}")
elif(ct==3):
    value=(sueldo*0.20+sueldo)
    print(f"Categoria{ct}\n salario bruto: {value}")
elif(ct==4):
    value=(sueldo*0.40+sueldo)
    print(f"categoria{c}\n salario bruto:{value}")
elif(ct==5):
    value=(sueldo*0.60+sueldo)
    print(f"categoria {ct}\n salario bruto: {value}")


