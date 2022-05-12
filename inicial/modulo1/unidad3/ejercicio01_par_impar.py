import sys

param1 = sys.argv[1]
param2 = sys.argv[2]
param3 = sys.argv[3]

parametros = [param1, param2, param3]

print("NRO - PAR/IMPAR")
print("---   ---------")

for num in parametros:
    if int(num)%2==0:
        print(num + "     PAR")
    else:
        print(num + "     IMPAR")
