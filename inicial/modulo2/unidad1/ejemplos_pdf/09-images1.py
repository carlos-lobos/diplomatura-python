from tkinter import *
import os

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
ruta = os.path.join(BASE_DIR, "images", "downloading.gif")

win = Tk()
# Boton con la imagen dentro
imagen = PhotoImage(file=ruta)
Button(win, image=imagen).pack()

# canvas que imprime la imagen en la ventana
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=imagen, anchor=NW)

win.mainloop()

