#actividad: añadir dificultad facil y dificil
#faci= el numero secreto esta entre 1 y 20, tien seis intentos
#dificl = el numero secret esta entre 1 y 200, tiene siete intentos, utilizar el while cambia el valor secreto e intentos maximos
#-hay que validar la entrada
#-re
import random
jugar =True
dificultad = 1
ingresoValido=True
jugarT=""
#^jugar Texto
while jugar ==True:
    print("A continucacion ingrese la dificultad en la que desea jugar")
    print("[1]-Facil (Del 1 al 20)")
    print("[2]-Dificil (Del  1 al 200)")
    dificultad = int(input("-->"))
    if dificultad == 1:
        print("[Dificultad - Facil]")
        rangoMax = 20
        intentos = 6
    elif dificultad == 2:
        print("[Dificultad - Dificil]")
        rangoMax = 200
        intentos = 7
    else:
        ingresoValido=False
        print("No se ingreso una dificultad valida")
    if ingresoValido==True:
        Nrandom=random.randint(1,rangoMax)
        for i in range(1,intentos,1):
            print("Quedan [" , (intentos-i) , "] intentos")
            print("Ingrese un numero a probar")
            intento = int(input("-->"))
            if intento == Nrandom:
                print("Adivino!")
                break
            elif intento>Nrandom:
                print("[Intento Fallido]")
                print("El numero ingresado es mayor al numero a adivinar")
            else:
                print("[Intento Fallido]")
                print("El numero ingresado es menor al numero a adivinar")
                
            print("#######################################")
    print("Desea intentar de nuevo?Y/N")
    jugarT=input("-->")
    jugarT=jugarT.capitalize
    if jugarT == "Y":
        jugar=True
    else:
        jugar=False
