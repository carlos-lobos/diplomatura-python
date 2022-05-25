from tkinter import *

"""
COLORES:
--------
* Fondo: background="black" ó bg="black"
* Letra: foreground="red" ó fg="red"
* Fondo activo: : activebackground="green"
* Letra activa: : activeforeground="yellow",
* Letra deshabilitado: : disabledforeground="blue"
"""

master = Tk()

def callback():
    print("click!")

a = Button(
    master, text="OK", command=callback, padx=132, pady=132,
    activebackground="green", activeforeground="yellow",
    background="black", foreground="red"
)
a.pack()

b = Button(
    master, text="OK", command=callback, padx=132, pady=132,
    state=DISABLED, background="black", disabledforeground="blue"
)
b.pack()

mainloop()
