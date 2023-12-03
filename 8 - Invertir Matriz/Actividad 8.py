#matriz con los numeros
filas = 5
columnas = 5
matriz = [[i + j * columnas + 1 for i in range(columnas)] for j in range(filas)]
for fila in matriz:
    print(fila)
#Inverter
for i in range (filas):
    for j in range(int(columnas/2)):
        indice_opuesto = columnas - j - 1
        actual = matriz[i][j]
        opuesto = matriz[i][indice_opuesto]
        matriz[i][j] = opuesto
        matriz[i][indice_opuesto]=actual
#print
for fila in matriz:
    print(fila)