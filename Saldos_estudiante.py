from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import datetime
import guardado_de_saldos


class Consultas():
    def __init__(self, administrador):
        self.administrador = administrador
        self.administrador.title('Umani consultas y servicios  ')
        self.administrador.geometry('1350x750')
        self.administrador.config(bg='lightblue')

        # ==================================================Variables=================================================
        self.recibo = StringVar()

        self.nombre = StringVar()

        self.admision = StringVar()

        self.fecha = StringVar()

        self.facultad = StringVar()

        self.semestre = StringVar()

        self.total = DoubleVar()

        self.pago = DoubleVar()

        self.pagare = DoubleVar()

        # ==================================================Funciones=================================================
        def Tuple(event):
            try:
                global st
                index = self.list.curselection()[0]
                st = self.list.get(index)

                self.recibo_entrada.delete(0, END)
                self.recibo_entrada.insert(END, st[1])

                self.nombre_entrada.delete(0, END)
                self.nombre_entrada.insert(END, st[2])

                self.admision_entrada.delete(0, END)
                self.admision_entrada.insert(END, st[3])

                self.fecha_entrada.delete(0, END)
                self.fecha_entrada.insert(END, st[4])

                self.facultad_entrada.delete(0, END)
                self.facultad_entrada.insert(END, st[5])

                self.semestre_entrada.delete(0, END)
                self.semestre_entrada.insert(END, st[6])

                self.total_entrada.delete(0, END)
                self.total_entrada.insert(END, st[7])

                self.pago_entrada.delete(0, END)
                self.pago_entrada.insert(END, st[8])

                self.pagare_entrada.delete(0, END)
                self.pagare_entrada.insert(END, st[9])


            except IndexError:
                pass

        def Insertar():
            if (len(self.admision.get()) != 0):
                guardado_de_saldos.insert(self.recibo.get(), self.nombre.get(), self.admision.get(), self.fecha.get(),
                                   self.facultad.get(), self.semestre.get(), self.total.get(), self.pago.get(),
                                   self.pagare.get())
                self.list.delete(0, END)

                self.list.insert(END, (self.recibo.get(), self.nombre.get(), self.admision.get(), self.fecha.get(),
                                       self.facultad.get(), self.semestre.get(), self.total.get(), self.pago.get(),
                                       self.pagare.get()))

        def Ver():
            self.list.delete(0, END)
            for row in guardado_de_saldos.view():
                self.list.insert(END, row, str(' '))

        def Formatear():
            self.recibo.set('')

            self.nombre.set('')

            self.admision.set('')

            #self.date.set('')
            self.facultad.set('')

            self.semestre.set('')

            self.pago.set('')

            self.pagare.set('')

            self.Display.delete('1.0', END)

            self.list.delete(0, END)

        def Eliminar():


            try:

                guardado_de_saldos.delete(st[0])
                Formatear()
                Ver()

            except NameError:
                pass



        def Recibo():

            try:

                self.Display.delete('1.0', END)

                self.Display.insert(END, '\t\tRecibo' + '\n\n')

                self.Display.insert(END, '\tRecibo No.\t     :' + self.recibo.get() + '\n')



                self.Display.insert(END, '\tNombre del estudiante  :' + self.nombre.get() + '\n')


                self.Display.insert(END, '\tAdmision No.\t:' + self.admision.get() + '\n')


                self.Display.insert(END, '\tFecha\t  :' +  "   " + self.fecha.get() + '\n')


                self.Display.insert(END, '\tFacultdad\t:' + self.facultad.get() + '\n')


                self.Display.insert(END, '\tSemestre\t:' + self.semestre.get() + '\n\n')

                x1 = (self.total.get())
                x2 = (self.pago.get())
                x3 = (x1 - x2)

                self.Display.insert(END, '\tMonto Total  :' + "  " + str(x1) + '\n')
                self.Display.insert(END, '\tMonto Pagado  :' + "  " + str(x2) + '\n')
                self.Display.insert(END, '\tBalance\t    :' + "  " + str(x3) + '\n')

                self.pagare.set(x3)

            except tkinter.TclError:
                pass

        def Buscar():

            try:
                self.list.delete(0, END)
                for row in guardado_de_saldos.search(self.recibo.get(), self.nombre.get(), self.admision.get(), self.fecha.get(),
                                              self.facultad.get(), self.semestre.get(), self.total.get(), self.pago.get(),
                                              self.pagare.get()):
                    self.list.insert(END, row, str(' '))
            except :
                pass

        def Actualizar():
            try:
                guardado_de_saldos.delete(st[0])
                Insertar()
            except: NameError

        def Salir():
            Exit = tkinter.messagebox.askyesno(
                'atencion', 'confirme si quiere salir')
            if Exit > 0:
                root.destroy()
                return

        # ==================================================Frames===================================================
        Cuadro_principal = Frame(self.administrador, bg='lightblue')
        Cuadro_principal.grid()

        Titulo_cuadro  = LabelFrame(
            Cuadro_principal, width=1350, height=100, bg='#F8F8F8', relief='ridge', bd=15)
        Titulo_cuadro.pack(side=TOP)



        self.lblTitle = Label(Titulo_cuadro, font=('arial', 40, 'bold'), text='Saldos y saldos pendientes', bg='#F8F8F8', padx=13)
        self.lblTitle.grid(padx=400)



        cuadro_de_datos = Frame(Cuadro_principal, width=1350, height=350, bg='#F8F8F8', relief='ridge', bd=15)
        cuadro_de_datos.pack(side=TOP, padx=15)



        cuadro_1 = LabelFrame(cuadro_de_datos, width=850, height=350, bg='#F8F8F8', relief='ridge', bd=8, text='Informacion', font=('arial', 15, 'bold'))
        cuadro_1.pack(side=LEFT, padx=10)



        cuadro_2 = LabelFrame(cuadro_de_datos, width=495, height=350, bg='#FFFFEF', relief='ridge', bd=8,text='Recibo', font=('arial', 15, 'bold'))
        cuadro_2.pack(side=RIGHT, padx=10)



        Cuadro_de_lista = Frame( Cuadro_principal, width=1350, height=150, bg='lightblue', relief='ridge', bd=15)
        Cuadro_de_lista.pack(side=TOP, padx=15)



        Button_Frame = Frame( Cuadro_principal, width=1350, height=80,
                             bg='#F8F8F8', relief='ridge', bd=15)
        Button_Frame.pack(side=TOP)

        # ===================================================Labels================================================
        self.recibo_label = Label(cuadro_1, text='Recibo No. : ', font=('arial', 14, 'bold'), bg='#F8F8F8')
        self.recibo_label.grid(row=0, column=0, padx=15, sticky=W)




        self.nombre_label = Label(cuadro_1, text='Nombre del estudiante : ', font=('arial', 14, 'bold'), bg='#F8F8F8')
        self.nombre_label.grid(row=1, column=0, padx=15, sticky=W)




        self.admision_label = Label(cuadro_1, text='Admision No. : ', font=('arial', 14, 'bold'), bg='#F8F8F8')
        self.admision_label.grid(row=2, column=0, padx=15, sticky=W)




        self.fecha_label = Label(cuadro_1, text='Fecha : ', font=('arial', 14, 'bold'), bg='#F8F8F8')
        self.fecha_label.grid(row=3, column=0, padx=15, sticky=W)




        self.facultad_label = Label(cuadro_1, text='Facultad : ', font=('arial', 14, 'bold'), bg='#F8F8F8')
        self.facultad_label.grid(row=4, column=0, padx=15, sticky=W)




        self.semestre_label = Label(cuadro_1, text='Semestre : ', font=('arial', 14, 'bold'), bg='#F8F8F8')
        self.semestre_label.grid(row=5, column=0, padx=15, sticky=W)




        self.total_label = Label(cuadro_1, text='Monto total : ', font=('arial', 14, 'bold'), bg='#F8F8F8')
        self.total_label.grid(row=2, column=2, padx=5, sticky=W)




        self.pago_label = Label(cuadro_1, text='Monto pagado : ', font=('arial', 14, 'bold'), bg='#F8F8F8')
        self.pago_label.grid(row=3, column=2, padx=5, sticky=W)




        self.pagare_label = Label(cuadro_1, text='Balance : ', font=(
            'arial', 14, 'bold'), bg='#F8F8F8')
        self.pagare_label.grid(row=4, column=2, padx=5, sticky=W)

        # ==================================================Entries=================================================
        self.var_1 = DoubleVar(cuadro_1, value='15000')
        d1 = datetime.date.today()
        self.fecha.set(d1)




        self.recibo_entrada = Entry(cuadro_1, font=('arial', 14), textvariable=self.recibo, bg="#FFFFEF")
        self.recibo_entrada.grid(row=0, column=1, padx=15, pady=5)




        self.nombre_entrada = Entry(cuadro_1, font=('arial', 14), textvariable=self.nombre, bg="#FFFFEF")
        self.nombre_entrada.grid(row=1, column=1, padx=15, pady=5)




        self.admision_entrada = Entry(cuadro_1, font=('arial', 14), textvariable=self.admision , bg="#FFFFEF")
        self.admision_entrada.grid(row=2, column=1, padx=15, pady=5)




        self.fecha_entrada = Entry(cuadro_1, font=('arial', 14), textvariable=self.fecha, bg="#FFFFEF")
        self.fecha_entrada.grid(row=3, column=1, padx=15, pady=5)




        self.facultad_entrada = ttk.Combobox(cuadro_1, values=(' ', 'Derecho', 'Ingenieria', 'Ciencias Basicas', 'Comunicacion Social'), font=('arial', 14), width=19, textvariable=self.facultad  )
        self.facultad_entrada.grid(row=4, column=1, padx=15, pady=5)




        self.semestre_entrada = ttk.Combobox(cuadro_1, values=(' ', 'Primero', 'Segundo', 'Tercero' , 'Cuarto', 'Quinto' , 'Sexto' , 'Septimo', 'Octavo' , 'Noveno' , 'Decimo'), font=('arial', 14), width=19,
                                      textvariable=self.semestre, )
        self.semestre_entrada.grid(row=5, column=1, padx=15, pady=5)




        self.total_entrada = Entry(cuadro_1, font=( 'arial', 14), width=10, textvariable=self.total, bg="#FFFFEF")
        self.total_entrada.grid(row=2, column=3, padx=8, pady=5)




        self.pago_entrada = Entry(cuadro_1, font=('arial', 14), width=10, textvariable=self.pago, bg="#FFFFEF")
        self.pago_entrada.grid(row=3, column=3, pady=5)




        self.pagare_entrada = Entry(cuadro_1, font=( 'arial', 14), width=10, textvariable=self.pagare, bg="#FFFFEF")
        self.pagare_entrada.grid(row=4, column=3, pady=7)




        # ==================================================Frame_2=================================================
        self.Display = Text(cuadro_2, width=42, height=12,
                            font=('arial', 14, 'bold'))
        self.Display.grid(row=0, column=0, padx=3)




        # =============================================List box and scrollbar===========================================


        sb = Scrollbar(Cuadro_de_lista)
        sb.grid(row=0, column=1, sticky='ns')

        self.list = Listbox(Cuadro_de_lista, font=(
            'arial', 13, 'bold'), width=140, height=8)
        self.list.bind('<<ListboxSelect>>', Tuple)
        self.list.grid(row=0, column=0)
        sb.config(command=self.list.yview)




        # ==================================================Buttons=================================================
        boton_guardado = Button(Button_Frame, text='Guardar', font=('arial', 14, 'bold'), width=10, command=Insertar)
        boton_guardado.grid(row=0, column=0, padx=5, pady=5)





        boton_ver = Button(Button_Frame, text='Mostrar', font=('arial', 14, 'bold'), width=10, command=Ver)
        boton_ver.grid(row=0, column=1, padx=5, pady=5)




        boton_formateo = Button(Button_Frame, text='Resetear', font=('arial', 14, 'bold'), width=10, command=Formatear)
        boton_formateo.grid(row=0, column=2, padx=5, pady=5)




        boton_actualizar = Button(Button_Frame, text='Actualizar', font=('arial', 14, 'bold'), width=10, command=Actualizar)
        boton_actualizar.grid(row=0, column=3, padx=5, pady=5)




        boton_buscar = Button(Button_Frame, text='Buscar', font=('arial', 14, 'bold'), width=10, command=Buscar)
        boton_buscar.grid(row=0, column=4, padx=5, pady=5)




        boton_eliminar = Button(Button_Frame, text='Borrar', font=('arial', 14, 'bold'), width=10, command=Eliminar)
        boton_eliminar.grid(row=0, column=5, padx=5, pady=5)




        boton_recibo = Button(Button_Frame, text='Recibo', font=('arial', 14, 'bold'), width=10, command=Recibo)
        boton_recibo.grid(row=0, column=6, padx=5, pady=5)




        boton_salida = Button(Button_Frame, text='Salir', font=('arial', 14, 'bold'), width=10, command=Salir)
        boton_salida.grid(row=0, column=7, padx=5, pady=5)


root = Tk()
obj = Consultas(root)
root.mainloop()
