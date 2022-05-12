oracion = input("Por favor, ingrese una oración:\n")

# Oración de EJemplo: "AÁaá EÉeé IÍíi OÓóo UÚúu"
print("\nLa oración ingresada es: \"" + oracion + "\"\n")

lista = list(oracion.lower()) 

# Declaracion de vocales a buscar y sus casos especiales (vocales acentuadas)
# (Un diccionario que contiene listas)
vocales = {
    'a': ['a', 'á'],
    'e': ['e', 'é'],
    'i': ['i', 'í'],
    'o': ['o', 'ó'],
    'u': ['u', 'ú'],
}

for vocal in vocales.keys():
    v1, v2 = vocales[vocal]
    nro = lista.count(v1) + lista.count(v2)
    print("La letra \""+vocal+"\" aparece " + str(nro) + " veces!")
