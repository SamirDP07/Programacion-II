#
#Actividad de adivinar el número
#
import random
numeroS=random.randint(1,20)
#numero secreto^
print("[Intente adivinar un numero entre uno y veinte]")
for i in range(1,6,1):
    print("[Tiene ",6-i," intentos restantes]")
    print("[Ingrese un numero a probar]")
    intento=int(input("-->"))
    if intento == numeroS:
        print("[Adivinó!]")
        break
    elif intento>numeroS:
        print("[El numero que probo es mayor al numero secreto]")
    else:
        print("[El numero que probo es menor al numero secreto]")
    if i==6:
        print("[Se ha quedado sin intentos]")
