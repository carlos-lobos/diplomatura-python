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

def imprimir_detalle(lista):
    print(f"\nDetalle de productos comprados:")
    print(f"\tPRODUCTO\tCANTIDAD\tPRECIO UNIT\tSUBTOTAL")
    print(f"\t--------\t--------\t-----------\t--------")
    for prod in lista:
        print(f"\t{prod[0]:8}\t{prod[1]:8}\t{prod[2]:11}\t{prod[3]:8}")


total = 0
listadecpras = []

producto, cantidad, precio = pedir_producto("Ingrese producto cantidad y precio, en ese orden, separados por espacios, uno por linea [ENTER para terminar]:\n")
if cantidad and precio:
    subtotal = int(cantidad) * int(precio)
    total += subtotal
    if producto:
        listadecpras.append([producto, int(cantidad), int(precio), subtotal])

while producto and cantidad and precio:
    producto, cantidad, precio = pedir_producto("")
    if cantidad and precio:
        subtotal = int(cantidad) * int(precio)
        total += subtotal
        if producto:
            listadecpras.append([producto, int(cantidad), int(precio), subtotal])

imprimir_detalle(listadecpras)

print(f"\nEl monto total gastado es: {total}")
