frase = "Lorem Ipsum"

# 1ra Forma: Funcion lambda para revertir una cadena usando slicing
reversa = lambda cadena: cadena[::-1]
print(f"La frase \"{frase}\" al reves se escribe:", reversa(frase))

# 2da Forma: Funcion lambda para revertir una cadena usando recursividad
reversa2 = lambda cadena: cadena if cadena == "" else reversa2(cadena[1:])+cadena[0]
print(f"La frase \"{frase}\" al reves se escribe:", reversa2(frase))
