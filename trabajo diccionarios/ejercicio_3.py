
usuarios = { 
    "iperurena": { 
            "nombre": "Iñaki", 
                "apellido": "Perurena", 
                "password": "123123" 
    }, 
    "fmuguruza": { 
        "nombre": "Fermín", 
            "apellido": "Muguruza", 
            "password": "654321" 
    }, 
    "aolaizola": { 
            "nombre": "Aimar", 
                "apellido": "Olaizola", 
                "password": "123456" 
    } 
} 
c=1
for i in usuarios:
    user=input("Ingrese su nombre y usuario: ")
    password=input("Ingrese su contraseña: ")
    if user in usuarios and (password==usuarios[user]["password"]):
        name=usuarios[user]["nombre"]
        name2=usuarios[user]["apellido"]
        print(name,name2)
        break
    else:
        if c==3:
            print("Maximo de intentos permitidos")
        c=c+1
