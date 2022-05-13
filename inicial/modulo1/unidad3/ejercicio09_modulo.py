# Modulo para el ejercicio 9

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

def alta(id, diccdecpras):
    producto, cantidad, precio = pedir_producto("Ingrese producto cantidad y precio, en ese orden, separados por espacios, uno por linea [ENTER para terminar las ALTAS]:\n")
    if cantidad and precio:
        subtotal = int(cantidad) * int(precio)
        if producto:
            id += 1
            diccdecpras[id] = {'producto': producto, 'cantidad': int(cantidad), 'precio': int(precio), 'subtotal': subtotal}
    
    while producto and cantidad and precio:
        producto, cantidad, precio = pedir_producto("")
        if cantidad and precio:
            subtotal = int(cantidad) * int(precio)
            if producto:
                id += 1
                diccdecpras[id] = {'producto': producto, 'cantidad': int(cantidad), 'precio': int(precio), 'subtotal': subtotal}
    return id

def baja(diccdecpras):
    id2del = int(input("Ingrese el ID del producto a eliminar: "))
    diccdecpras.pop(id2del)

def consulta(diccdecpras):
    total = 0
    print(f"\nDetalle de productos comprados:")
    print(f"\tID\tPRODUCTO\tCANTIDAD\tPRECIO UNIT\tSUBTOTAL")
    print(f"\t--\t--------\t--------\t-----------\t--------")
    for id in diccdecpras:
        prod=diccdecpras[id]
        total += prod['subtotal']
        print(f"\t{id:2}\t{prod['producto']:8}\t{prod['cantidad']:8}\t{prod['precio']:11}\t{prod['subtotal']:8}")
    return total

def modificar(diccdecpras):
    id2mod = int(input("Ingrese el ID del producto a modificar: "))
    producto, cantidad, precio = pedir_producto("Ingrese producto cantidad y precio, en ese orden, separados por espacios:\n")
    if cantidad and precio:
        subtotal = int(cantidad) * int(precio)
        if producto:
            diccdecpras[id2mod] = {'producto': producto, 'cantidad': int(cantidad), 'precio': int(precio), 'subtotal': subtotal}

def menu():
    print("\nOPCIONES:\n\t1) Agregar Producto\n\t2) Eliminar Producto\n\t3) Consultar Productos\n\t4) Modificar Producto\n\t5) Finalizar Compra\n")
    opcion=int(input("Que desea hacer? (Ingrese el nro de opcion):"))
    return opcion
