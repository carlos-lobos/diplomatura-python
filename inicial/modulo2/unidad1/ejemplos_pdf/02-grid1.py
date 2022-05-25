from tkinter import *

"""
* Grid(): Es otra forma de hubicar los widgets en la ventana de tkinter,
          la grilla divide la ventana en una tabla de 2 dimensiones (filasa y columnas)
          Cada celda, puede contener un elemento.
"""

root = Tk()
Label(root, text="id").grid(row=0, column=0)
Label(root, text="nombre").grid(row=1, column=0)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()
