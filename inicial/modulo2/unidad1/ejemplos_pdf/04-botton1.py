from tkinter import *
import os

"""
* Button(): elemento botón, puede estar asociado a una funcion de callback 
            [donde el boton va a llamar (call) al volver (back) al programa python]
"""

master = Tk()

def callback():
    print("click!")

b = Button(master, text="OK", command=callback)
b.pack()

# state: es posible deshabilitar un boton agregando el atributo estado en "DISABLED" (deshabilitado)
c = Button(master, text="Help", state=DISABLED)
c.pack()

# padx, pady: es posible agregar un padding, a traves de estas 2, indicando un espacio interno entre el texto del boton y su contorno.
d = Button(master, text="OK2", command=callback, padx=15, pady=15)
d.pack()

# height, width: El alto y ancho de un botón de texto está dado en unidades de texto, mientras que si es una imagen, se trabaja en px.
e = Button(master, text="Sure!", anchor=W, justify=LEFT, padx=22, height=3, width=12)
e.pack(fill=BOTH, expand=1)

# En kubuntu 20.04 tuve que usar el modulo os para poder encontrar la imagen
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
ruta = os.path.join(BASE_DIR, "images", "downloading.gif")
photo=PhotoImage(file=ruta)
f = Button(master, text="Sure 2!", anchor=W, justify=LEFT, image=photo)
f.pack(fill=BOTH, expand=1)

mainloop()
