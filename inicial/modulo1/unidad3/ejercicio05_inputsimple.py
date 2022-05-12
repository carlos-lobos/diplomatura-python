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


total = 0

producto, cantidad, precio = pedir_producto("Ingrese producto cantidad y precio, en ese orden, separados por espacios, uno por linea [ENTER para terminar]:\n")
if cantidad and precio:
    total += int(cantidad) * int(precio)

while producto and cantidad and precio:
    producto, cantidad, precio = pedir_producto("")
    if cantidad and precio:
        total += int(cantidad) * int(precio)

print(f"\nEl monto total gastado es: {total}")
