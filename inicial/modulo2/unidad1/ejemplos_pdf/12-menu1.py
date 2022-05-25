from tkinter import *


def hola():
    print("Hola")

def popup(event):
    menubar.post(event.x_root,event.y_root)

master = Tk()

# Frame (creacion de una caja)
frame = Frame(master, width=512, height=512)
frame.pack()

menubar = Menu(master)

# Menu Archivo
menu_archivo = Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Abrir", command=hola)
menu_archivo.add_command(label="Guardar", command=hola)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=master.quit)
menubar.add_cascade(label="Archivo", menu=menu_archivo)

# Menu Editar
menu_edicion = Menu(menubar, tearoff=0)
menu_edicion.add_command(label="Copiar", command=hola)
menu_edicion.add_command(label="Pegar", command=hola)
menu_edicion.add_separator()
menubar.add_cascade(label="Editar", menu=menu_edicion)

# Submenu de Editar -> Transformar
submenu = Menu(menu_edicion, tearoff=True)
submenu.add_command(label="Editar color", command=hola)
submenu.add_command(label="Rotar", command=hola)
menu_edicion.add_cascade(label="Transformar", menu=submenu)

master.config(menu=menubar)

# Asociar el popup a la caja (button-3 es la referencia de TK al click derecho)
frame.bind("<Button-3>", popup)

master.mainloop()