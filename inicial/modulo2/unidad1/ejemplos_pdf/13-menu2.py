from tkinter import *

contar = 0

def update():
    global contar
    contar = contar + 1
    menuPrueba.entryconfig(0, label=str(contar))

master = Tk()

menubar = Menu(master)

menuPrueba = Menu(menubar, tearoff=0, postcommand=update)
menuPrueba.add_command(label=str(contar))
menuPrueba.add_command(label="Salir", command=master.quit)
menubar.add_cascade(label="Prueba", menu=menuPrueba)

master.config(menu=menubar)

master.mainloop()