# Basado en ejercicio07.py

from ejercicio09_modulo import alta, baja, consulta, modificar, menu

id = 0
diccdecpras = {}

opcion = menu()

while opcion!=5:
    if opcion==1:
        id=alta(id, diccdecpras)
    if opcion==2:
        baja(diccdecpras)
    if opcion==3:
        consulta(diccdecpras)
    if opcion==4:
        modificar(diccdecpras)
    opcion = menu()

total = consulta(diccdecpras)

print(f"\nEl monto total gastado es: {total}")
