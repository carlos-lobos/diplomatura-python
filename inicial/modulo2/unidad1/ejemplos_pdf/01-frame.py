from tkinter import *

""""
* pack(): es una de las formas que se tiene de hubicar los widgets en la ventana de tkinter
* widget: son cada uno de los elementos que puede tener una ventana de tkinter, por ejemplo, Label, Frame, etc.
* Label(): es una etiqueta, sirve para escribir texto.
* Frame(): es equivalente a la etiqueta <hr> en  html, es una linea horizontal que sirve como separadora de contenido.
"""

master = Tk()
Label(text="uno").pack()
separador = Frame(master, height=2, bd=1, relief=SUNKEN)
separador.pack(fill=X, padx=5, pady=5)
Label(text="dos").pack()
mainloop()
