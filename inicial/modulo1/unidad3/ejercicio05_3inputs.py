def pedir_producto(mensaje):
    producto = input(mensaje)
    cantidad = input()
    if cantidad=="": 
        cantidad = "0"
    precio = input()
    if precio=="": 
        precio = "0"
    return producto, cantidad, precio


total = 0

producto, cantidad, precio = pedir_producto("Ingrese producto cantidad y precio (en ese orden):\n")
if cantidad and precio:
    total += int(cantidad) * int(precio)

while producto and cantidad and precio:
    producto, cantidad, precio = pedir_producto("Ingrese nuevo producto cantidad y precio (en ese orden) [o 3 veces ENTER para terminar]:\n")
    if cantidad and precio:
        total += int(cantidad) * int(precio)

print(f"\nEl monto total gastado es: {total}")
