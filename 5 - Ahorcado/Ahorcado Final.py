#Ahorcado 1.6
import random
imagenesAhorcado = ['''        
  +---+        
  |   |        
      |        
      |        
      |        
      |        
  =========''', '''        
  +---+        
  |   |        
  O   |        
      |        
      |        
      |        
  =========''', '''        
  +---+        
  |   |        
  O   |        
  |   |        
      |        
      |        
  =========''', '''        
  +---+        
  |   |        
  O   |        
 /|   |        
      |        
      |        
  =========''', '''        
  +---+        
  |   |        
  O   |        
 /|\  |        
      |        
      |        
  =========''', '''        
  +---+        
  |   |        
  O   |        
 /|\  |        
 /    |        
      |        
  =========''', '''        
  +---+        
  |   |        
  O   |        
 /|\  |        
 / \  |        
      |        
  =========''']
#Variables
##Generar Palabra
palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo cebra'.split()
palabraSecreta = []
palabraSecretaOculta = []
##Mostrar Tablero

##Obtener Turno
letrasValidas=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ñ','z','x','c','v','b','n','m']
letrasIncorrectas=[]
letrasCorrectas=[]
#Funciones
def generarPalabra (palabras):
    return palabras[random.randint(0,len(palabras)-1)]
def ocultarPalabra (palabraSecreta):
    return "#"*len(palabraSecreta)
def mostrarTablero(imagenesAhorcado):
    print(imagenesAhorcado[len(letrasIncorrectas)])
    print( palabraSecretaOculta )
    print("Letras Incorrrectas:",letrasIncorrectas)
def obtenerTurno(palabraSecreta , palabraSecretaOculta , letrasIncorrectas ):
    posiciones=[]
    reintentar=1
    while reintentar == 1:
        intento=input("Ingrese UNA letra a probar [").lower()
        if len(intento) != 1 :
            print("Debe ingresar un solo caracter")
            break
        elif intento not in letrasValidas:
            print("debe ingresar una letra valida para el alfabeto español")
            break
        elif intento in letrasIncorrectas or intento in letrasCorrectas:
            print("Ya se ha probado esa letra")
            break
        elif intento in palabraSecreta:
            print("La letra es correcta")
            letrasCorrectas.append(intento)
            #for para buscar en que posiciones esta la letra
            for i in range(len(palabraSecreta)):
                if palabraSecreta[i]==intento:
                    posiciones.append(i)
            #for para sustituir las letras
            for i in range(len(palabraSecreta)):
                if intento == palabraSecreta[i]:
                    palabraSecretaOculta[i]=intento
            reintentar=0 
            break
        else:
            letrasIncorrectas.append(intento)
            reintentar=0
            print("La letra es incorrecta")
            break
def jugarDeNuevo():
    jDNp=input("¿Desea jugar de nuevo? si/no").upper()
    if jDNp=="SI":
        jDN=True
    else:
        jDN=False
    return jDN
#Programa
ejecutar=True
while ejecutar == True :
    letrasIncorrectas=[]
    letrasProbadas=[]
    letrasCorrectas=[]
    palabraSecreta=list(generarPalabra(palabras))
    palabraSecretaOculta=list(ocultarPalabra(palabraSecreta))
    while len(letrasIncorrectas)<7:
        mostrarTablero(imagenesAhorcado)
        obtenerTurno(palabraSecreta , palabraSecretaOculta , letrasIncorrectas )
        if palabraSecreta == palabraSecretaOculta:
            print("[ACIERTO COMPLETO]")
            break
        elif len(letrasIncorrectas) == 6:
            print("[GAME OVER]")
            break
    ejecutar=jugarDeNuevo()