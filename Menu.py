from tkinter import *
import random
import os


def __informacion__():
    filename = 'interfaz_estudiante.py'
    os.system(filename)
    os.system('notepad' + filename)


def __Registro__():
    filename = 'Saldos_estudiante.py'
    os.system(filename)
    os.system('notepad' + filename)


def menu():
    root = Tk()
    root.title('Menu')
    root.geometry('1350x750')

    titulo_cuadro = LabelFrame(root, font=('arial', 50, 'bold'), width=1000, height=100, bg='#8B8B45', relief='raise',
                               bd=13)
    titulo_cuadro.grid(row=0, column=0, pady=50)

    titulo_label = Label(titulo_cuadro, text='U mani moto', font=('arial', 30, 'bold'), bg='#8B8B45')
    titulo_label.grid(row=0, column=0, padx=150)

    # ========================================================FRAMES===================================================================
    Cuadro_1 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='#8B8B45', relief='ridge', bd=10)
    Cuadro_1.grid(row=1, column=0, padx=280)

    Cuadro_2 = LabelFrame(root, font=('arial', 17, 'bold'), width=1000, height=100, bg='#8B8B45', relief='ridge', bd=10)
    Cuadro_2.grid(row=2, column=0, padx=130, pady=7)

    # ========================================================LABELS===================================================================
    Label_1 = Label(Cuadro_1, text='Soy Umanimoto', font=('arial', 25, 'bold'), bg='#8B8B45')
    Label_1.grid(row=0, column=0, padx=50, pady=5)

    Label_2 = Label(Cuadro_2, text='uMani consultas y servicios', font=('arial', 25, 'bold'), bg='#8B8B45')
    Label_2.grid(row=0, column=0, padx=100, pady=5)

    # ========================================================Botones===================================================================
    Boton_1 = Button(Cuadro_1, text='Mirar', font=('arial', 16, 'bold'), width=8, command=__informacion__, bg="#CDCD66")
    Boton_1.grid(row=0, column=3, padx=50)

    Boton_2 = Button(Cuadro_2, text='Mirar', font=('arial', 16, 'bold'), width=8, command=__Registro__, bg="#CDCD66")
    Boton_2.grid(row=0, column=3, padx=50)

    root.mainloop()


if __name__ == '__main__':
    menu()
