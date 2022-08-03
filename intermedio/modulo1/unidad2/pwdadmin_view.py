from tkinter import ttk
from tkinter.constants import E, W, NSEW
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button

from pwdadmin_model import refrescar
from pwdadmin_model import cargar
from pwdadmin_model import alta
from pwdadmin_model import baja
from pwdadmin_model import modificar
from pwdadmin_model import filtrar

def show_view(master):
    master.title("PWDAdmin v1.0")
    master.geometry("1080x490")

    style = ttk.Style(master)
    style.theme_use("clam")

    # Titulo
    mensaje = Label(master, text="PWDAdmin 1.0", fg="navy")
    mensaje.config(font=("TimesNewRoman", 15, "bold", "italic"))
    mensaje.grid(row=1, column=0, columnspan=10, sticky=E, padx=5, pady=5)

    # Etiquetas
    cat = Label(master, text="Categoría")
    cat.grid(row=2, column=0, sticky=W, padx=5, pady=2)
    desc = Label(master, text="Descripción")
    desc.grid(row=3, column=0, sticky=W, padx=5, pady=2)
    user= Label(master, text="Usuario")
    user.grid(row=4, column=0, sticky=W, padx=5, pady=2)
    passw = Label(master, text="Contraseña")
    passw.grid(row=5, column=0, sticky=W, padx=5, pady=2)
    url = Label(master, text="URL")
    url.grid(row=6, column=0, sticky=W, padx=5, pady=2)
    comment = Label(master, text="Comentarios")
    comment.grid(row=7, column=0, sticky=W, padx=5, pady=2)

    # Variables
    var_cat = StringVar()
    var_desc = StringVar()
    var_user = StringVar()
    var_passw = StringVar()
    var_url = StringVar()
    var_comment = StringVar()

    # Cajas de texto
    entry_cat = Entry(master, textvariable=var_cat, width=150, bg="white")
    entry_cat.grid(row=2, column=1, columnspan=9, padx=5, pady=2, sticky=W)
    entry_desc = Entry(master, textvariable=var_desc, width=150, bg="white")
    entry_desc.grid(row=3, column=1, columnspan=9, padx=5, pady=2, sticky=W)
    entry_user = Entry(master, textvariable=var_user, width=150, bg="white")
    entry_user.grid(row=4, column=1, columnspan=9, padx=5, pady=2, sticky=W)
    entry_passw = Entry(master, textvariable=var_passw, width=150, bg="white")
    entry_passw.grid(row=5, column=1, columnspan=9, padx=5, pady=2, sticky=W)
    entry_url = Entry(master, textvariable=var_url, width=150, bg="white")
    entry_url.grid(row=6, column=1, columnspan=9, padx=5, pady=2, sticky=W)
    entry_comment = Entry(master, textvariable=var_comment, width=150, bg="white")
    entry_comment.grid(row=7, column=1, columnspan=9, padx=5, pady=2, sticky=W)

    # Arbol
    tree = ttk.Treeview(master)

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
    boton_alta = Button(master, text="Alta", command=lambda:alta(tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment, entry_cat))
    boton_alta.grid(row=8, column=1, sticky=NSEW, padx=5, pady=5)
    boton_baja = Button(master, text="Baja", command=lambda:baja(tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment, entry_cat))
    boton_baja.grid(row=8, column=2, sticky=NSEW, padx=5, pady=5)
    boton_modif = Button(master, text="Modificar", command=lambda:modificar(tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment))
    boton_modif.grid(row=8, column=3, sticky=NSEW, padx=5, pady=5)
    boton_filtrar = Button(master, text="Buscar Usuario", command=lambda:filtrar(tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment, entry_user))
    boton_filtrar.grid(row=8, column=4, sticky=NSEW, padx=5, pady=5)

    # Rellenar el treeview
    refrescar(tree)

    # Doble click, obtiene los valores de la row de treeview y las coloca en los Entry correspondientes
    tree.bind('<Double-Button-1>', lambda event: cargar(tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment))
