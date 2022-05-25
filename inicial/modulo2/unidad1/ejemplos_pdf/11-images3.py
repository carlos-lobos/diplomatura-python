from tkinter import *
# El método PhotoImage de PILLOW "pisa" al método PhotoImage de tkinter
from PIL.ImageTk import PhotoImage
import os
from glob import glob
import random

"""
* Pillow (actualizacion de la libreria PIL), permite trabajar con mas de 30 formatos
"""

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
ruta = os.path.join(BASE_DIR, "images")

def seleccion():
    # Selecciona randomicamente una tupla de la lista y guarda cada valor de la tupla en una variable
    nombre, foto = random.choice(image_tuple_list)
    # Cambia el texto del label por la ruta completa a la imagen que se va a mostrar
    dialogo.config(text=nombre)
    # Cambia la imagen del boton
    boton.config(image=foto)

root=Tk()
dialogo = Label(root, text="aquí va a ir la ruta", bg='OrangeRed')
boton = Button(root, text="Presionar para ver imagen", command=seleccion)

dialogo.pack(fill=BOTH)
boton.pack()

# Lista de rutas completas a todos los archivos .gif dentro de la carpeta images
rutas_list = glob(ruta + "/" + "*") # Podria haber filtrado los JPG con *.jpg
# Lista de tuplas (ruta, IMAGEN)
image_tuple_list = [(x, PhotoImage(file=x)) for x in rutas_list]
print(rutas_list)
root.mainloop()
