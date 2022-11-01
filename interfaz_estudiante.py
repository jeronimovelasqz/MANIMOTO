from tkinter import *
import tkinter.messagebox
import random
import guardado_de_informacion_estudiante
from tkinter import ttk


class Informacion_estudiante():

    def __init__(self, administrador):
        self.administrador = administrador
        self.administrador.title('universidad manimoto')
        self.administrador.geometry('1350x750')
        self.administrador.config(bg='lightblue')

        def information():
            # ========================================================Variables=====================================================================

            self.nombre = StringVar()

            self.nombrePadre = StringVar()

            self.nombreMadre = StringVar()

            self.direccion = StringVar()

            self.telefono = StringVar()

            self.email = StringVar()

            self.fechaNacimiento = StringVar()

            self.genero = StringVar()

            # ==========================================================Funciones====================================================================

            def StudentRec(event):

                try:
                    global tupla_seleccionada

                    index = self.listbox.curselection()[0]
                    tupla_seleccionada = self.listbox.get(index)

                    self.Entrada_nombre.delete(0, END)
                    self.Entrada_nombre.insert(END, tupla_seleccionada[1])

                    self.Entrada_nombrePadre.delete(0, END)
                    self.Entrada_nombrePadre.insert(END, tupla_seleccionada[2])

                    self.Entrada_nombreMadre.delete(0, END)
                    self.Entrada_nombreMadre.insert(END, tupla_seleccionada[3])

                    self.Entrada_direccion.delete(0, END)
                    self.Entrada_direccion.insert(END, tupla_seleccionada[4])

                    self.Entrada_telefono.delete(0, END)
                    self.Entrada_telefono.insert(END, tupla_seleccionada[5])

                    self.Entry_emailID.delete(0, END)
                    self.Entry_emailID.insert(END, tupla_seleccionada[6])

                    self.Entrada_fechaNacieminto.delete(0, END)
                    self.Entrada_fechaNacimiento.insert(END, tupla_seleccionada[7])

                    self.Entrada_genero.delete(0, END)
                    self.Entrada_genero.insert(END, tupla_seleccionada[8])

                except:
                    (IndexError, AttributeError)

            def Agregar():
                if (len(self.nombre.get()) != 0):
                    guardado_de_informacion_estudiante.insert(self.nombre.get(), self.nombrePadre.get(),
                                                              self.nombreMadre.get(), self.direccion.get(),
                                                              self.telefono.get(), self.email.get(),
                                                              self.fechaNacimiento.get(), \
                                                              self.genero.get())
                    self.listbox.delete(0, END)
                    self.listbox.insert(END, (
                    self.nombre.get(), self.nombrePadre.get(), self.nombreMadre.get(), self.direccion.get(),
                    self.telefono.get(), self.email.get(), self.fechaNacimiento.get(), \
                    self.genero.get()))

            def Desplegar():
                self.listbox.delete(0, END)
                for row in guardado_de_informacion_estudiante.view():
                    self.listbox.insert(END, row, str(' '))

            def Salir():
                Exit = tkinter.messagebox.askyesno("sistema de logeo", "confirme si quiere salir")
                if Exit > 0:
                    self.administrador.destroy()
                    return

            def Resetear():

                self.nombre.set('')

                self.nombrePadre.set('')

                self.nombreMadre.set('')

                self.direccion.set('')

                self.telefono.set('')

                self.email.set('')

                self.fechaNacimiento.set('')

                self.genero.set('')

                self.listbox.delete(0, END)

            def Borrar():
                if (len(self.nombre.get()) != 0):
                    guardado_de_informacion_estudiante.delete(tupla_seleccionada[0])
                    Resetear()
                    Desplegar()

            def Buscar():
                try:
                    self.listbox.delete(0, END)
                    for row in guardado_de_informacion_estudiante.search(self.nombre.get(), self.nombrePadre.get(),
                                                                         self.nombreMadre.get(), self.direccion.get(),
                                                                         self.telefono.get(), self.email.get(),
                                                                         self.fechaNacimiento.get(), self.genero.get()):
                        self.listbox.insert(END, row, str(' '))

                except:
                    TypeError

            def Actualizar():
                if (len(self.nombre.get()) != 0):
                    guardado_de_informacion_estudiante.delete(tupla_seleccionada[0])

                if (len(self.nombre.get()) != 0):
                    guardado_de_informacion_estudiante.insert(self.nombre.get(), self.nombrePadre.get(),
                                                              self.nombreMadre.get(), self.direccion.get(),
                                                              self.telefono.get(), self.email.get(),
                                                              self.fechaNacimiento.get(), \
                                                              self.genero.get())

                    self.listbox.delete(0, END)
                    self.listbox.insert(END, (
                    self.nombre.get(), self.nombrePadre.get(), self.nombrePadre.get(), self.direccion.get(),
                    self.telefono.get(), self.email.get(), self.fechaNacimiento.get(), \
                    self.genero.get()))

            # ============================================================cuadros=====================================================================

            self.Main_Frame = LabelFrame(self.administrador, width=1300, height=500, font=('arial', 20, 'bold'), \
                                         bg='lightblue', bd=15, relief='ridge')
            self.Main_Frame.grid(row=0, column=0, padx=10, pady=20)

            self.Frame_1 = LabelFrame(self.Main_Frame, width=600, height=400, font=('arial', 15, 'bold'), \
                                      relief='ridge', bd=10, bg='lightblue', text=' informacion del estudiante ')
            self.Frame_1.grid(row=1, column=0, padx=10)

            self.Frame_2 = LabelFrame(self.Main_Frame, width=750, height=400, font=('arial', 15, 'bold'), \
                                      relief='ridge', bd=10, bg='lightblue', text='Base de Datos del estudiante')
            self.Frame_2.grid(row=1, column=1, padx=5)

            self.Frame_3 = LabelFrame(self.administrador, width=1200, height=100, font=('arial', 10, 'bold'), \
                                      bg='lightblue', relief='ridge', bd=13)
            self.Frame_3.grid(row=2, column=0, pady=10)

            # ========================================================label del cuadro========================================================
            self.Label_nombre = Label(self.Frame_1, text='nombre', font=('arial', 20, 'bold'), bg='lightblue')
            self.Label_nombre.grid(row=0, column=0, sticky=W, padx=20, pady=10)

            self.Label_nombrePadre = Label(self.Frame_1, text='nombre del padre', font=('arial', 20, 'bold'),
                                           bg='lightblue')
            self.Label_nombrePadre.grid(row=1, column=0, sticky=W, padx=20)

            self.Label_nombreMadre = Label(self.Frame_1, text='nombre de la madre', font=('arial', 20, 'bold'),
                                           bg='lightblue')
            self.Label_nombreMadre.grid(row=2, column=0, sticky=W, padx=20)

            self.Label_direccion = Label(self.Frame_1, text='direccion', font=('arial', 20, 'bold'), bg='lightblue')
            self.Label_direccion.grid(row=3, column=0, sticky=W, padx=20)

            self.Label_telefono = Label(self.Frame_1, text='telefono', font=('arial', 20, 'bold'), bg='lightblue')
            self.Label_telefono.grid(row=4, column=0, sticky=W, padx=20)

            self.Label_emailID = Label(self.Frame_1, text='email', font=('arial', 20, 'bold'), bg='lightblue')
            self.Label_emailID.grid(row=5, column=0, sticky=W, padx=20)

            self.Label_fechaNacimiento = Label(self.Frame_1, text='fecha nacimiento', font=('arial', 20, 'bold'),
                                               bg='lightblue')
            self.Label_fechaNacimiento.grid(row=6, column=0, sticky=W, padx=20)

            self.Label_genero = Label(self.Frame_1, text='Genero', font=('arial', 20, 'bold'), bg='lightblue')
            self.Label_genero.grid(row=7, column=0, sticky=W, padx=20, pady=10)

            # ========================================================Entries of Frame_1========================================================
            self.Entrada_nombre = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.nombre)
            self.Entrada_nombre.grid(row=0, column=1, padx=10, pady=5)

            self.Entrada_nombrePadre = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.nombrePadre)
            self.Entrada_nombrePadre.grid(row=1, column=1, padx=10, pady=5)

            self.Entrada_nombreMadre = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.nombreMadre)
            self.Entrada_nombreMadre.grid(row=2, column=1, padx=10, pady=5)

            self.Entrada_direccion = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.direccion)
            self.Entrada_direccion.grid(row=3, column=1, padx=10, pady=5)

            self.Entrada_telefono = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.telefono)
            self.Entrada_telefono.grid(row=4, column=1, padx=10, pady=5)

            self.Entry_emailID = Entry(self.Frame_1, font=('arial', 17, 'bold'), textvariable=self.email)
            self.Entry_emailID.grid(row=5, column=1, padx=10, pady=5)

            self.Entrada_fechaNacimiento = Entry(self.Frame_1, font=('arial', 17, 'bold'),
                                                 textvariable=self.fechaNacimiento)
            self.Entrada_fechaNacimiento.grid(row=6, column=1, padx=10, pady=5)

            self.Entrada_genero = ttk.Combobox(self.Frame_1, values=(' ', 'Maculino', 'Femenino', 'Others'), \
                                               font=('arial', 17, 'bold'), textvariable=self.genero, width=19)
            self.Entrada_genero.grid(row=7, column=1, padx=10, pady=5)

            # ========================================================botones de self.frame_3=========================================================
            self.Boton_Guardar = Button(self.Frame_3, text='Guardar', font=('arial', 17, 'bold'), width=8,
                                        command=Agregar)
            self.Boton_Guardar.grid(row=0, column=0, padx=10, pady=10)

            self.Boton_Desplegar = Button(self.Frame_3, text='deplegar', font=('arial', 17, 'bold'), width=8,
                                          command=Desplegar)
            self.Boton_Desplegar.grid(row=0, column=1, padx=10, pady=10)

            self.Boton_resetear = Button(self.Frame_3, text='resetear', font=('arial', 17, 'bold'), width=8,
                                         command=Resetear)
            self.Boton_resetear.grid(row=0, column=2, padx=10, pady=10)

            self.Boton_actualizar = Button(self.Frame_3, text='actualizar', font=('arial', 17, 'bold'), width=8,
                                           command=Actualizar)
            self.Boton_actualizar.grid(row=0, column=3, padx=10, pady=10)

            self.Boton_borrar = Button(self.Frame_3, text='borrar', font=('arial', 17, 'bold'), width=8, command=Borrar)
            self.Boton_borrar.grid(row=0, column=4, padx=10, pady=10)

            self.Boton_buscar = Button(self.Frame_3, text='buscar', font=('arial', 17, 'bold'), width=8, command=Buscar)
            self.Boton_buscar.grid(row=0, column=5, padx=10, pady=10)

            self.Buton_salir = Button(self.Frame_3, text='salir', font=('arial', 17, 'bold'), width=8, command=Salir)
            self.Buton_salir.grid(row=0, column=6, padx=10, pady=10)

            # ===============================================List Box and self.scrollbar========================================================
            self.scrollbar = Scrollbar(self.Frame_2)
            self.scrollbar.grid(row=0, column=1, sticky='ns')

            self.listbox = Listbox(self.Frame_2, width=75, height=20, font=('arial', 12, 'bold'))
            self.listbox.bind('<<ListboxSelect>>', StudentRec)
            self.listbox.grid(row=0, column=0)
            self.scrollbar.config(command=self.listbox.yview)

        information()


root = Tk()
obj = Informacion_estudiante(root)
root.mainloop()
