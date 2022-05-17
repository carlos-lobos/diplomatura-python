# En el video que se explican las funciones recursivas,
# se dejo como tarea la realizacion de una funcion que calcule el factorial de un nro
# n! = n * n-1 * n-2 * .. * 1    (donde n es un número entero positivo o 0)

# 1ra forma (Aplicando funcion con uso de un loop while para calcular) - [9 Lineas de código]
def fact1(nro):
    fact = 1
    while nro >=0:
        if nro == 0:
            fact = fact * 1
        else:
            fact = fact * nro
        nro -= 1
    return fact

# 2da forma (Aplicando funcion recursiva) - [5 Lineas de código]
def fact2(nro):
    if nro == 0:
        return 1
    else:
        return nro * fact2(nro-1)

# 3ra forma (Aplicando Recursividad indirecta + uso funcion lambda) - [6 Lineas de código]
lfact3 = lambda nro : nro * fact3(nro-1)

def fact3(nro):
    if nro == 0:
        return 1
    else:
        return lfact3(nro)

# 4ta forma (Aplicando Recursividad ternaria + uso de funcion lambda) - [3 Lineas de código]
lfact4 = lambda nro : nro * fact4(nro-1)

def fact4(nro):
    return 1 if nro == 0 else lfact4(nro)

# 5ta forma (Aplicando funcion recursiva ternaria) - [2 Lineas de código]
def fact5(nro):
    return 1 if nro == 0 else nro * fact5(nro-1)

# 6ta forma (Aplicando funcion lambda con recursividad ternaria dentro) - [1 Linea de código]
lfact6 = lambda nro : 1 if nro == 0 else nro * lfact6(nro-1)

print("\nUsando fact1():")
print("---------------")
print("\tFactorial de 0 = ", fact1(0))
print("\tFactorial de 1 = ", fact1(1))
print("\tFactorial de 2 = ", fact1(2))
print("\tFactorial de 3 = ", fact1(3))
print("\tFactorial de 4 = ", fact1(4))
print("\tFactorial de 5 = ", fact1(5))

print("\nUsando fact2():")
print("---------------")
print("\tFactorial de 0 = ", fact2(0))
print("\tFactorial de 1 = ", fact2(1))
print("\tFactorial de 2 = ", fact2(2))
print("\tFactorial de 3 = ", fact2(3))
print("\tFactorial de 4 = ", fact2(4))
print("\tFactorial de 5 = ", fact2(5))

print("\nUsando fact3():")
print("---------------")
print("\tFactorial de 0 = ", fact3(0))
print("\tFactorial de 1 = ", fact3(1))
print("\tFactorial de 2 = ", fact3(2))
print("\tFactorial de 3 = ", fact3(3))
print("\tFactorial de 4 = ", fact3(4))
print("\tFactorial de 5 = ", fact3(5))

print("\nUsando fact4():")
print("---------------")
print("\tFactorial de 0 = ", fact4(0))
print("\tFactorial de 1 = ", fact4(1))
print("\tFactorial de 2 = ", fact4(2))
print("\tFactorial de 3 = ", fact4(3))
print("\tFactorial de 4 = ", fact4(4))
print("\tFactorial de 5 = ", fact4(5))

print("\nUsando fact5():")
print("---------------")
print("\tFactorial de 0 = ", fact5(0))
print("\tFactorial de 1 = ", fact5(1))
print("\tFactorial de 2 = ", fact5(2))
print("\tFactorial de 3 = ", fact5(3))
print("\tFactorial de 4 = ", fact5(4))
print("\tFactorial de 5 = ", fact5(5))

print("\nUsando lfact6():")
print("---------------")
print("\tFactorial de 0 = ", lfact6(0))
print("\tFactorial de 1 = ", lfact6(1))
print("\tFactorial de 2 = ", lfact6(2))
print("\tFactorial de 3 = ", lfact6(3))
print("\tFactorial de 4 = ", lfact6(4))
print("\tFactorial de 5 = ", lfact6(5))
