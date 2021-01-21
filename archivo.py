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
        original = open(self.getCompleto(), 'r')
        count = 0
        ln = ""
        for ln in original.readlines():
            count += 1
            longitud = len(ln)
        original.close()
        self.__data = ln
        self.__dataEncriptada = integration(clave, self.__data)
        print("Archivo codificado: ", self.__dataEncriptada)
