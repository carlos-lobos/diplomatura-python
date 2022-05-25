from tkinter import *

# askopenfilename: permite seleccionar un archivo a traves de una ventana de navegacion del sistema de archivos
from tkinter.filedialog import askopenfilename
def openfile():
    ruta = askopenfilename()
    print(ruta)

# askcolor: permite seleccionar un color desde un paleta de colores
from tkinter.colorchooser import askcolor

def callback():
    result = askcolor(color="#00ff00",title = "Bernd's Colour Chooser")
    print(result)
    print(result[1])


root = Tk()
# askopenfilename:
Button(root, text='Abrir archivo', command=openfile).pack(fill=X)
# askcolor:
Button(root, text='Seleccionar color', fg="green", command=callback).pack(side=LEFT, padx=10)
# Ejemplo de boton salir
Button(text='Cerrar', command=root.quit, fg="red").pack(side=LEFT, padx=10)

mainloop()
