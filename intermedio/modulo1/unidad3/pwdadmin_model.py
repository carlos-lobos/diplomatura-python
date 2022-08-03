import os
import sqlite3
from tkinter.messagebox import *
import re

class Model():
    def __init__(self, ):
        BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
        self.ruta_bd = os.path.join(BASE_DIR, "passwords.db")

        # Expresion regular para la validación de la URL para el Alta y la Modificación
        patron = "^[a-zA-Z0-9:/=%\?\-\.]*$"
        self.regexp = re.compile(patron)

        # Creacion de la BD y Tabla
        self.crear_tabla()

    def conexion(self, ):
        con = sqlite3.connect(self.ruta_bd)
        return con

    def crear_tabla(self, ):
        con = self.conexion()
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

    def refrescar(self, mitreview):
        # Eliminamos todos los elementos anteriores del treeview
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

        # Seleccionamos todos los registros de la BD
        sql = "SELECT * FROM passwords ORDER BY id DESC"
        con=self.conexion()
        cursor=con.cursor()
        datos=cursor.execute(sql)

        # Agregamos todos los registros de nuevo al treeview
        resultado = datos.fetchall()
        for fila in resultado:
            mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))

        return True

    def limpiar(self, var_cat, var_desc, var_user, var_passw, var_url, var_comment, limpiar_user=True):
        # Blanqueo los Entry
        var_cat.set("")
        var_desc.set("")
        if limpiar_user:
            var_user.set("")
        var_passw.set("")
        var_url.set("")
        var_comment.set("")

    def alta(self, tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment, entry_cat):
        # Validar campos usuario y password
        if (var_user.get() == "" or var_passw.get() == ""):
            showerror("Error en validación", "Debe ingresar al menos usuario y contraseña")
            return False
        # Validar sintaxis de la URL
        urlvalue = var_url.get()
        result = self.regexp.match(urlvalue)
        if not result:
            showerror("Error en validación de URL", "La URL '" + urlvalue + "' no es válida!")
            return False
        
        # Alta en BD
        dbconn = self.conexion()
        cursor = dbconn.cursor()
        data = (var_cat.get(), var_desc.get(), var_user.get(), self.enc_pass(var_passw.get()), var_url.get(), var_comment.get())
        sql = "INSERT INTO passwords (category, description, username, passwd, url, comments) VALUES(?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, data)
        dbconn.commit()

        showinfo("Alta", "El alta se realizó correctamente!")

        # Blanqueo los Entry
        self.limpiar(var_cat, var_desc, var_user, var_passw, var_url, var_comment)
        
        # Refrescar Arbol
        self.refrescar(tree)

        entry_cat.focus_set()


    def baja(self, tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment, entry_cat):
        # Baja en BD
        valor = tree.selection()
        item = tree.item(valor)
        mi_id = item['text'] # text es el ID

        con=self.conexion()
        cursor=con.cursor()
        data = (mi_id,)
        sql = "DELETE FROM passwords WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()

        # Blanqueo los Entry
        self.limpiar(var_cat, var_desc, var_user, var_passw, var_url, var_comment)

        showinfo("Baja", "La baja se realizó correctamente!")

        # Refrescar Arbol
        self.refrescar(tree)

        entry_cat.focus_set()

    def modificar(self, tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment):
        # Validar campos usuario y password
        if (var_user.get() == "" or var_passw.get() == ""):
            showerror("Error en validación", "Debe ingresar al menos usuario y contraseña")
            return False
        # Validar sintaxis de la URL
        urlvalue = var_url.get()
        result = self.regexp.match(urlvalue)
        if not result:
            showerror("Error en validación de URL", "La URL '" + urlvalue + "' no es válida!")
            return False

        # Modificacion en BD
        valor = tree.selection()
        item = tree.item(valor)
        mi_id = item['text'] # text es el ID

        con=self.conexion()
        cursor=con.cursor()
        data = (var_cat.get(), var_desc.get(), var_user.get(), self.enc_pass(var_passw.get()), var_url.get(), var_comment.get(),mi_id)
        sql = "UPDATE passwords SET category=?, description=?, username=?, passwd=?, url=?, comments=? WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()

        showinfo("Modificar", "La modificación se realizó correctamente!")

        # Refrescar Arbol
        self.refrescar(tree)

    def filtrar(self, tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment, entry_user):
        # Limpio los Entry que no se usan en la busqueda/filtro
        self.limpiar(var_cat, var_desc, var_user, var_passw, var_url, var_comment, False)

        # Filtrar en BD
        user_search = var_user.get()
        user_search = user_search.replace("'", "") # Quitamos cualquier comilla simple que pueda molestar en el SQL
        user_search = user_search.strip()          # Quitamos espacios en blanco

        if user_search == "":
            # Busqueda Vacia => listamos todos los elementos
            return self.refrescar(tree)

        # Eliminamos todos los elementos anteriores del treeview
        records = tree.get_children()
        for element in records:
            tree.delete(element)
        
        # Seleccionamos todos los registros de la BD cuyo username coincidan en algo con el string buscado
        con=self.conexion()
        cursor=con.cursor()
        sql = "SELECT * FROM passwords WHERE username LIKE '%" + user_search + "%' ORDER BY id DESC"
        datos=cursor.execute(sql)

        # Agregamos todos los registros de nuevo al treeview
        resultado = datos.fetchall()
        for fila in resultado:
            tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4], fila[5], fila[6]))

        showinfo("Filtrar", "El filtrado se realizó correctamente!")

        entry_user.focus_set()

    def cargar(self, tree, var_cat, var_desc, var_user, var_passw, var_url, var_comment):
        # Obtener los valores del registro seleccionado en el treeview
        valor = tree.selection()
        item = tree.item(valor)
        values = item['values'] # values son todos los registros que tenemos en la BD ordenados en el treeview

        # Setear los valores en cada uno de los Entry correspondientes
        var_cat.set(values[0])
        var_desc.set(values[1])
        var_user.set(values[2])
        var_passw.set(self.dec_pass(values[3]))
        var_url.set(values[4])
        var_comment.set(values[5])

    """
    Funciones para encodeo y desencodeo de passwords
    Una opción un poco más estándar: https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
    """
    def enc_pass(self, passwd):
        enc_dicc = {'a': '#!#', 'e': '$##', 'i': '##%', 'o': '#&#', 'u': '/##'}
        for orig_let, rep_let in enc_dicc.items():
            passwd = passwd.replace(orig_let, rep_let)
        return passwd

    def dec_pass(self, encpasswd):
        dec_dicc = {'#!#': 'a', '$##': 'e', '##%': 'i', '#&#': 'o', '/##': 'u'}
        for rep_let, orig_let in dec_dicc.items():
            encpasswd = encpasswd.replace(rep_let, orig_let)
        return encpasswd
