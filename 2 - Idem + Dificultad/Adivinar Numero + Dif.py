#actividad: añadir dificultad facil y dificil
#faci= el numero secreto esta entre 1 y 20, tien seis intentos
#dificl 0 el numero secret esta entre 1 y 200, tiene siete intentosutilizar el while cambia el valor secreto e intentos maximos
#-hay que validar la entrada
#-re
import random
from turtle import goto
numa=random.randint(1,20)
jugar=1
print("¿En qué dificultad desea jugar?")
print("[1]-Fácil")
print("[2]-Difícil")
dif=int(input("-->" ))
while jugar==1:

    for intentos in range (6,1,-1):
        numi=int(input("Intente adivinar un número entre el 1 y el 20 ", ))
        if numi==numa:
            break
        else:
            print("No adivino! ",intentos," intentos restantes.")
            if numa>numi:
                print("El número es mayor al correcto")
            else:
                print("El número es menor al correcto")
    print("¡Lo adivino, el numero era ", numi ,"!")
