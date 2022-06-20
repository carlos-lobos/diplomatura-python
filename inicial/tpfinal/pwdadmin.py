from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import sqlite3
import re
from turtle import width
import os

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
ruta_bd = os.path.join(BASE_DIR, "passwords.db")

def conexion():
    con = sqlite3.connect(ruta_bd)
    return con

def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = """CREATE TABLE IF NOT EXISTS passwords
        (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             category varchar(30) NOT NULL DEFAULT '',
             description varchar(100) NOT NULL DEFAULT '',
             username varchar(100) NOT NULL DEFAULT '',
             passwd varchar(250) NOT NULL DEFAULT '',
             url varchar(250) NOT NULL DEFAULT '',
             comments text NOT NULL DEFAULT ''
        )
    """
    cursor.execute(sql)
    con.commit()

def refrescar(mitreview):
    # Eliminamos todos los elementos anteriores del treeview
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    # Seleccionamos todos los registros de la BD
    sql = "SELECT * FROM passwords ORDER BY id DESC"
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql)

    # Agregamos todos los registros de nuevo al treeview
    resultado = datos.fetchall()
    for fila in resultado:
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))

    return True

def limpiar(limpiar_user=True):
    # Blanqueo los Entry
    var_cat.set("")
    var_desc.set("")
    if limpiar_user:
        var_user.set("")
    var_passw.set("")
    var_url.set("")
    var_comment.set("")

def alta():
    # Validar campos usuario y password
    if (var_user.get() == "" or var_passw.get() == ""):
        showerror("Error en validación", "Debe ingresar al menos usuario y contraseña")
        return False
    # Validar sintaxis de la URL
    urlvalue = var_url.get()
    result = regexp.match(urlvalue)
    if not result:
        showerror("Error en validación de URL", "La URL '" + urlvalue + "' no es válida!")
        return False
    
    # Alta en BD
    dbconn = conexion()
    cursor = dbconn.cursor()
    data = (var_cat.get(), var_desc.get(), var_user.get(), enc_pass(var_passw.get()), var_url.get(), var_comment.get())
    sql = "INSERT INTO passwords (category, description, username, passwd, url, comments) VALUES(?, ?, ?, ?, ?, ?)"
    cursor.execute(sql, data)
    dbconn.commit()

    showinfo("Alta", "El alta se realizó correctamente!")

    # Blanqueo los Entry
    limpiar()
    
    # Refrescar Arbol
    refrescar(tree)

    entry_cat.focus_set()


def baja():
    # Baja en BD
    valor = tree.selection()
    item = tree.item(valor)
    mi_id = item['text'] # text es el ID

    con=conexion()
    cursor=con.cursor()
    data = (mi_id,)
    sql = "DELETE FROM passwords WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()

    # Blanqueo los Entry
    limpiar()

    showinfo("Baja", "La baja se realizó correctamente!")

    # Refrescar Arbol
    refrescar(tree)

    entry_cat.focus_set()

def modificar():
    # Validar campos usuario y password
    if (var_user.get() == "" or var_passw.get() == ""):
        showerror("Error en validación", "Debe ingresar al menos usuario y contraseña")
        return False
    # Validar sintaxis de la URL
    urlvalue = var_url.get()
    result = regexp.match(urlvalue)
    if not result:
        showerror("Error en validación de URL", "La URL '" + urlvalue + "' no es válida!")
        return False

    # Modificacion en BD
    valor = tree.selection()
    item = tree.item(valor)
    mi_id = item['text'] # text es el ID

    con=conexion()
    cursor=con.cursor()
    data = (var_cat.get(), var_desc.get(), var_user.get(), enc_pass(var_passw.get()), var_url.get(), var_comment.get(),mi_id)
    sql = "UPDATE passwords SET category=?, description=?, username=?, passwd=?, url=?, comments=? WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()

    showinfo("Modificar", "La modificación se realizó correctamente!")

    # Refrescar Arbol
    refrescar(tree)

def filtrar():
    # Limpio los Entry que no se usan en la busqueda/filtro
    limpiar(False)

    # Filtrar en BD
    user_search = var_user.get()
    user_search = user_search.replace("'", "") # Quitamos cualquier comilla simple que pueda molestar en el SQL
    user_search = user_search.strip()          # Quitamos espacios en blanco

    if user_search == "":
        # Busqueda Vacia => listamos todos los elementos
        return refrescar(tree)

    # Eliminamos todos los elementos anteriores del treeview
    records = tree.get_children()
    for element in records:
        tree.delete(element)
    
    # Seleccionamos todos los registros de la BD cuyo username coincidan en algo con el string buscado
    con=conexion()
    cursor=con.cursor()
    sql = "SELECT * FROM passwords WHERE username LIKE '%" + user_search + "%' ORDER BY id DESC"
    datos=cursor.execute(sql)

    # Agregamos todos los registros de nuevo al treeview
    resultado = datos.fetchall()
    for fila in resultado:
        tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))

    showinfo("Filtrar", "El filtrado se realizó correctamente!")

    entry_user.focus_set()

def cargar(event):
    # Obtener los valores del registro seleccionado en el treeview
    valor = tree.selection()
    item = tree.item(valor)
    values = item['values'] # values son todos los registros que tenemos en la BD ordenados en el treeview

    # Setear los valores en cada uno de los Entry correspondientes
    var_cat.set(values[0])
    var_desc.set(values[1])
    var_user.set(values[2])
    var_passw.set(dec_pass(values[3]))
    var_url.set(values[4])
    var_comment.set(values[5])

"""
Funciones para encodeo y desencodeo de passwords
Una opción un poco más estándar: https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
"""
def enc_pass(passwd):
    enc_dicc = {'a': '#!#', 'e': '$##', 'i': '##%', 'o': '#&#', 'u': '/##'}
    for orig_let, rep_let in enc_dicc.items():
        passwd = passwd.replace(orig_let, rep_let)
    return passwd

def dec_pass(encpasswd):
    dec_dicc = {'#!#': 'a', '$##': 'e', '##%': 'i', '#&#': 'o', '/##': 'u'}
    for rep_let, orig_let in dec_dicc.items():
        encpasswd = encpasswd.replace(rep_let, orig_let)
    return encpasswd


# Creacion de la BD y Tabla
crear_tabla()


# Expresion regular para la validación de la URL para el Alta y la Modificación
patron = "^[a-zA-Z0-9:/=%\?\-\.]*$"
regexp = re.compile(patron)


# INICIO Loop de TKinter
master = Tk()
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

# Botones
boton_alta = Button(master, text="Alta", command=alta)
boton_alta.grid(row=8, column=1, sticky=NSEW, padx=5, pady=5)
boton_baja = Button(master, text="Baja", command=baja)
boton_baja.grid(row=8, column=2, sticky=NSEW, padx=5, pady=5)
boton_modif = Button(master, text="Modificar", command=modificar)
boton_modif.grid(row=8, column=3, sticky=NSEW, padx=5, pady=5)
boton_filtrar = Button(master, text="Buscar Usuario", command=filtrar)
boton_filtrar.grid(row=8, column=4, sticky=NSEW, padx=5, pady=5)

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

# Rellenar el treeview
refrescar(tree)

# Doble click, obtiene los valores de la row de treeview y las coloca en los Entry correspondientes
tree.bind('<Double-Button-1>', cargar)

# FINALIZO Loop de TKinter
master.mainloop()
