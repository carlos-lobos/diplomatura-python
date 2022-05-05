# Funcion para calcular el area
def calc_area(radio):
    A = pi*radio*radio
    return A

# Defino valor de PI
pi = 3.1416

# Pido el Radio 
val1 = input("Ingrese el radio de la circunferecia: ")
rad = int(val1)

A = calc_area(rad)
print("El área de la circunferencia de radio " + val1 + " es: " + str(A))
