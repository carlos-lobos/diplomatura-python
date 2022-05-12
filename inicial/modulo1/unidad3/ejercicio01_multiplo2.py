import sys

param1 = sys.argv[1]
param2 = sys.argv[2]
param3 = sys.argv[3]

parametros = [param1, param2, param3]

print("NRO - MULTIPLO DE 2")
print("---   -------------")

for num in parametros:
    if int(num)%2==0:
        print(num + "     SI")
    else:
        print(num + "     NO")
