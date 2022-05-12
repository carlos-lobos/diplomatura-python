oracion = input("Por favor, ingrese una oración:\n")

print("\nLa oración ingresada es: \"" + oracion + "\"")

lista = list(oracion)
nro = lista.count('a')

print("\nLa letra \"a\" aparece " + str(nro) + " veces!")
