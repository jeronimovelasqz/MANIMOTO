from tkinter import *
import tkinter.messagebox
import os
from tkinter import ttk
import random
import time
import datetime


def main():
    root = Tk()
    app = Ventana_1(root)
    root.mainloop()


class Ventana_1:
    def __init__(self, administrador):
        self.administrador = administrador
        self.administrador.title("Administracion de manis")
        self.administrador.geometry('1350x750')
        self.administrador.config(bg="#ADADFF")
        self.Frame = Frame(self.administrador, bg="#C1C1FF")
        self.Frame.pack()

        self.usuario = StringVar()
        self.contraseña = StringVar()

        self.Titulo_label = Label(self.Frame, text='Login Umani moto', font=('arial', 55, 'bold'), bg='#C1C1FF',
                                  fg='Black')
        self.Titulo_label.grid(row=0, column=0, columnspan=3, pady=40)

        self.Cuadro_de_logeo_1 = LabelFrame(self.Frame, width=1350, height=600, relief='ridge', bg='#C1C1FF', bd=15,
                                            font=('arial', 20, 'bold'))
        self.Cuadro_de_logeo_1.grid(row=1, column=0)

        self.Cuadro_de_logeo_2 = LabelFrame(self.Frame, width=1000, height=600, relief='ridge', bg='#C1C1FF', bd=15,
                                            font=('arial', 20, 'bold'))
        self.Cuadro_de_logeo_2.grid(row=2, column=0)

        # ===================================================LABEL y Entradas=======================================================================
        self.Label_usuario = Label(self.Cuadro_de_logeo_1, text='Usuario', font=('arial', 20, 'bold'), bg='#C1C1FF',
                                   bd=20)
        self.Label_usuario.grid(row=0, column=0)

        self.texto_usuario = Entry(self.Cuadro_de_logeo_1, font=('arial', 20, 'bold'), textvariable=self.usuario)
        self.texto_usuario.grid(row=0, column=1, padx=50)

        self.Label_contraseña = Label(self.Cuadro_de_logeo_1, text='Clave', font=('arial', 20, 'bold'), bg='#C1C1FF',
                                      bd=20)
        self.Label_contraseña.grid(row=1, column=0)

        self.text_contraseña = Entry(self.Cuadro_de_logeo_1, font=('arial', 20, 'bold'), show='*',
                                     textvariable=self.contraseña)
        self.text_contraseña.grid(row=1, column=1)

        # =============================================================botones=======================================================================
        self.boton_logeo = Button(self.Cuadro_de_logeo_2, text='logearse', width=10, font=('airia', 15, 'bold'),
                                  command=self.Login)
        self.boton_logeo.grid(row=3, column=0, padx=8, pady=20)

        self.boton_resetear = Button(self.Cuadro_de_logeo_2, text='resetear', width=10, font=('airia', 15, 'bold'),
                                     command=self.Reset)
        self.boton_resetear.grid(row=3, column=1, padx=8, pady=20)

        self.boton_salir = Button(self.Cuadro_de_logeo_2, text='salir', width=10, font=('airia', 15, 'bold'),
                                  command=self.Exit)
        self.boton_salir.grid(row=3, column=2, padx=8, pady=20)

    def Login(self):
        usuario = (self.usuario.get())
        contraseña = (self.contraseña.get())

        if (usuario == str('admin') and contraseña == str('admin')):
            self.__menu__()

        else:
            tkinter.messagebox.askyesno("Logearse", "Error : contraseña equivocada ")
            self.usuario.set("")
            self.contraseña.set("")

    def Reset(self):
        self.usuario.set("")
        self.contraseña.set("")
        self.texto_usuario.focus()

    def Exit(self):
        self.Exit = tkinter.messagebox.askokcancel("sistema de logeo", "Confirme si quiere salir")
        if self.Exit > 0:
            self.administrador.destroy()
            return

    def __menu__(self):
        filename = 'Menu.py'
        os.system(filename)
        os.system('notepad' + filename)

    '''def new_window(self):
        self.new_Window = Toplevel(self.master)
        self.app = Window_2(self.new_Window)'''


class Ventana_2:
    def __init__(self, administrador):
        self.administrador = administrador
        self.administrador.title("Administracion de manis")
        self.administrador.geometry('1350x750')
        self.administrador.config(bg="green")
        self.Cuadro = Cuadro(self.master, bg="green")
        self.Cuadro.pack()


if __name__ == '__main__':
    main()

