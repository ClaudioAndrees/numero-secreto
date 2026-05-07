import random
try:
    minimo = int(input("Límite inferior: "))
    maximo = int(input("Límite superior: "))
 
 
    num_base = random.randint(minimo,maximo)
    #generamos un número cualquiera y lo ajustamos al múltiplo de 3
    secreto = (num_base //3) * 3
    #Si el ajuste se sale del rango, lo movemos hacia adentro del rango
    if secreto < minimo:
        secreto +=3
    elif secreto > maximo:
        secreto -= 3
    #-- Intento 1 -- 
    intento = int(input("ingresa el primer intento: "))
    if intento == secreto:
        print("Adivinastes")
        exit()
    pista_orden = "MAYOR" if secreto > intento else "MENOR"
    print(f"Pista: El número es {pista_orden}")
   ###
   # if secreto > intento:
   #     print("el numero es mayor")
   # else:
   #     print("El numero es menor")
   ###
    error1 = abs(secreto - intento)
    #-- Intento 2 --
    intento = int(input("ingresa el segundo intento: "))
    if intento == secreto:
        print("Adivinastes")
        exit()
    error2 = abs(secreto -intento)
    cercania = "Más cerca" if error2 < error1 else "Más lejos"
    print(f"Cercania: {cercania} del segundo intento")
    pista_orden = "MAYOR" if secreto > intento else "MENOR"
    print(f"Pista: El número es {pista_orden}")
 
 
    #--Intento 3 ---
    intento = int(input("ingresa el tercer intento: "))
    if intento == secreto:
        print("Ganastes")
    else:
        print(f"Perdistes, el número era:{secreto}")
except ValueError:
    print("Error de valores")