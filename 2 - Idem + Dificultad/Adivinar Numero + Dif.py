#actividad: añadir dificultad facil y dificil
#faci= el numero secreto esta entre 1 y 20, tien seis intentos
#dificl = el numero secret esta entre 1 y 200, tiene siete intentos, utilizar el while cambia el valor secreto e intentos maximos
#-hay que validar la entrada
#-re
import random
jugar =1
dificultad = 1
ingresoValido=True
while jugar ==1:
    print("A continucacion ingrese la dificultad en la que desea jugar")
    print("[1]-Facil")
    print("[2]-Dificil")
    dificultad = int(input("-->"))
    if dificultad == 1:
        rangoMax = 20
        intentos = 6
    elif dificultad == 2:
        rangoMax = 200
        intentos = 7
    else:
        ingresoValido=False
        print("No se ingreso una dificultad valida")
        print("Desea intentar de nuevo? y/n")
        jugar = input("-->").capitalize
        
        
