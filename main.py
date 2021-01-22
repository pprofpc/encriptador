from tkinter import Tk
from tkinter import StringVar, Label, Button, Entry, E, DISABLED
from tkinter import messagebox as Messagebox
from tkinter import *
from archivo import Archivo

from cifrar import *

from tkinter import filedialog
from tkinter import ttk
import os

from tkinter import ttk

#----Variables del sistema----
window = Tk()

password = StringVar()
mostrarDato = StringVar()
estadoArchivo = StringVar()
estadoArchivo.set("Cargar archivo")
archivoLeer = Archivo()

#Variables Desencriptador

passwordD = StringVar()
mostrarDatoD = StringVar()
estadoArchivoD = StringVar()
estadoArchivoD.set("Cargar archivo")
archivoLeerD = Archivo()
#-----Lógica del programa----

#Lógica del Botón Encriptar
def setDato():
    mostrarDato.set("Datos encriptados, ya puede guardar")
    if archivoLeer.getOk()&(len(password.get())>0):
        archivoLeer.setDataEncriptada(password.get())
        if archivoLeer.isEncrypted():
            Messagebox.showinfo("Info", "Datos encriptados!")
            btnGuardar['state'] = 'normal'
        else:
            Messagebox.showerror("Error", "Algo salió mal!")
    else:
        Messagebox.showwarning("Error", "Falta introducir una clave!")

#Lógica de la apertura del archivo
def abrir_archivo():
    ruta_app = os.path.abspath("./")
    archivo_abierto = filedialog.askopenfile(initialdir=ruta_app, title= "Seleccionar archivo",filetypes = (("TXT","*.txt"),("All Files","*.*")))
    if archivo_abierto is None:
        Messagebox.showwarning("Atención", "Cancelo la operación!")
    else:
        archivoLeer.setCompleto(archivo_abierto.name)
        if archivoLeer.getOk():
            estadoArchivo.set("Archivo Cargado")
            btnEncriptar['state'] = 'normal'

#Lógica del Botón: Guardar datos encriptados
def guardar_archivo():
    ruta_app = os.path.abspath("./")
    files = [('TXT', '*.txt'),
             ('All Files', '*.*')]
    file = filedialog.asksaveasfile(initialdir=ruta_app, title="Guardar archivo",
                         filetypes=files, defaultextension=files)
    if file is None:
        Messagebox.showwarning("Atención","Cancelo la operación!")
    else:
        if archivoLeer.isEncrypted():
            size = archivoLeer.getLongitud()
            i = 0
            for n in archivoLeer.getDataEncriptada():
                file.write(str(n))
                if i < size-1:
                    file.write(",")
                i += 1
            file.close()
            Messagebox.showinfo("Info", "Datos Guardados!")

#----Lógica de la pestaña Desencriptar


def setDatoD():
    return True


def abrir_archivoD():
    ruta_app = os.path.abspath("./")
    archivo_abierto = filedialog.askopenfile(initialdir=ruta_app, title= "Seleccionar archivo",filetypes = (("TXT","*.txt"),("All Files","*.*")))
    if archivo_abierto is None:
        Messagebox.showwarning("Atención", "Cancelo la operación!")
    else:
        archivoLeerD.setCompleto(archivo_abierto.name)
        if archivoLeerD.getOk():
            estadoArchivoD.set("Archivo Cargado")
            btnDesencriptar['state'] = 'normal'


def guardar_archivoD():
    return True

#----Geometría de la UI----
window.title("Encriptador")
window.geometry("365x250")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Encriptar')

tab2 = ttk.Frame(tab_control)

tab_control.add(tab2, text='Desencriptar')

#----Espacio de encriptado----

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

btnEncriptar = Button(tab1, text="Encriptar", command=setDato, state=DISABLED)
btnEncriptar.grid(row=5, column=1, sticky=E, pady=10)

#----------Espacio de guardado--------------------

lineaGuardar = ttk.Separator(tab1, orient='horizontal')
#lineaGuardar.place(relx=0, rely=0.33, relwidth=1, relheight=1)
lineaGuardar.grid(row=7, column=0, columnspan=4, sticky='ew')
lblSeparador2 = Label(tab1)
lblSeparador2.grid(column=0, row=8)

#Botón Guardar
btnGuardar = Button(tab1, text="Guardar datos encriptados",
                   command=guardar_archivo,
                    state=DISABLED)

btnGuardar.grid(row=9, columnspan=2, column=0, sticky=E)

#----Pestaña Desencriptar----

lblSeparadorD = Label(tab2)
lblSeparadorD.grid(column=0, row=0)

btnBuscarD = Button(tab2, text="Buscar archivo a desencriptar",
                   command=abrir_archivoD)
btnBuscarD.grid(row=1, columnspan=2, column=0, sticky=E)

lblArchivoOkD = Label(tab2, textvariable=estadoArchivoD)
lblArchivoOkD.grid(row=1, column=2)

lblPasswordD = Label(tab2, text="Contraseña: ")
lblPasswordD.grid(row=3, column=0)

txbPasswordD = Entry(tab2, textvariable=passwordD, show="**")
txbPasswordD.grid(row=3, column=1)

lblBanderaPasswordD = Label(tab2, textvariable=mostrarDatoD)
lblBanderaPasswordD.grid(row=4, column=0, columnspan=2)

#Botón Encriptar

btnDesencriptar = Button(tab2, text="Desencriptar", command=setDatoD, state=DISABLED)
btnDesencriptar.grid(row=5, column=1, sticky=E, pady=10)

#----------Espacio de guardado--------------------

lineaGuardarD = ttk.Separator(tab2, orient='horizontal')
#lineaGuardar.place(relx=0, rely=0.33, relwidth=1, relheight=1)
lineaGuardarD.grid(row=7, column=0, columnspan=4, sticky='ew')
lblSeparador2D = Label(tab2)
lblSeparador2D.grid(column=0, row=8)

#Botón Guardar
btnGuardarD = Button(tab2, text="Guardar datos desencriptados",
                    command=guardar_archivoD,
                    state=DISABLED)

btnGuardarD.grid(row=9, columnspan=2, column=0, sticky=E)


#----Empaquetado Final----

tab_control.pack(expand=1, fill='both')

window.mainloop()
