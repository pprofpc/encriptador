from tkinter import *
from cifrar import *

from tkinter import filedialog
import os

from tkinter import ttk


window = Tk()

password = StringVar()
mostrarDato = StringVar()


def setDato():
    mostrarDato.set("Clave: "+text2ASCII(password.get()))

def abrir_archivo():
    archivo_abierto = filedialog.askopenfile(initialdir="/", title= "Seleccionar archivo",filetypes = (("txt","*.txt"),("all files","*.*")))
    print(archivo_abierto)

window.title("Encriptador")
window.geometry("700x450")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Encriptar')

tab2 = ttk.Frame(tab_control)

tab_control.add(tab2, text='Desencriptar')

lblSeparador = Label(tab1)
lblSeparador.grid(column=0, row=0)

lblPassword = Label(tab1, text="Contraseña: ")
lblPassword.grid(row=1, column=0)

txbPassword = Entry(tab1, textvariable=password, show="**")
txbPassword.grid(row=1, column=1)

lblBanderaPassword = Label(tab1, textvariable=mostrarDato)
lblBanderaPassword.grid(row=3, column=0, columnspan=2)

btnAceptar = Button(tab1, text="Aceptar", command=setDato)
btnAceptar.grid(row=4, column=1, sticky=E)

btnBuscar = Button(tab1, text="Buscar archivo a encriptar", command=abrir_archivo)
btnBuscar.grid(row=5, column=1, sticky=E)



tab_control.pack(expand=1, fill='both')

window.mainloop()
