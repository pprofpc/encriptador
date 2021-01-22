from cifrar import integration


class Archivo:
    nombre = ""
    ruta = ""
    completo = ""
    __data = ""
    __dataEncriptada = ""

    def setNombre(self, nombre):
        self.nombre = nombre

    def setRuta(self, ruta):
        self.ruta = ruta

    def getRuta(self):
        return self.ruta

    def getNombre(self):
        return self.nombre

    def setCompleto(self, completo):
        """Seteo la ruta completa y nombre de archivo"""
        self.completo = completo

    def getCompleto(self):
        """Devuelve ruta completa y nombre de archivo"""
        return self.completo

    def getOk(self):
        """Devuelve si el archivo existe"""
        if (len(self.getCompleto()) > 0):
            return True
        else:
            return False

    def setDataEncriptada(self, clave):
        """Encripta el archivo con la clave introducida"""
        original = open(self.getCompleto(), 'r')
        count = 0
        ln = ""
        for ln in original.readlines():
            count += 1

        original.close()
        self.__data = ln
        self.__dataEncriptada = integration(clave, self.__data)
        
    def isEncrypted(self):
        if len(self.__dataEncriptada)>0:
            return True
        else:
            return False

    def getDataEncriptada(self):
        return self.__dataEncriptada

    def getLongitud(self):
        return len(self.__dataEncriptada)