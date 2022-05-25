from tkinter import *

"""
* Las celdas de las grillas poseen por defecto la alineacion centrada, por ello, todos los elementos aparecen centrados.
* sticky: es un atributo que permite cambiar la alineaccion del elemento,
          los valores posibles son: N, S, E y W (North, South, East, West)
"""

root = Tk()
Label(root, text="id").grid(row=0, column=0, sticky=W)
Label(root, text="nombre").grid(row=1, column=0, sticky=W)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()
