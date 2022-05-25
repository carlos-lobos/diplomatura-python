from tkinter import *

"""
Estas opciones de posicionamiento sirven para botones, textos e imagenes
"""

master = Tk()
master.geometry("300x300")

def callback():
    print("click!")

# anchor: Posicion de la imagen. Valores posibles: N, NE, E, SE, S, SW, W, NW, o CENTER (es el valore por defecto)
a = Button(
    master, text="OK", command=callback,
    activebackground="green", activeforeground="yellow",
    background="black", foreground="red", height=7, width=12, anchor=SW
)

# side: Posicion del boton. Valores posibles: LEFT, TOP, RIGHT, BOTTOM
a.pack(side=LEFT)

# font: Fuente del texto, es una tupla de 3 valores ('tipo', tamaño, 'peso')
# Ejemplos tipo: 'courier', 'times', 'sans'
b = Button(
    master, text="Ok!", anchor=W, justify=LEFT, padx=22,
    height=3, width=12, font=('times', 22, 'bold')
)
b.pack(fill=BOTH, expand=1)

mainloop()
