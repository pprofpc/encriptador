from cifrar import text2ASCII

def ASCII2Text(Matriz):
    """Convierte una matriz de número ASCII en una 'Cadena'"""
    texto = ""
    for letra in Matriz:
        numero = int(letra)
        texto += str(chr(numero))
    return texto

def ConvertTextInVector(text):
    vector = []
    vector = text.split(",")
    return vector


def CrearNuevaClave(clave, vector):
    """Arma una 'Cadena' de claves de la longitud de lo que se quiere cifrar"""
    nuevoVector = []
    count = 0
    agregar = 0
    for n in vector:
        agregar = text2ASCII(clave[count])
        nuevoVector.append(agregar)
        if(count == len(clave)-1):
            count = 0
        else:
            count += 1
    return nuevoVector


def Decifrar(claveVector, textoVector):
    """Decifra por medio de la clave proporcionada el texto encriptado"""
    nuevoTexto = ""
    count = 0
    ascii = 0
    for n in textoVector:
        ascii = int(n) - int(claveVector[count])
        nuevoTexto += str(chr(ascii))
        if(count == len(claveVector)-1):
            count = 0
        else:
            count += 1
    return nuevoTexto
