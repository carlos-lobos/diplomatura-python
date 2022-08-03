from tkinter import ttk
from tkinter.constants import E, W, NSEW
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button

import pwdadmin_model

class View():
    def __init__(self, master):
        self.window = master

        self.model=pwdadmin_model.Model()

        self.window.title("PWDAdmin v1.0")
        self.window.geometry("1080x490")

        style = ttk.Style(self.window)
        style.theme_use("clam")

        # Titulo
        mensaje = Label(self.window, text="PWDAdmin 1.0", fg="navy")
        mensaje.config(font=("TimesNewRoman", 15, "bold", "italic"))
        mensaje.grid(row=1, column=0, columnspan=10, sticky=E, padx=5, pady=5)

        # Etiquetas
        cat = Label(self.window, text="Categoría")
        cat.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        desc = Label(self.window, text="Descripción")
        desc.grid(row=3, column=0, sticky=W, padx=5, pady=2)
        user= Label(self.window, text="Usuario")
        user.grid(row=4, column=0, sticky=W, padx=5, pady=2)
        passw = Label(self.window, text="Contraseña")
        passw.grid(row=5, column=0, sticky=W, padx=5, pady=2)
        url = Label(self.window, text="URL")
        url.grid(row=6, column=0, sticky=W, padx=5, pady=2)
        comment = Label(self.window, text="Comentarios")
        comment.grid(row=7, column=0, sticky=W, padx=5, pady=2)

        # Variables
        var_cat = StringVar()
        var_desc = StringVar()
        var_user = StringVar()
        var_passw = StringVar()
        var_url = StringVar()
        var_comment = StringVar()

        # Cajas de texto
        entry_cat = Entry(self.window, textvariable=var_cat, width=150, bg="white")
        entry_cat.grid(row=2, column=1, columnspan=9, padx=5, pady=2, sticky=W)
        entry_desc = Entry(self.window, textvariable=var_desc, width=150, bg="white")
        entry_desc.grid(row=3, column=1, columnspan=9, padx=5, pady=2, sticky=W)
        entry_user = Entry(self.window, textvariable=var_user, width=150, bg="white")
        entry_user.grid(row=4, column=1, columnspan=9, padx=5, pady=2, sticky=W)
        entry_passw = Entry(self.window, textvariable=var_passw, width=150, bg="white")
        entry_passw.grid(row=5, column=1, columnspan=9, padx=5, pady=2, sticky=W)
        entry_url = Entry(self.window, textvariable=var_url, width=150, bg="white")
        entry_url.grid(row=6, column=1, columnspan=9, padx=5, pady=2, sticky=W)
        entry_comment = Entry(self.window, textvariable=var_comment, width=150, bg="white")
        entry_comment.grid(row=7, column=1, columnspan=9, padx=5, pady=2, sticky=W)

        # Arbol
        tree = ttk.Treeview(self.window)

        tree["columns"]=("col1", "col2", "col3", "col4", "col5", "col6")
        tree.column("#0", width=50, minwidth=50, anchor=W)
        tree.column("col1", width=100, minwidth=100, anchor=W)
        tree.column("col2", width=150, minwidth=150, anchor=W)
        tree.column("col3", width=140, minwidth=140, anchor=W)
        tree.column("col4", width=150, minwidth=150, anchor=W)
        tree.column("col5", width=200, minwidth=200, anchor=W)
        tree.column("col6", width=280, minwidth=280, anchor=W)
        tree.heading("#0", text="ID")
        tree.heading("col1", text="Categ")
        tree.heading("col2", text="Desc")
        tree.heading("col3", text="Usuario")
        tree.heading("col4", text="Passwd")
        tree.heading("col5", text="URL")
        tree.heading("col6", text="Comentarios")

        tree.grid(row=9, column=0, columnspan=10, padx=5, pady=5)

        # Botones
        boton_alta = Button(self.window, text="Alta", command=lambda:self.model.alta(tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment, entry_cat))
        boton_alta.grid(row=8, column=1, sticky=NSEW, padx=5, pady=5)
        boton_baja = Button(self.window, text="Baja", command=lambda:self.model.baja(tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment, entry_cat))
        boton_baja.grid(row=8, column=2, sticky=NSEW, padx=5, pady=5)
        boton_modif = Button(self.window, text="Modificar", command=lambda:self.model.modificar(tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment))
        boton_modif.grid(row=8, column=3, sticky=NSEW, padx=5, pady=5)
        boton_filtrar = Button(self.window, text="Buscar Usuario", command=lambda:self.model.filtrar(tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment, entry_user))
        boton_filtrar.grid(row=8, column=4, sticky=NSEW, padx=5, pady=5)

        # Rellenar el treeview
        self.model.refrescar(tree)

        # Doble click, obtiene los valores de la row de treeview y las coloca en los Entry correspondientes
        tree.bind('<Double-Button-1>', lambda event: self.model.cargar(tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment))
