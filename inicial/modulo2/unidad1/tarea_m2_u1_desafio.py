from tkinter import *

master = Tk()
master.title("Tarea-M2-U1-Python Inicial")
master.geometry("400x150")

#background_label = Label(master)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
mensaje = Label(master, text="Ingrese los siguientes datos:", bg="purple", fg="white")
mensaje.grid(row=0, column=0, columnspan=3, sticky=NSEW)

titulo = Label(master, text="Título")
titulo.grid(row=1, column=0, sticky=W)
ruta = Label(master, text="Ruta")
ruta.grid(row=2, column=0, sticky=W)
desc = Label(master, text="Descripción")
desc.grid(row=3, column=0, sticky=W)

var_titulo = StringVar()
var_ruta = StringVar()
var_desc = StringVar()

entry_titulo = Entry(master, textvariable=var_titulo, width=35)
entry_titulo.grid(row=1, column=1)
entry_ruta = Entry(master, textvariable=var_ruta, width=35)
entry_ruta.grid(row=2, column=1)
entry_desc = Entry(master, textvariable=var_desc, width=35)
entry_desc.grid(row=3, column=1)

def alta():
    print(var_titulo.get(), var_ruta.get(), var_desc.get())

def sorpresa():
    #background_label.config(background="#FFCA8D")
    master.configure(background="#FFCA8D")

boton_a = Button(master, text="Alta", command=alta)
boton_a.grid(row=4, column=0)
boton_s = Button(master, text="Sorpresa", command=sorpresa)
boton_s.grid(row=4, column=1)
master.mainloop()
