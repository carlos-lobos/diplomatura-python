def solicitaredad():
    edad = int(input("Por favor, ingrese su edad: "))
    
    listaedades = []
    for i in range(1, edad+1):
        listaedades.append(str(i))
    print(", ".join(listaedades))

    listaedades_rev = []
    for i in range(edad, 0, -1):
        listaedades_rev.append(str(i))
    print(", ".join(listaedades_rev))


solicitaredad()
