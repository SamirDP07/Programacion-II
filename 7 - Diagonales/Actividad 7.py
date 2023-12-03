#Declare una matriz de 4x4
#Realize una funcion que devuelva la suma de la diagonal principal y otra que devuelva la suma de la diagonal principal
#y otra que devuelva la multiplicacio
#Hacer otras 2 funciones que develvn suma y mult de la contradiagonal
matriz=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
def diagonalPrincipalSuma(matriz):
    resultado=0
    for j in range (0,4,1):
        for i in range (0,4,1):
            if i == j:
                resultado=resultado+matriz[j][i]
    return resultado
def diagonalPrincipalMultiplicacion(matriz):
    resultado=1
    for j in range(0,4,1):
        for i in range (0,4,1):
            if i == j :
               resultado=resultado*matriz[j][i] 
    return resultado
print("La suma de la diagonal principal es:")
print(diagonalPrincipalSuma(matriz))
print("La multiplicacion de la diagonal principal es:")
print(diagonalPrincipalMultiplicacion(matriz))
#para diagonal inversa

def diagonalInversaMultiplicacion(Matriz):
    resultado=1
    for j in range(0,4,1):
        for i in range (0,4,1):
            if j==4-i-1:
                resultado=resultado*matriz[j][i]
    return resultado
print("La multiplicacion de la diagonal inversa es: ")
print(diagonalInversaMultiplicacion(matriz))
        
