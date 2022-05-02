"""
Incremento xp-->int-->x
Cantidad de xp por mob-->m
"""
while True:
    x,m=input().split()
    if(x == '0' and m == '0'):
        break
    print(int(x)*int(m))