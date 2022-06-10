from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import sqlite3
import re


def db_connect():
    con = sqlite3.connect("productos.db")
    return con


def create_table():
    conn = db_connect()
    cursor = conn.cursor()
    sql = """
        CREATE TABLE IF NOT EXISTS productos (
            id integer primary key autoincrement,
            producto text,
            descripcion text
        )
    """
    cursor.execute(sql)
    conn.commit()


def alta():
    patron = "^[a-zA-Z0-9]*$"
    if re.match(patron,var_prod.get()):
      conn=db_connect()
      cursor=conn.cursor()
      data=(var_prod.get(), var_desc.get())
      sql="INSERT INTO productos (producto, descripcion) VALUES (?, ?)"
      cursor.execute(sql, data)
      conn.commit()
      var_prod.set("")
      var_desc.set("")
      actualizar(tree)
    else:
      showerror('Producto Inválido', "El producto solo puede contener caracteres alfanuméricos!")
     

def actualizar(arbol):
    # Elimino las filas del arbol
    records = arbol.get_children()
    for element in records:
        arbol.delete(element)

    # Consulto todos los productos desde la BD
    conn=db_connect()
    cursor=conn.cursor()
    sql = "SELECT * FROM productos ORDER BY id DESC"
    datos=cursor.execute(sql)
    resultado = datos.fetchall()

    # Agrego los productos al arbol
    for row in resultado:
        arbol.insert("", 0, text=row[0], values=(row[1], row[2]))


create_table()

# Inicia Loop Tkinter
app = Tk()
app.geometry("360x320")

# Etiquetas
product = Label(app, text="Producto")
product.grid(row=1, column=0, sticky=W)
desc=Label(app, text="Descripción")
desc.grid(row=2, column=0, sticky=W)

# Variables
var_prod = StringVar()
var_desc = StringVar()

# Cajas de texto
entrada1 = Entry(app, textvariable=var_prod) 
entrada1.grid(row=1, column=1, sticky=NSEW)
entrada2 = Entry(app, textvariable=var_desc) 
entrada2.grid(row=2, column=1, sticky=NSEW)

# Botones
boton = Button(text="Agregar", command=alta)
boton.grid(row=3, column=1, sticky=NSEW)

# Arbol
tree = ttk.Treeview(app)

tree["columns"]=("col1", "col2")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=100, minwidth=100, anchor=W)
tree.column("col2", width=200, minwidth=200, anchor=W)
tree.heading("#0", text="ID")
tree.heading("col1", text="Producto")
tree.heading("col2", text="Descripción")
actualizar(tree)

tree.grid(row=4, column=0, columnspan=2)

# Finaliza Loop Tkinter
app.mainloop()
