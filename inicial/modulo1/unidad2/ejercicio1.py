import sys

param1 = sys.argv[1]
param2 = sys.argv[2]
param3 = sys.argv[3]

print("NRO - MULTIPLO DE 2")
print("---   -------------")

if int(param1)%2==0:
    print(param1 + "     SI")
else:
    print(param1 + "     NO")

if int(param2)%2==0:
    print(param2 + "     SI")
else:
    print(param2 + "     NO")

if int(param3)%2==0:
    print(param3 + "     SI")
else:
    print(param3 + "     NO")
