import sys

param1 = sys.argv[1]
param2 = sys.argv[2]
param3 = sys.argv[3]

# Alternativa al ejercicio 2, sin uso de if (porque en clases no se habia dado todavia)

print("Si el resultado de realizar el modulo == 0, entonces el nro es multiplo de 2: ")

print("Resultado del primer  parametro '" + param1 + "': " + str(int(param1)%2))
print("Resultado del segundo parametro '" + param2 + "': " + str(int(param2)%2))
print("Resultado del tercer  parametro '" + param3 + "': " + str(int(param3)%2))
