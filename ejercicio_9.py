d1=0
d2=0
d3=0
while(True):
    a=int(input())
    if(a == 4):
        break
    else:
        if (a == 1):
            d1 +=1
        elif (a == 2):
            d2+=1
        elif (a == 3):
            d3+=1
        else:
            continue
print("MUITO OBRIGADO")
print("Alcool:",d1)
print("Gasolina:",d2)
print("Diesel:",d3)