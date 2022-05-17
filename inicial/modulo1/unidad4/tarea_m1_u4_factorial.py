# En el video que se explican las funciones recursivas,
# se dejo como tarea la realizacion de una funcion que calcule el factorial de un nro
# n! = n * n-1 * n-2 * .. * 1    (donde n es un número entero positivo o 0)

# Aplicando funcion recursiva
def fact(nro):
    if nro == 0:
        return 1
    else:
        return nro * fact(nro-1)

print("\nUsando fact():")
print("---------------")
print("\tFactorial de 0 = ", fact(0))
print("\tFactorial de 1 = ", fact(1))
print("\tFactorial de 2 = ", fact(2))
print("\tFactorial de 3 = ", fact(3))
print("\tFactorial de 4 = ", fact(4))
print("\tFactorial de 5 = ", fact(5))
