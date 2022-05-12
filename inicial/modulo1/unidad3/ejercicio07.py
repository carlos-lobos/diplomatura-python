# Basado en ejercicio05_inputsimple.py

def pedir_producto(mensaje):
    producto, cantidad, precio = [ "", "", "" ]
    linea = input(mensaje)
    if linea!="":
        producto, cantidad, precio = linea.split(" ")
    if cantidad=="": 
        cantidad = "0"
    if precio=="": 
        precio = "0"
    return producto, cantidad, precio

def imprimir_detalle(diccionario):
    print(f"\nDetalle de productos comprados:")
    print(f"\tPRODUCTO\tCANTIDAD\tPRECIO UNIT\tSUBTOTAL")
    print(f"\t--------\t--------\t-----------\t--------")
    for id in diccionario:
        prod=diccionario[id]
        print(f"\t{prod['producto']:8}\t{prod['cantidad']:8}\t{prod['precio']:11}\t{prod['subtotal']:8}")


total = 0

id = 1
diccdecpras = {}

producto, cantidad, precio = pedir_producto("Ingrese producto cantidad y precio, en ese orden, separados por espacios, uno por linea [ENTER para terminar]:\n")
if cantidad and precio:
    subtotal = int(cantidad) * int(precio)
    total += subtotal
    if producto:
        diccdecpras[id] = {'producto': producto, 'cantidad': int(cantidad), 'precio': int(precio), 'subtotal': subtotal}

while producto and cantidad and precio:
    producto, cantidad, precio = pedir_producto("")
    if cantidad and precio:
        subtotal = int(cantidad) * int(precio)
        total += subtotal
        if producto:
            id += 1
            diccdecpras[id] = {'producto': producto, 'cantidad': int(cantidad), 'precio': int(precio), 'subtotal': subtotal}


imprimir_detalle(diccdecpras)

print(f"\nEl monto total gastado es: {total}")
