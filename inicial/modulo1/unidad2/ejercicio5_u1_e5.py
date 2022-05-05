# Funcion para sumar un porcentaje a un valor
def sumar_porcentaje(valor, porcentaje):
    resultado = valor + valor*porcentaje/100
    return resultado
    
val1 = input("Ahora, por favor, ingrese un valor para sumarle un 10%: ")
porcent = 10

resultado = sumar_porcentaje(int(val1), porcent)

print("El resultado de " + val1 + " +10% es: " + str(resultado))
