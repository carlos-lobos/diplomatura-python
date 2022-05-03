
# En el segundo video donde se trató listas y se toco algo de diccionarios,
# se dejo la tarea de intentar realizar un ejemplo similar al visto con listas pero utilizando diccionarios

persona1 = {"nombre": "Pepe", "apellido": "Argento"}
persona2 = {"nombre": "Moni", "apellido": "Argento"}
persona3 = {"nombre": "Coqui", "apellido": "Argento"}
persona4 = {"nombre": "Paola", "apellido": "Argento"}
persona5 = {"nombre": "Fatiga", "apellido": "Argento"}

dic_argentos = {
    "1": persona1,
    "2": persona2,
    "3": persona3,
    "4": persona4,
    "5": persona5,
}

codigo, persona = list(dic_argentos.items())[0]
nombre = persona.get("nombre")
apellido = persona.get("apellido")

print(codigo, nombre, apellido)
