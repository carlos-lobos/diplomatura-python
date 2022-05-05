# Funcion para calcular el perimetro
def calc_perimetro(radio):
    L = 2*pi*radio
    return L

# Defino valor de PI
pi = 3.1416

# Pido el Radio 
val1 = input("Ingrese el radio de la circunferecia: ")
rad = int(val1)

L = calc_perimetro(rad)
print("El perímetro de la circunferencia de radio " + val1 + " es: " + str(L))
