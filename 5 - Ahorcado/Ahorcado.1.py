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
#aca van variables
debeJugar=True
letrasIncorrectas=[]
letrasCorrectas=[]
palabraSecretaOculta=""
palabraSecreta=""
palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo cebra'.split()
#aca van funciones
letrasValidas=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ñ','z','x','c','v','b','n','m']
intentosRestantes=0
def generarPalabra (palabras):
    palabraSecreta=palabras[random.randint(1,len(palabras)-1)]
    palabraSecretaOculta="#"*len(palabraSecreta)
    palabraSecreta=list(palabraSecreta)
    palabraSecretaOculta=list(palabraSecretaOculta)
    print(palabraSecreta , "////" , palabraSecretaOculta)
    return palabraSecreta
def jugarDeNuevo ():
    jDNp=input("¿Desea jugar de nuevo? si/no").upper()
    if jDNp=="SI":
        jDN=True
    else:
        jDN=False
    return jDN
def obtenerIntento (palabraSecretaOculta , palabraSecreta , letrasIncorrectas , letrasCorrectas):
    posiciones=[]
    intento=1
    while intento==1:
        intento=input("Ingrese una letra a probar")
        intento=intento.lower()
        if len(intento)!= 1:
            print("debe ingresar un solo caracter")
            break
        else:
            if intento in letrasIncorrectas :
                print("¡Ya probo esa letra!")
                print("Pruebe con otra")
                break
            else:
                if intento in palabraSecreta:
                    letrasCorrectas=letrasCorrectas.append(intento)
                    for i in range (len(palabraSecreta)):        
                        if intento == palabraSecreta[i]:
                            posiciones.append(i)
                    for i in len(posiciones):
                        palabraSecretaOculta[posiciones[i]]=posiciones[i]
                else:
                    letrasIncorrectas=letrasIncorrectas.append(intento)
                    print("La letra no esta en la palabra")
                    break
def mostrarTablero (imagenesAhorcado, letrasCorrectas, letrasIncorrectas, palabraSecretaOculta, palabraSecreta ):
    print(imagenesAhorcado[len(letrasIncorrectas)])

    print(palabraSecreta , "////" , palabraSecretaOculta)
    
    print("Letras Probadas:" , letrasIncorrectas)
#Programa
while debeJugar == True:
    generarPalabra (palabras)
    while len(letrasIncorrectas) < 6:
        mostrarTablero(imagenesAhorcado, letrasCorrectas, letrasIncorrectas, palabraSecretaOculta)
        obtenerIntento(palabraSecretaOculta , palabraSecreta , letrasIncorrectas , letrasCorrectas)
debeJugar=jugarDeNuevo()