from tkinter import *
import sqlite3

"""
TAREA 2
    A partir del ejercicio desafío de la unidad anterior:
        cree una aplicación que permita realizar un alta de registros en la base de datos (sqlite3) 
"""

def crear_base():
    dbconn = sqlite3.connect('tarea_m2_u2_desafio_tarea2.db')
    return dbconn

def crear_tabla(dbconn):
    cursor = dbconn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS libros(id integer PRIMARY KEY autoincrement, titulo text, ruta text, descripcion text)"
    cursor.execute(sql)
    dbconn.commit()


dbconn = crear_base()
crear_tabla(dbconn)

master = Tk()
master.title("Tarea-M2-U2-Python Inicial")
master.geometry("400x150")

mensaje = Label(master, text="Ingrese los siguientes datos:", bg="purple", fg="white")
mensaje.grid(row=0, column=0, columnspan=3, sticky=NSEW)

titulo = Label(master, text="Título")
titulo.grid(row=1, column=0, sticky=W)
ruta = Label(master, text="Ruta")
ruta.grid(row=2, column=0, sticky=W)
desc = Label(master, text="Descripción")
desc.grid(row=3, column=0, sticky=W)

var_titulo = StringVar()
var_ruta = StringVar()
var_desc = StringVar()

entry_titulo = Entry(master, textvariable=var_titulo, width=35)
entry_titulo.grid(row=1, column=1)
entry_ruta = Entry(master, textvariable=var_ruta, width=35)
entry_ruta.grid(row=2, column=1)
entry_desc = Entry(master, textvariable=var_desc, width=35)
entry_desc.grid(row=3, column=1)

def alta():
    global dbconn
    cursor = dbconn.cursor()
    data = (var_titulo.get(), var_ruta.get(),  var_desc.get())
    print("Insertando datos: ", data)
    sql = "INSERT INTO libros(titulo, ruta, descripcion) VALUES(?, ?, ?)"
    cursor.execute(sql, data)
    dbconn.commit()

def sorpresa():
    master.configure(background="#FFCA8D")

boton_a = Button(master, text="Alta", command=alta)
boton_a.grid(row=4, column=0)
boton_s = Button(master, text="Sorpresa", command=sorpresa)
boton_s.grid(row=4, column=1)
master.mainloop()
