# 1ra Forma
par = lambda nro: nro%2 == 0

def msgParImpar(nro):
    if par(nro):
        print(f"El nro {nro} es Par!")
    else:
        print(f"El nro {nro} es Impar!")

nro1 = 1
msgParImpar(nro1)
nro2 = 2
msgParImpar(nro2)
nro3 = 3
msgParImpar(nro3)
nro4 = 4
msgParImpar(nro4)

print("")

# 2da Forma
parimpar = lambda nro: "Par!" if nro%2 == 0 else "Impar!"

nro1 = 1
print(f"El nro {nro1} es", parimpar(nro1))
nro2 = 2
print(f"El nro {nro2} es", parimpar(nro2))
nro3 = 3
print(f"El nro {nro3} es", parimpar(nro3))
nro4 = 4
print(f"El nro {nro4} es", parimpar(nro4))
