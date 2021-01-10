def text2ASCII(Cadena):
    """Convierte una 'Cadena' en una sucesión de números ASCII"""
    i = 0 					           # Variable del bucle.
    Size = len(Cadena)		     # Longitud de la cadena.
    Temp = ''	    # Variable temporal, donde se construirá la cadena en ASCII.
    while i < Size:  				      # Instancia del bucle.
        # Se empieza a contruir la palabra, usando la función ord().
        Temp += str(ord(Cadena[i]))
        if i < Size-1:
            Temp += ','
        i += 1 					      # Aumentamos el valor de la variable del bucle.
    return Temp


def crearNuevaClave(clave, Cadena):
    """Arma una 'Cadena' de claves de la longitud de lo que se quiere cifrar"""
    nuevaCadena = ""
    count = 0
    for rearmar in Cadena:
        nuevaCadena += clave[count]
        if(count == len(clave)-1):
            count = 0
        else:
            count += 1
    return nuevaCadena


def integration(clave, Cadena):
    nuevaClave = ""
    nuevaClave = crearNuevaClave(clave, Cadena)
    nuevaClave = text2ASCII(nuevaClave)
    CadenaVector = text2ASCII(Cadena)
    CadenaVector = CadenaVector.split(",")
    nuevaClaveVector = nuevaClave.split(",")
    count = 0
    numCifrados = 0
    vectorCifrado = []
    print(nuevaClaveVector, "Tamaño ", len(nuevaClaveVector))
    for num in nuevaClaveVector:
        # print(num)
        # print("CV: ",CadenaVector[count])
        numCifrados = int(num) + int(CadenaVector[count])
        vectorCifrado.append(numCifrados)
        # print("Suma: ",numCifrados)
        # print(vectorCifrado)
        if(count == len(nuevaClaveVector)-1):
            count = 0
        else:
            count += 1
    return vectorCifrado
