import random
from turtle import goto
numa=random.randint(1,20)
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
