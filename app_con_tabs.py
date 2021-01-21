from tkinter import *
from cifrar import *

from tkinter import filedialog
import os

from tkinter import ttk


window = Tk()

password = StringVar()
mostrarDato = StringVar()

class Archivo:
    nombre = ""
    ruta = ""
    completo = ""

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

archivoLeer = Archivo()

def setDato():
    mostrarDato.set("Clave: "+text2ASCII(password.get()))

def abrir_archivo():
    ruta_app = os.path.abspath("./")
    archivo_abierto = filedialog.askopenfile(initialdir=ruta_app, title= "Seleccionar archivo",filetypes = (("txt","*.txt"),("all files","*.*")))
    print(archivo_abierto.name)
    archivoLeer.setCompleto(archivo_abierto.name)
    print(archivoLeer.getCompleto())


window.title("Encriptador")
window.geometry("700x450")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Encriptar')

tab2 = ttk.Frame(tab_control)

tab_control.add(tab2, text='Desencriptar')

lblSeparador = Label(tab1)
lblSeparador.grid(column=0, row=0)

btnBuscar = Button(tab1, text="Buscar archivo a encriptar", command=abrir_archivo)
btnBuscar.grid(row=1, columnspan=2, column=0, sticky=E)

lblPassword = Label(tab1, text="Contraseña: ")
lblPassword.grid(row=3, column=0)

txbPassword = Entry(tab1, textvariable=password, show="**")
txbPassword.grid(row=3, column=1)

lblBanderaPassword = Label(tab1, textvariable=mostrarDato)
lblBanderaPassword.grid(row=4, column=0, columnspan=2)

btnAceptar = Button(tab1, text="Encriptar", command=setDato)
btnAceptar.grid(row=5, column=1, sticky=E)





tab_control.pack(expand=1, fill='both')

window.mainloop()
