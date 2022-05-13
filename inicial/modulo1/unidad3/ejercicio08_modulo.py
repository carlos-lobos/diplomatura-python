# Modulo para el ejercicio 8

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

def alta(listadecpras):
    producto, cantidad, precio = pedir_producto("Ingrese producto cantidad y precio, en ese orden, separados por espacios, uno por linea [ENTER para terminar las ALTAS]:\n")
    if cantidad and precio:
        subtotal = int(cantidad) * int(precio)
        if producto:
            listadecpras.append([producto, int(cantidad), int(precio), subtotal])
    
    while producto and cantidad and precio:
        producto, cantidad, precio = pedir_producto("")
        if cantidad and precio:
            subtotal = int(cantidad) * int(precio)
            if producto:
                listadecpras.append([producto, int(cantidad), int(precio), subtotal])

def baja(listadecpras):
    id2del = int(input("Ingrese el ID del producto a eliminar: "))
    listadecpras.pop(id2del)

def consulta(listadecpras):
    total = 0
    print(f"\nDetalle de productos comprados:")
    print(f"\tID\tPRODUCTO\tCANTIDAD\tPRECIO UNIT\tSUBTOTAL")
    print(f"\t--\t--------\t--------\t-----------\t--------")
    for id in range(0, len(listadecpras)):
        prod = listadecpras[id]
        total += prod[3]
        print(f"\t{id:2}\t{prod[0]:8}\t{prod[1]:8}\t{prod[2]:11}\t{prod[3]:8}")
    return total

def modificar(listadecpras):
    id2mod = int(input("Ingrese el ID del producto a modificar: "))
    producto, cantidad, precio = pedir_producto("Ingrese producto cantidad y precio, en ese orden, separados por espacios:\n")
    if cantidad and precio:
        subtotal = int(cantidad) * int(precio)
        if producto:
            listadecpras[id2mod] = [producto, int(cantidad), int(precio), subtotal]

def menu():
    print("\nOPCIONES:\n\t1) Agregar Producto\n\t2) Eliminar Producto\n\t3) Consultar Productos\n\t4) Modificar Producto\n\t5) Finalizar Compra\n")
    opcion=int(input("Que desea hacer? (Ingrese el nro de opcion):"))
    return opcion
