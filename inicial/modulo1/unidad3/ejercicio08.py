# Basado en ejercicio06.py

from ejercicio08_modulo import alta, baja, consulta, modificar, menu

listadecpras = []

opcion = menu()

while opcion!=5:
    if opcion==1:
        alta(listadecpras)
    if opcion==2:
        baja(listadecpras)
    if opcion==3:
        consulta(listadecpras)
    if opcion==4:
        modificar(listadecpras)
    opcion = menu()

total = consulta(listadecpras)

print(f"\nEl monto total gastado es: {total}")
