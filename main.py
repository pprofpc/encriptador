from tkinter import Tk
from tkinter import StringVar, Label, Button, Entry, E, DISABLED
from tkinter import messagebox as Messagebox
from archivo import Archivo

from cifrar import *

from tkinter import filedialog
import os

from tkinter import ttk


window = Tk()

password = StringVar()
mostrarDato = StringVar()
estadoArchivo = StringVar()
estadoArchivo.set("Cargar archivo")


archivoLeer = Archivo()

#Lógica del Botón Encriptar
def setDato():
    mostrarDato.set("Clave: "+text2ASCII(password.get()))
    if archivoLeer.getOk()&(len(password.get())>0):
        archivoLeer.setDataEncriptada(password.get())
        if archivoLeer.isEncrypted():
            Messagebox.showinfo("Info", "Datos encriptados!")
        else:
            Messagebox.showerror("Error", "Algo salió mal!")
    else:
        Messagebox.showwarning("Error", "Falta introducir una clave!")

#Lógica de la apertura del archivo
def abrir_archivo():
    ruta_app = os.path.abspath("./")
    archivo_abierto = filedialog.askopenfile(initialdir=ruta_app, title= "Seleccionar archivo",filetypes = (("txt","*.txt"),("all files","*.*")))
    archivoLeer.setCompleto(archivo_abierto.name)
    if archivoLeer.getOk():
        estadoArchivo.set("Archivo Cargado")
        btnAceptar['state'] = 'normal'
        



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

lblArchivoOk = Label( tab1, textvariable=estadoArchivo )
lblArchivoOk.grid(row=1, column=2)

lblPassword = Label(tab1, text="Contraseña: ")
lblPassword.grid(row=3, column=0)

txbPassword = Entry(tab1, textvariable=password, show="**")
txbPassword.grid(row=3, column=1)

lblBanderaPassword = Label(tab1, textvariable=mostrarDato)
lblBanderaPassword.grid(row=4, column=0, columnspan=2)

#Botón Encriptar

btnAceptar = Button(tab1, text="Encriptar", command=setDato, state=DISABLED)
btnAceptar.grid(row=5, column=1, sticky=E)





tab_control.pack(expand=1, fill='both')

window.mainloop()