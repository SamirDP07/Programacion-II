#Actividad
#El usuario debe ingresar una palabra y un desplazamiento (+ o -) y aplicar cifrado césar
#osea que pasa de a a b
#de b a c
#que el usuario pueda aumentar o dismiuir el cifrado a gusto
#investigar chr y do
palabra = input("Palabra: ")
desplazamiento = int(input("Caracteres a desplazar (puede ser negativo): "))
palabra = palabra.lower()

def desplazar(palabra, desplazamiento):
    resultado = ""
    for i in range(len(palabra)):
        c = palabra[i]
        if c.isalpha():
            c = chr((ord(c) - ord('a') + desplazamiento) % 26 + ord('a'))
        resultado += c
    return resultado

resultado = desplazar(palabra, desplazamiento)
print("Resultado: " + resultado)

